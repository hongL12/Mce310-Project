#!/usr/bin/env python

import math
import rospy
from geometry_msgs.msg import Twist

def log_velocity(linear, angular):
    rospy.loginfo(f"Linear Velocity: {linear}, Angular Velocity: {angular}")


def turtle_circle(radius=2.0):
    pub = rospy.Publisher( Twist, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = radius
        vel.angular.z = 1
        log_velocity([radius, 0, 0], [0, 0, 1])
        pub.publish(vel)
        rate.sleep()

def turtle_trapezoid():
    rospy.init_node(anonymous=True)
    pub = rospy.Publisher( Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    side_length_top = 3
    side_length_bottom = 5
    angle = math.atan(2)
    while not rospy.is_shutdown():
        vel.linear.x = side_length_top
        vel.angular.z = math.atan(2)
        pub.publish(vel)
        rate.sleep()
        vel.linear.x = 0
        vel.angular.z = 0
        pub.publish(vel)
        rate.sleep()
        vel.linear.x = side_length_bottom
        vel.angular.z = math.pi - math.atan(2)
        pub.publish(vel)
        rate.sleep()
        vel.linear.x = 0
        vel.angular.z = 0
        pub.publish(vel)
        rate.sleep()
        angle += math.pi / 3
        if angle >= 2 * math.pi:
            break

def turtle_square(side_length):
    rospy.init_node( anonymous=True)
    pub = rospy.Publisher(Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    angle = 0
    while not rospy.is_shutdown():
        vel.linear.x = side_length
        vel.angular.z = math.pi / 2
        rospy.loginfo( side_length)
        pub.publish(vel)
        rate.sleep()
        vel.linear.x = 0
        vel.angular.z = 0
        pub.publish(vel)
        rate.sleep()
        angle += math.pi / 2
        if angle >= 2 * math.pi:
            break

def turtle_hexagon():
    rospy.init_node( anonymous=True)
    pub = rospy.Publisher( Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    angle = 0
    side_length = 2 * math.sin(math.pi / 3)
    while not rospy.is_shutdown():
        vel.linear.x = side_length
        vel.angular.z = math.pi / 3
        pub.publish(vel)
        rate.sleep()
        vel.linear.x = 0
        vel.angular.z = 0
        pub.publish(vel)
        rate.sleep()
        angle += math.pi / 3
        if angle >= 2 * math.pi:
            break

if __name__ == '__main__':
    rospy.init_node(anonymous=True)

    shape = input("Enter a shape (hexagon,trapezoid,square, circle): ")

    if shape == 'circle':
        turtle_circle()

    elif shape == 'square':
        turtle_square()
    elif shape == "hexagon":
       turtle_hexagon()

    elif shape == "trapezoid":
        turtle_trapezoid()
    else:
        print("Invalid shape entered.")
