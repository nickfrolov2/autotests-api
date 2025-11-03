import socket  # Импортируем модуль socket для работы с сетевыми соединениями

messages = []  # Общий список для хранения всех сообщений

def server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен и ждет подключений на localhost:12345")

    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: подключился к серверу")

        try:
            # Получаем данные от клиента
            data = client_socket.recv(4096)
            if not data:
                continue

            message = data.decode('utf-8', errors='replace').strip()
            print(f"Пользователь с адресом: отправил сообщение: {message}")

            # Добавляем сообщение в список всех сообщений
            messages.append(message)

            # Отправляем клиенту всю историю сообщений, каждое сообщение с новой строки
            history = "\n".join(messages)
            client_socket.sendall(history.encode('utf-8'))
        finally:
            # Закрываем соединение с клиентом
            client_socket.close()

if __name__ == '__main__':
    server()