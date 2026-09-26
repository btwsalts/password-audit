const hashInput = document.getElementById("hash");
const algorithm = document.getElementById("algorithm");
const wordlist = document.getElementById("wordlist");
const button = document.getElementById("auditButton");
const result = document.getElementById("result");
const status = document.getElementById("status");
const attempts = document.getElementById("attempts");
const elapsed = document.getElementById("elapsed");
const usedAlgorithm = document.getElementById("usedAlgorithm");
const passwordBox = document.getElementById("passwordBox");
const password = document.getElementById("password");
const error = document.getElementById("error");

button.addEventListener("click", async () => {
  result.classList.remove("hidden");
  passwordBox.classList.add("hidden");
  error.textContent = "";
  status.textContent = "RUNNING";
  button.disabled = true;

  if (!hashInput.value.trim() || !wordlist.files.length) {
    error.textContent = "Enter a hash and choose a wordlist.";
    status.textContent = "INPUT ERROR";
    button.disabled = false;
    return;
  }

  const form = new FormData();
  form.append("hash", hashInput.value.trim());
  form.append("algorithm", algorithm.value);
  form.append("wordlist", wordlist.files[0]);

  try {
    const response = await fetch("/api/audit", { method: "POST", body: form });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Audit failed.");

    attempts.textContent = data.attempts.toLocaleString();
    elapsed.textContent = data.elapsed + "s";
    usedAlgorithm.textContent = data.algorithm;
    status.textContent = data.found ? "MATCH FOUND" : "NO MATCH";

    if (data.found) {
      password.textContent = data.password;
      passwordBox.classList.remove("hidden");
    }
  } catch (err) {
    status.textContent = "ERROR";
    error.textContent = err.message;
  } finally {
    button.disabled = false;
  }
});
