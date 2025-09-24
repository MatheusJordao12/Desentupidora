document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        if(response.ok) {
            message.style.color = 'green';
            message.textContent = data.message;

            setTimeout(() => {
                window.location.href = "segunda.html"
            }, 200);
        } else {
            message.style.color = 'red';
            message.textContent = data.message;
        }
    } catch (error) {
        message.style.color = 'red';
        message.textContent = 'Erro ao se conectar ao servidor'
    }
});

