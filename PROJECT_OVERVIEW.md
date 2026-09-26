# Project Overview

## Purpose

Password Audit is a small cybersecurity learning project for understanding how dictionary-based password auditing works against offline password hashes.

## Workflow

1. Supply a test hash and hashing algorithm.
2. Read candidate passwords from a local wordlist.
3. Hash each candidate using the selected algorithm.
4. Compare the generated digest with the target hash.
5. Report whether a match was found and how many candidates were tested.

## Scope

The project is intentionally limited to offline hash comparison. It does not attempt to authenticate to websites, services, or user accounts.
