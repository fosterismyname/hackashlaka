import cv2
import pyzbar.pyzbar as pyzbar
import rospy
from std_msgs.msg import String

# Функция для распознавания QR-кодов в изображении
def decode_qr(frame):
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        return obj.data.decode("utf-8")
    return None

# Основная функция
def main():
    # Инициализация ROS-ноды
    rospy.init_node('qr_code_publisher', anonymous=True)
    # Создание ROS-паблишера для топика /qr_text
    qr_publisher = rospy.Publisher('/qr_text', String, queue_size=10)
    
    # Подключение к камере
    cap = cv2.VideoCapture(0)

    rate = rospy.Rate(10)  # Частота публикации 10 Гц
    
    while not rospy.is_shutdown():
        # Чтение кадра с камеры
        ret, frame = cap.read()
        if not ret:
            break

        # Распознавание QR-кодов
        qr_text = decode_qr(frame)
        if qr_text:
            rospy.loginfo(f"Распознанный текст: {qr_text}")
            # Публикация распознанного текста в топик /qr_text
            qr_publisher.publish(qr_text)

        # Отображение кадра с камеры
        cv2.imshow('QR Code Scanner', frame)

        # Ожидание нажатия клавиши "q" для выхода
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        rate.sleep()

    # Освобождение ресурсов
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
