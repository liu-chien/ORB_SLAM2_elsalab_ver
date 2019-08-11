#!/usr/bin/env python
import rospy
import roslib
from geometry_msgs.msg import Twist, Vector3

def create_twist(x, y, z):
    pub_twist = Twist()

    pub_twist.linear.x = 0.0
    pub_twist.linear.y = 0.0
    pub_twist.linear.z = 0.0

    pub_twist.angular.x= x
    pub_twist.angular.y= y
    pub_twist.angular.z= z


    return pub_twist


def fake_cmd_vel_publish():
    rospy.init_node('fake_cmd_vel')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
    print('ros node started')
    while True:
        g = input('anular: ')
        try:
            if g == 'w':
                pose = create_twist(0, 0, 0)
                pub.publish(pose)
                sleep(0.1)
            elif g == 's':
                pose = create_twist(0, 0, 0)
                pub.publish(pose)
                sleep(0.1)
            elif g == 'd':
                print('right')
                pose = create_twist(0, 0, -1)
                pub.publish(pose)
                sleep(0.1)
            elif g == 'a':
                print('left')
                pose = create_twist(0, 0, 1)
                pub.publish(pose)
                sleep(0.1)
            elif keyboard.is_pressed('esc'):
                print('finished')
                break
        except:
            print('keyboard error')
            break





if __name__ == '__main__':
    try:
        print('start fake /cmd_vel publisher')
        fake_cmd_vel_publish()

    except rospy.ROSInterruptException:
        print('ROS error')
        pass