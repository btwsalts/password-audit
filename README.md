# Password Audit

A simple web-based password auditing tool for testing password hashes against a wordlist in an authorized, offline lab environment.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/btwsalts/password-audit.git
cd password-audit
```

### 2. Install the requirements

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
python app.py
```

### 4. Open the web interface

Open:

```
http://127.0.0.1:5000
```

## Using the Tool

1. Enter the hash you want to test.
2. Select the hashing algorithm.
3. Upload a wordlist.
4. Start the audit.
5. The tool reports whether a matching password was found and the number of attempts.

Supported algorithms:

- MD5
- SHA-1
- SHA-256
- SHA-512

## Example Test

Create a file called `wordlist.txt`:

```text
hello
password
Password123
admin
test
```

For example, a SHA-256 hash for `Password123` can be tested against this wordlist.

## Notes

This tool performs local dictionary-based hash comparison. It does **not** perform login attacks against websites or online services.

Use it only with passwords, hashes, and systems you own or are explicitly authorized to test.
