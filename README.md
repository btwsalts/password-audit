# 🔐 Password Audit

A simple web-based password auditing tool for testing password hashes against a wordlist in an authorized, offline lab environment.

## Run Locally

```bash
git clone https://github.com/btwsalts/password-audit.git
cd password-audit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

## Using the Tool

1. Open the local address shown by the application.
2. Enter the hash you want to test.
3. Select the hashing algorithm.
4. Upload or provide a wordlist.
5. Start the audit.

Example wordlist:

```text
hello
password
Password123
admin
test
```

## Notes

This tool performs local dictionary-based hash comparison for educational and authorized testing.

Use it only with passwords, hashes, and systems you own or are explicitly authorized to test.
