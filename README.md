# 🔐 Password Audit

### Web-Based Hash Auditing · Dictionary Testing · Security Learning

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Security](https://img.shields.io/badge/Use-Authorized%20Testing-111111)](#security-note)

> A simple web-based password auditing tool for testing password hashes against a wordlist in an authorized, offline lab environment.

---

## ✦ What is Password Audit?

Password Audit is a lightweight web application that demonstrates how dictionary-based password auditing works.

Instead of testing credentials against an online service, the application works locally by comparing candidate words from a wordlist against a supplied password hash.

It is designed for:

- Cybersecurity learning
- Password-hash demonstrations
- Offline security labs
- CTF-style practice
- Authorized password auditing

---

## 🧩 Features

- 🌐 Web-based interface
- 🔐 Hash comparison
- 📄 Wordlist-based auditing
- 🧪 Offline dictionary testing
- ⚙️ Multiple hashing algorithms
- 📊 Attempt/result reporting
- 🐍 Python-based backend
- 💻 Runs locally
- 🎓 Designed for educational and authorized testing

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **Flask** | Web application/backend |
| **HTML5** | Interface structure |
| **CSS3** | Styling and responsive layout |
| **JavaScript** | Frontend interactions |
| **Hashing libraries** | Hash generation and comparison |
| **Wordlists** | Candidate password input |

---

## 📁 Project Structure

```text
password-audit/
├── app.py
├── requirements.txt
├── templates/
├── static/
└── README.md
```

> The exact file structure may change as the project develops.

---

## 🚀 Run Locally

Clone the repository, create a virtual environment, install the dependencies, and start the application:

```bash
git clone https://github.com/btwsalts/password-audit.git
cd password-audit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

After starting the application, open the local address shown by the Flask application in your browser.

---

## 🧠 How It Works

The basic workflow is:

```text
Hash Input
    │
    ▼
Select Algorithm
    │
    ▼
Load Wordlist
    │
    ▼
Read Candidate
    │
    ▼
Generate Hash
    │
    ▼
Compare With Target Hash
    │
    ├── Match → Password Found
    │
    └── No Match → Continue
```

The process continues until a matching candidate is found or the wordlist has been exhausted.

---

## 🔎 Supported Hash Algorithms

The current implementation supports:

- MD5
- SHA-1
- SHA-256
- SHA-512

---

## 🧪 Example Wordlist

Create a file such as `wordlist.txt`:

```text
hello
password
Password123
admin
test
```

The application can then compare each candidate against the supplied hash.

---

## 📌 Example Workflow

1. Start the application locally.
2. Open the web interface.
3. Enter a hash generated from a test password.
4. Select the correct hashing algorithm.
5. Provide a wordlist.
6. Start the audit.
7. Review the result and number of attempts.

For testing, use passwords and hashes that you generated yourself.

---

## 🔐 Security Note

This project performs **local dictionary-based hash comparison**.

It does **not** perform:

- Online login attacks
- Credential stuffing
- Remote brute-force attacks
- Attempts against third-party accounts

Only use the project with passwords, hashes, wordlists, and systems you own or are explicitly authorized to test.

---

## ⚠️ Limitations

- Only candidates present in the supplied wordlist can be discovered.
- A password will not be found if the correct candidate is missing from the wordlist.
- Hashing algorithms such as MD5 and SHA-1 are not recommended for storing passwords in modern applications.
- Performance depends on the size of the wordlist and the selected algorithm.
- This project is intended as an educational auditing tool, not a production password-cracking platform.

---

## 🧠 What I Practiced

This project demonstrates practical experience with:

- Python application development
- Flask web development
- Hashing concepts
- File handling
- Wordlist processing
- Form handling
- Backend/frontend communication
- Input validation
- Security-focused application design
- Building a usable security tool instead of only a command-line script

---

## 🔭 Future Improvements

Potential improvements include:

- [ ] Additional hashing algorithms
- [ ] Custom wordlist management
- [ ] Progress indicators
- [ ] Improved result reporting
- [ ] Hash-format detection
- [ ] Larger-file streaming
- [ ] Performance improvements
- [ ] Password-audit statistics
- [ ] Better error handling
- [ ] Automated testing
- [ ] Docker support

---

## 💼 Portfolio Value

Password Audit is a practical example of combining **software engineering and cybersecurity**.

The project demonstrates how a security concept can be turned into a usable web application with a frontend, backend logic, file processing, and hash comparison.

It also provides a foundation for experimenting with:

**Web UI → Backend Logic → Wordlist Processing → Hashing → Result Reporting**

---

## 👤 Author

Built by **btwsalts** as a cybersecurity and software-engineering project.
