document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registerForm');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // 1. Собираем данные
        const formData = {
            name: document.getElementById('name').value.trim(),
            email: document.getElementById('email').value.trim(),
            password: document.getElementById('password').value.trim()
        };

        console.log("Отправляемые данные:", formData);

        try {
            // 2. Отправляем на сервер
            const response = await fetch('http://127.0.0.1:8000/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            console.log("Статус ответа:", response.status);

            // 3. Обрабатываем ответ
            if (!response.ok) {
                const errorData = await response.json();
                console.error("Ошибка сервера:", errorData);
                alert(`Ошибка: ${JSON.stringify(errorData)}`);
                return;
            }

            const result = await response.json();
            console.log("Успешный ответ:", result);
            alert("Регистрация успешна!");
            
        } catch (error) {
            console.error("Ошибка при отправке:", error);
            alert("Произошла ошибка соединения");
        }
    });
});