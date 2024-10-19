# Создание ROS пакета на Python, содержащего ноду-публикатор и ноду-подписчик

# 1. Создайте новый ROS пакет
# В терминале, в рабочей директории catkin_workspace выполните команду:
# catkin_create_pkg test_package rospy std_msgs

# 2. Перейдите в директорию test_package и создайте Python скрипты для нод

# Нода-публикатор: publisher_node.py
import rospy
from std_msgs.msg import Int32

def publisher():
    rospy.init_node('test_publisher', anonymous=True)
    pub = rospy.Publisher('/test', Int32, queue_size=10)
    rate = rospy.Rate(10)  # Частота публикации 10 Гц
    count = 0
    
    while not rospy.is_shutdown():
        rospy.loginfo(f"Публикуется значение: {count}")
        pub.publish(count)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

# Нода-подписчик: subscriber_node.py
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(f"Получено значение: {data.data}")

def subscriber():
    rospy.init_node('test_subscriber', anonymous=True)
    rospy.Subscriber('/test', Int32, callback)
    rospy.spin()  # Ожидание сообщений

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass

# 3. Добавьте файлы в CMakeLists.txt
# В CMakeLists.txt пакета test_package добавьте следующие строки, чтобы сделать скрипты исполняемыми:
#
# catkin_install_python(PROGRAMS scripts/publisher_node.py scripts/subscriber_node.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

# 4. Запуск нод
# В терминале выполните команды:
# roscore
# rosrun test_package publisher_node.py
# rosrun test_package subscriber_node.py
