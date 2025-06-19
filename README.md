📌 WhatsApp Group Link Checker by Wajahat Ali Mir

A Python-powered tool to scan and verify the status of WhatsApp group invite links in bulk. Whether you're a digital community manager, automation nerd, or someone who manages a massive list of WhatsApp groups — this script helps you find out which links are active, expired, or broken.

🚀 Features

Bulk check: Scan multiple WhatsApp group links at once

Detect expired or invalid links

Import from file: Easily check links from a .txt or .csv

Export results: Save active/inactive links separately

Minimal setup: Clean, readable Python script

Fast & reliable: Uses requests and simple HTTP checks

🧰 Requirements

Python 3.7+

requests library

To install dependencies:
pip install requests

📁 File Structure

whatsapp-group-link-checker/

checker.py

input.txt

output_active.txt

output_expired.txt

README.md

input.txt: Your list of WhatsApp group links (one per line)

checker.py: The main script

output_active.txt: Verified working links

output_expired.txt: Expired or invalid links

🧪 How to Use

Step 1: Add Links
Put all your WhatsApp group invite links in input.txt, like:
https://chat.whatsapp.com/Abc123
https://chat.whatsapp.com/Xyz789

Step 2: Run the Script
python checker.py

Step 3: Get Results

output_active.txt: Links that still work

output_expired.txt: Dead or invalid links

📦 Example Output

[ ✔ ] Available ~ https://chat.whatsapp.com/Abc123
[ ✖ ] Not Found ~ https://chat.whatsapp.com/Xyz789

🔒 License

This project is licensed under the MIT License.
You're free to use, modify, distribute — just keep the credit.

See LICENSE file for more details.

🙋‍♂️ About the Developer

Wajahat Ali Mir
Python Developer | Automation Builder | Real-World Problem Solver
Based in Pakistan – building smart backend tools with purpose.
“Build smart. Break limits. Stay curious.”

**🔗 Connect With Me

GitHub: https://github.com/wajahatalimirpro

Email: mrwajahatalimir@gmail.com

WhatsApp: https://wa.me/923700882006

LinkedIn: https://linkedin.com/in/wajahatalimirpro

Pinterest: https://www.pinterest.com/mrwajahatalimir

If you find this tool useful, give it a star on GitHub. Contributions are welcome!**
