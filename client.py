import socket

# Настройки подключения к серверу
HOST = 'localhost'  # Адрес сервера (если сервер локальный, используем localhost)
PORT = 9090         # Порт, который слушает сервер

# Создаём сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Подключаемся к серверу
    client_socket.connect((HOST, PORT))
    print("Соединение с сервером установлено")

    while True:
        # Читаем строку от пользователя
        message = input("Введите сообщение (или 'exit' для выхода): ")

        if message.lower() == 'exit':
            print("Завершаем соединение с сервером...")
            break

        # Отправляем сообщение серверу
        client_socket.send(message.encode())
        print(f"Отправлено серверу: {message}")

        # Получаем ответ от сервера
        data = client_socket.recv(1024)
        print(f"Ответ от сервера: {data.decode()}")

except ConnectionRefusedError:
    print("Не удалось подключиться к серверу. Проверьте, запущен ли сервер.")

finally:
    # Закрываем соединение
    client_socket.close()
    print("Соединение с сервером закрыто")
