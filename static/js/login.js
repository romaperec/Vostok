document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('loginForm');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const email = document.getElementById('loginEmail').value.trim();
        const password = document.getElementById('loginPassword').value.trim();

        if (!email || !password) {
            alert('Все поля обязательны для заполнения');
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'Ошибка входа');
            }

            alert('Вход выполнен успешно!');
            setTimeout(() => {
                window.location.href = '/account';
            }, 1500);

        } catch (error) {
            alert('Ошибка:', error);
        }
    });

});