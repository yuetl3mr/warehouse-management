document.addEventListener('DOMContentLoaded', function () {
    const alertMessage = document.createElement('div');
    alertMessage.textContent = 'Chào mừng bạn đã đăng nhập thành công!';
    alertMessage.style.position = 'fixed';
    alertMessage.style.top = '10px';
    alertMessage.style.right = '10px';
    alertMessage.style.backgroundColor = '#1abc9c';
    alertMessage.style.color = '#ffffff';
    alertMessage.style.padding = '10px';
    alertMessage.style.borderRadius = '5px';
    alertMessage.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';

    document.body.appendChild(alertMessage);

    setTimeout(() => {
        alertMessage.remove();
    }, 3000);
});
