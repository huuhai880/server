import random
from flask import Flask
from flask_socketio import SocketIO, join_room
import time
from threading import Thread, Lock
from datetime import datetime, timedelta
import requests

app = Flask(__name__)
socketio = SocketIO(app)

API_URL = 'http://localhost:9001'

lock = Lock()

@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('join_room')
def handle_join_room(data):
    room = data.get('room')
    if room:
        print(f'Client joining room: {room}')
        join_room(room)

def handleSubmitKetQua(ma_tin, ket_qua):

    data = {
        'ma_tin': ma_tin,
        'ket_qua': str(ket_qua),
        'action': 'luu_kq',
    }

    requests.post("http://localhost:9001/mb/ket_qua/api_luu_ket_qua.php", data=data)
    



def generate_random_array(length, count):

    current_time = datetime.now()

    after_time = current_time + timedelta(seconds=75)

    result_array = []
    for i in range(count):
        if i == 2:  # Nếu là item thứ 3
            # Sinh ngẫu nhiên 10 kí tự số và cách nhau mỗi 5 kí tự
            random_string = "".join(random.choice("0123456789")
                                    for _ in range(10))
            # Chia chuỗi thành các đoạn có 5 kí tự và cách nhau mỗi 5 kí tự
            random_string = ",".join([random_string[j:j+5]
                                     for j in range(0, len(random_string), 5)])
        elif i == 3:  # Nếu là item thứ 4
            # Sinh ngẫu nhiên 30 kí tự số và cách nhau mỗi 5 kí tự
            random_string = "".join(random.choice("0123456789")
                                    for _ in range(30))
            # Chia chuỗi thành các đoạn có 5 kí tự và cách nhau mỗi 5 kí tự
            random_string = ",".join([random_string[j:j+5]
                                     for j in range(0, len(random_string), 5)])
        elif i == 4:  # Nếu là item thứ 5
            # Sinh ngẫu nhiên 12 kí tự số
            random_string = "".join(random.choice("0123456789")
                                    for _ in range(16))
            random_string = ",".join([random_string[j:j+4]
                                     for j in range(0, len(random_string), 4)])
        elif i == 5:  # Nếu là item thứ 6
            # Sinh ngẫu nhiên 12 kí tự số
            random_string = "".join(random.choice("0123456789")
                                    for _ in range(24))
            random_string = ",".join([random_string[j:j+4]
                                     for j in range(0, len(random_string), 4)])

        elif i == 6:  # Nếu là item thứ 7
            # Sinh ngẫu nhiên 12 kí tự số
            random_string = "".join(random.choice("0123456789")
                                    for _ in range(9))
            random_string = ",".join([random_string[j:j+3]
                                     for j in range(0, len(random_string), 3)])

        elif i == 7:  # Nếu là item thứ 8
            # Sinh ngẫu nhiên 12 kí tự số
            random_string = "".join(random.choice("0123456789")
                                    for _ in range(8))
            random_string = ",".join([random_string[j:j+2]
                                     for j in range(0, len(random_string), 2)])

        else:
            # Sinh ngẫu nhiên 5 kí tự số
            random_string = "".join(random.choice("0123456789")
                                    for _ in range(length))

        # Thêm chuỗi vào mảng
        result_array.append(random_string)

    result = {}

    result['number_list'] = result_array

    result['openTime'] = after_time.strftime("%Y-%m-%d %H:%M:%S")

    result['serverTime'] = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print(result)

    handleSubmitKetQua('123', str(result_array))

    return result


def background_task():

    print("chay 1 lan")

    while True:
        with lock:
            result = generate_random_array(length=5, count=8)
            socketio.emit('message_from_server', result, room="room")
        time.sleep(75)
        


if __name__ == '__main__':
    # Start the background task in a separate thread
    background_thread = Thread(target=background_task)
    background_thread.start()
    socketio.run(app, debug=True)
