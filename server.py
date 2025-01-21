import socket

# Настройки сервера
HOST = ''  # Пустая строка означает, что сервер будет доступен по всем интерфейсам
PORT = 9090  # Порт для прослушивания

# Создаём сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_socket.bind((HOST, PORT))
print("Сервер запущен и привязан к порту", PORT)

# Ставим сервер в режим прослушивания
server_socket.listen(1)  # 1 — максимальное количество подключений 
print("Сервер начинает прослушивание порта...")

try:
    while True:
        # Принимаем подключение от клиента
        conn, addr = server_socket.accept()
        print(f"Клиент подключился: {addr}")

        # Обрабатываем данные от клиента
        while True:
            data = conn.recv(1024)  # Получаем данные  по 1 КБ
            if not data:
                print(f"Клиент {addr} отключился")
                break

            print(f"Получено от клиента: {data.decode()}")
            conn.send(data)  # Отправляем данные обратно клиенту (эхо)
            print(f"Отправлено клиенту: {data.decode()}")

        # Закрываем соединение с клиентом
        conn.close()

except KeyboardInterrupt:
    print("\nСервер остановлен вручную")

# Закрываем серверный сокет
server_socket.close()
print("Сервер полностью остановлен")
