document.addEventListener('DOMContentLoaded', () => {
    const toggleButtons = document.querySelectorAll('.toggle-submenu');

    toggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            const submenu = button.nextElementSibling;
            if (submenu.style.display === 'block') {
                submenu.style.display = 'none'; // Скрыть вложенные списки
                button.textContent = '+'; // Изменить маркер на +
            } else {
                submenu.style.display = 'block'; // Показать вложенные списки
                button.textContent = '-'; // Изменить маркер на -
            }
        });
    });
});
