import serial
import time

# Настройка порта (замените 'COM3' на ваш порт)
port = 'COM7'  # Для Windows
# port = '/dev/ttyUSB0'  # Для Linux/Mac
baudrate = 115200  # Должно совпадать с настройкой STM32

try:
    ser = serial.Serial(port, baudrate, timeout=1)
    print(f"Подключено к {port} на скорости {baudrate} бод")

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(
                data)
        time.sleep(0.1)

except serial.SerialException as e:
    print("Ошибка подключения:", e)
except KeyboardInterrupt:
    print("Программа остановлена")
    ser.close()
