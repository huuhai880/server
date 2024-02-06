import random
from flask import Flask
from flask_socketio import SocketIO, join_room
from threading import Thread, Lock
from datetime import datetime, timedelta
import asyncio
import redis
import mysql.connector
import httpx
import requests






app = Flask(__name__)
socketio = SocketIO(app)

# Configuration
API_URL = 'http://159.65.129.60:9001'
ROOM_NAME = "room"


lock = Lock()

r = redis.Redis(host='159.65.129.60', port=6379, db=0, password='SUPER_SECRET_PASSWORD')


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


async def handle_submit_result(ma_tin, ket_qua, openTime, NewNumberClass):
    try:

        data = {
            'ma_tin': ma_tin,
            'ket_qua': str(ket_qua),
            'openTime': str(openTime),
            'action': 'luu_kq',
            'ma_phien_toi': NewNumberClass
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f"{API_URL}/mb/ket_qua/api_luu_ket_qua.php", data=data)
                response.raise_for_status()  # Raise an error for bad responses
                print("Request successful!")
                # Do something with the response, if needed
            except httpx.HTTPStatusError as errh:
                print(f"HTTP Error: {errh}")
            except Exception as err:
                print(f"An error occurred: {err}")

    except requests.RequestException as e:
        print(f"Error submitting result: {e}")


async def generate_random_array(length, count):

    mydb = mysql.connector.connect(
            host="159.65.129.60",
            user="root",
            password="4Jmnidyl@bot",
            database="dp_app"
    )
    
    list_without_parentheses =[]
    #Lấy danh sách số xuất hiện nhiều nhất
    mycursor = mydb.cursor()

    mycursor.execute("CALL ten_proc()")

    myresult = mycursor.fetchall()

    list_without_parentheses = [item[0] for item in myresult]
   
    list_without_parentheses = set(list(list_without_parentheses))

    print(list_without_parentheses)


    current_time = datetime.now()
    after_time = current_time + timedelta(seconds=75)

    result_array = []

    array_check = []

    CurrentNumberClass = r.get("NewNumberClass")
    
    CurrentNumberClass = CurrentNumberClass.decode('utf-8')
    #Tạo mã phiên mới
    formatted_time = int(after_time.strftime("%Y%m%d")) + int(after_time.strftime("%H%M%S"))
    # digit_sum = sum(int(digit) for digit in formatted_time)

    NewNumberClass = formatted_time
    
    

    for i in range(count):
        if i == 2:  # Nếu là item thứ 3

            while True:
                # Sinh ngẫu nhiên 10 kí tự số và cách nhau mỗi 5 kí tự
                random_string = "".join(random.choice("0123456789") for _ in range(10))
                # Chia chuỗi thành các đoạn có 5 kí tự và cách nhau mỗi 5 kí tự
                random_string = ",".join([random_string[j:j+5] for j in range(0, len(random_string), 5)])
                _random_string = random_string.split(',')

                if all(elem not in _random_string for elem in array_check) and  all(elem[-2:] not in list_without_parentheses for elem in _random_string):
                    array_check.append(random_string)
                    break
            
        
        elif i == 3:  # Nếu là item thứ 4

            while True:
                # Sinh ngẫu nhiên 30 kí tự số và cách nhau mỗi 5 kí tự
                random_string = "".join(random.choice("0123456789")
                                        for _ in range(30))
                # Chia chuỗi thành các đoạn có 5 kí tự và cách nhau mỗi 5 kí tự
                random_string = ",".join([random_string[j:j+5]
                                        for j in range(0, len(random_string), 5)])
                _random_string = random_string.split(',')
                if all(elem not in _random_string for elem in array_check) and  all(elem[-2:] not in list_without_parentheses for elem in _random_string):
                    array_check.append(random_string)
                    break
            
        elif i == 4:  # Nếu là item thứ 5
            while True:
                # Sinh ngẫu nhiên 12 kí tự số
                random_string = "".join(random.choice("0123456789")
                                        for _ in range(16))
                random_string = ",".join([random_string[j:j+4]
                                        for j in range(0, len(random_string), 4)])
                _random_string = random_string.split(',')
                if all(elem not in _random_string for elem in array_check) and  all(elem[-2:] not in list_without_parentheses for elem in _random_string):
                    array_check.append(random_string)
                    break
            
        elif i == 5:  # Nếu là item thứ 6
            while True:
                # Sinh ngẫu nhiên 12 kí tự số
                random_string = "".join(random.choice("0123456789")
                                        for _ in range(24))
                random_string = ",".join([random_string[j:j+4]
                                        for j in range(0, len(random_string), 4)])
                _random_string = random_string.split(',')
                if all(elem not in _random_string for elem in array_check) and  all(elem[-2:] not in list_without_parentheses for elem in _random_string):
                    array_check.append(random_string)
                    break
            

        elif i == 6:  # Nếu là item thứ 7

            while True:
                # Sinh ngẫu nhiên 12 kí tự số
                random_string = "".join(random.choice("0123456789")
                                        for _ in range(9))
                random_string = ",".join([random_string[j:j+3]
                                        for j in range(0, len(random_string), 3)])
                _random_string = random_string.split(',')
                if all(elem not in _random_string for elem in array_check) and  all(elem[-2:] not in list_without_parentheses for elem in _random_string):
                    array_check.append(random_string)
                    break
            

        elif i == 7:  # Nếu là item thứ 8
            while True:
               # Sinh ngẫu nhiên 12 kí tự số
                random_string = "".join(random.choice("0123456789")
                                        for _ in range(8))
                random_string = ",".join([random_string[j:j+2]
                                        for j in range(0, len(random_string), 2)])
                _random_string = random_string.split(',')
                if all(elem not in _random_string for elem in array_check) and  all(elem[-2:] not in list_without_parentheses for elem in _random_string):
                    array_check.append(random_string)
                    break
            

        else:
            # Sinh ngẫu nhiên 5 kí tự số
            while True:
                random_string = "".join(random.choice("0123456789") for _ in range(length))
                if random_string not in array_check and  random_string[-2:] not in list_without_parentheses:
                    array_check.append(random_string)
                    break

        result_array.append(random_string)

    result = {
        'number_list': result_array,
        'openTime': after_time.strftime("%Y-%m-%d %H:%M:%S"),
        'serverTime': current_time.strftime("%Y-%m-%d %H:%M:%S")
    }

    # Move the print statement outside the loop
    print(result)

    # Lưu kết quả

    await handle_submit_result(CurrentNumberClass, str(result_array), after_time.strftime("%Y-%m-%d %H:%M:%S"), NewNumberClass)

    # kiểm tra kết quả

    r.set("NewNumberClass", NewNumberClass)

    return result


async def background_task():
    print("Running background task")

    while True:
        with lock:
            result = await generate_random_array(length=5, count=8)
            socketio.emit('message_from_server', result, room=ROOM_NAME)
        await asyncio.sleep(75)


def run_background_task():
    asyncio.run(background_task())


if __name__ == '__main__':
    # Start the background task in a separate thread
    background_thread = Thread(target=run_background_task)
    background_thread.start()

    socketio.run(app,host='0.0.0.0', debug=False, allow_unsafe_werkzeug=True)
