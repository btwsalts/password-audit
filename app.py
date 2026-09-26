from flask import Flask, jsonify, request, send_from_directory
from cracker import audit_candidates, SUPPORTED_ALGORITHMS
import time

app = Flask(__name__, static_folder="frontend", static_url_path="")

@app.get("/")
def index():
    return send_from_directory("frontend", "index.html")

@app.post("/api/audit")
def audit():
    target_hash = str(request.form.get("hash", "")).strip()
    algorithm = str(request.form.get("algorithm", "sha256")).lower()
    wordlist = request.files.get("wordlist")

    if not target_hash:
        return jsonify({"error": "Enter a target hash."}), 400
    if algorithm not in SUPPORTED_ALGORITHMS:
        return jsonify({"error": "Unsupported hashing algorithm."}), 400
    if wordlist is None:
        return jsonify({"error": "Upload a wordlist."}), 400

    try:
        content = wordlist.read().decode("utf-8", errors="ignore")
    except Exception:
        return jsonify({"error": "Could not read the wordlist."}), 400

    candidates = content.splitlines()
    started = time.perf_counter()

    try:
        result = audit_candidates(target_hash, candidates, algorithm)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    elapsed = round(time.perf_counter() - started, 4)
    return jsonify({
        "found": result["found"],
        "password": result["password"],
        "attempts": result["attempts"],
        "elapsed": elapsed,
        "algorithm": algorithm.upper(),
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
