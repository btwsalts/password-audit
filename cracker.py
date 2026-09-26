import hashlib
from pathlib import Path

SUPPORTED_ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}

def hash_password(password: str, algorithm: str) -> str:
    algorithm = algorithm.lower()
    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    return SUPPORTED_ALGORITHMS[algorithm](password.encode("utf-8")).hexdigest()

def audit_candidates(target_hash: str, candidates, algorithm: str = "sha256") -> dict:
    target_hash = target_hash.strip().lower()
    attempts = 0
    for candidate in candidates:
        password = str(candidate).strip()
        if not password:
            continue
        attempts += 1
        if hash_password(password, algorithm) == target_hash:
            return {"found": True, "password": password, "attempts": attempts}
    return {"found": False, "password": None, "attempts": attempts}

def audit_hash(target_hash: str, wordlist: str, algorithm: str = "sha256") -> dict:
    path = Path(wordlist)
    if not path.is_file():
        raise FileNotFoundError(f"Wordlist not found: {wordlist}")
    return audit_candidates(
        target_hash,
        path.read_text(encoding="utf-8", errors="ignore").splitlines(),
        algorithm,
    )
