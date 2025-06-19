import os
import csv
import time
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.exceptions import RequestException
from colorama import Fore, Style, init

init(autoreset=True)


def animated_banner():
    banner_lines = [
        f"{Fore.GREEN}W       W {Fore.BLUE}   AAAAA  {Fore.CYAN} JJJJJ{Fore.LIGHTMAGENTA_EX}   AAAAA  {Fore.YELLOW} H   H {Fore.RED}  AAAAA  {Fore.LIGHTGREEN_EX}TTTTTTT",
        f"{Fore.GREEN}W       W {Fore.BLUE}  A     A {Fore.CYAN}   J  {Fore.LIGHTMAGENTA_EX}  A     A {Fore.YELLOW} H   H {Fore.RED} A     A {Fore.LIGHTGREEN_EX}   T",
        f"{Fore.GREEN}W   W   W {Fore.BLUE}  AAAAAAA {Fore.CYAN}   J  {Fore.LIGHTMAGENTA_EX}  AAAAAAA {Fore.YELLOW} HHHHH {Fore.RED} AAAAAAA {Fore.LIGHTGREEN_EX}   T",
        f"{Fore.GREEN}W  W W  W {Fore.BLUE}  A     A {Fore.CYAN}J  J  {Fore.LIGHTMAGENTA_EX}  A     A {Fore.YELLOW} H   H {Fore.RED} A     A {Fore.LIGHTGREEN_EX}   T",
        f"{Fore.GREEN}W   W   W {Fore.BLUE}  A     A {Fore.CYAN}  J   {Fore.LIGHTMAGENTA_EX}  A     A {Fore.YELLOW} H   H {Fore.RED} A     A {Fore.LIGHTGREEN_EX}   T",
    ]
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + "\nLaunching WhatsApp Link Validator by Wajahat Ali Mir...\n")
    for line in banner_lines:
        print(line)
        time.sleep(0.01)
    print(Fore.GREEN + "\nLet's begin!\n")
    time.sleep(0.5)


def verify_whatsapp_link(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        h3_element = soup.find('h3', class_='_9vd5 _9scr', style='color:#5E5E5E;')

        if h3_element and h3_element.text.strip():
            group_name = h3_element.text.strip()
            print(f"[ {Fore.GREEN}✔️{Fore.WHITE} ] {Fore.GREEN}Available{Fore.WHITE} ~ {Fore.CYAN}{url}{Fore.WHITE}: {group_name}")
            return (group_name, url)
        else:
            print(f"[ {Fore.RED}✖️{Fore.WHITE} ] {Fore.RED}Not Found{Fore.WHITE} ~ {Fore.RED}{url}")
    except RequestException as e:
        print(f"[ {Fore.RED}ERROR{Fore.WHITE} ] Could not access {url}. Details: {str(e)}")
    return None


def list_txt_files():
    txt_files = [file for file in os.listdir() if file.endswith('.txt')]
    if not txt_files:
        print(f"{Fore.RED}No .txt files found in the current directory.")
        exit(1)

    print(f"{Fore.YELLOW}Available .txt files:")
    file_dict = {index + 1: file for index, file in enumerate(txt_files)}
    for number, file in file_dict.items():
        print(f"[ {number} ] {file}")
    return file_dict


def get_number_input(message, minimum=1, maximum=None):
    while True:
        try:
            number = int(input(f"{Fore.CYAN}{message}{Fore.WHITE} "))
            if number < minimum or (maximum and number > maximum):
                raise ValueError
            return number
        except ValueError:
            print(f"{Fore.RED}Invalid input. Try again.")


def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Group Name", "WhatsApp Link"])
        writer.writerows(data)

def main():
    animated_banner()
    files = list_txt_files()

    file_number = get_number_input("Enter the number of the file you want to use:", 1, len(files))
    selected_file = files[file_number]

    with open(selected_file, 'r', encoding='utf-8') as file:
        urls = list(set(file.read().splitlines()))  # remove duplicates

    if not urls:
        print(f"{Fore.RED}The selected file is empty.")
        return

    threads = get_number_input("How many threads do you want to use? (1-30):", 1, 30)
    output_filename = input(f"{Fore.CYAN}Enter the CSV filename to save the available links (e.g., output.csv):{Fore.WHITE} ").strip()
    if not output_filename.lower().endswith('.csv'):
        output_filename += '.csv'

    print(f"\n{Fore.YELLOW}Starting verification of {len(urls)} WhatsApp group links...\n")

    valid_links = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_url = {executor.submit(verify_whatsapp_link, url): url for url in urls}
        for i, future in enumerate(as_completed(future_to_url), 1):
            result = future.result()
            if result:
                valid_links.append(result)
            print(f"{Fore.BLUE}Progress: {i}/{len(urls)} checked", end='\r')

    save_to_csv(valid_links, output_filename)
    print(f"\n\n{Fore.GREEN}Done! Valid WhatsApp links saved to: {output_filename}")


if __name__ == "__main__":
    main()