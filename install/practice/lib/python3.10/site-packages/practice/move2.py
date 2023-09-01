import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import transforms3d
from transforms3d.euler import euler2quat
from geometry_msgs.msg import Quaternion,Point,Twist

import sys
import math
x=0.0
y=0.0
theta= 0.0
class Turtle_GTG2(Node):
    def __init__(self):
        super().__init__("Go_to_Goal_Node")
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.pose_sub = self.create_subscription(Odometry, '/odom', self.pose_callback, 10)
        self.timer = self.create_timer(0.1, self.goto)
        self.pose = Odometry()

    def pose_callback(self, msg):
        global x
        global y
        global theta
        x= msg.pose.pose.position.x
        y= msg.pose.pose.position.y

        rot_q=msg.pose.pose.orientation
        #{roll,pitch,theta} = euler_from_quarternion{[rot_q.x, rot_q.y.rot_z,rot_w]}
        roll, pitch, theta = self.quaternion_to_euler(rot_q)
    def quaternion_to_euler(self, quaternion):
        quat = [quaternion.x, quaternion.y, quaternion.z, quaternion.w]
        euler = transforms3d.euler.quat2euler(quat, 'rzyx')
        roll, pitch, theta = euler[0], euler[1], euler[2]
        return roll, pitch, theta
    

    def goto(self):
        goal = Point()
        goal.x = 5.0
        goal.y = 5.0
        #goal.theta = float(sys.argv[3])

        new_vel = Twist()
        
        # Ecludian Distance
        distance_to_goal = math.sqrt( (goal.x -x)**2  + (goal.y -y)**2 )
        # Angle to Goal
        angle_to_goal =math.atan2(goal.y -y , goal.x -x)

        distance_tolerance = 0.1
        #angle_tolerance = 0.01

        angle_error = angle_to_goal -theta
        kp = 10

        if abs(angle_error) > 0.1:
            #new_vel.angular.z = kp * angle_error
           new_vel.angular.z=0.1
        


        else :
            if( distance_to_goal ) >= distance_tolerance:
                new_vel.linear.x = kp * distance_to_goal
                new_vel.angular.z=0.0
            else :
                new_vel.linear.x= 0.0
                new_vel.angular.z=0.0
                self.get_logger().info("Goal Reached ")
                quit()
        self.cmd_vel_pub.publish(new_vel)        





def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = Turtle_GTG2()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()
