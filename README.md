# Password Audit

An educational offline password-auditing lab that demonstrates dictionary-based password recovery from test hashes.

## Features

- MD5, SHA-1, SHA-256, and SHA-512 support
- Local wordlist-based hash comparison
- Attempt counting
- Simple Python implementation suitable for security learning
- Designed for controlled, authorized test data

## Usage

Create a test wordlist, then use the core function from Python:

```python
from cracker import audit_hash

result = audit_hash("YOUR_TEST_HASH", "wordlist.txt", "sha256")
print(result)
```

## Safety

Use this project only with passwords, hashes, and systems you own or are explicitly authorized to test. It is intentionally designed as an offline educational lab and does not perform login attacks against online services.
