document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const messageEl = document.getElementById("message");

  try {
    const response = await fetch("/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (data.success) {
      messageEl.style.color = "green";
      messageEl.textContent = "✅ Login bem-sucedido!";
      setTimeout(() => {
        window.location.href = "segunda.html"; // redireciona para página principal
      }, 1000);
    } else {
      messageEl.style.color = "red";
      messageEl.textContent = "❌ " + data.message;
    }
  } catch (err) {
    messageEl.style.color = "red";
    messageEl.textContent = "Erro ao conectar com o servidor.";
  }
});
