# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# import sys


# class vel(Node):
#     def __init__(self):
#         super().__init__("circ")
#         self.cmd_vel2 = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
#         self.timer=self.create_timer(0.5,self.velocity2)
        
    
#     def velocity2(self):
#         msg=Twist()
#         linear_vel=float(sys.argv[1])
#         radius=float(sys.argv[2])
#         msg.linear.x=linear_vel
#         msg.linear.y= 0.0
#         msg.angular.z=linear_vel/radius
#         self.cmd_vel2.publish(msg)
# def main(args=None):
#     rclpy.init(args=args)
    
#     node = vel()
#     rclpy.spin(node)
#     rclpy.shutdown()





import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TurtlebotParabolicNode(Node):
    def __init__(self):
        super().__init__('turtlebot_parabolic_node')
        self.turtle_cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.turtle_cmd = Twist()
        self.linear_speed = 0.2  # Adjust the linear speed as needed

    def move_parabolic(self):
        num_steps = 100
        loop_rate = self.create_rate(10)  # Create a loop rate of 10 Hz (adjust as needed)
        for i in range(num_steps):
            t = i / (num_steps - 1.0)  # Time parameter from 0 to 1
            x = (t - 0.5) * 2.0  # Adjust scaling for the width of the parabola
            y = 0.5 * x**2
            angle = math.atan2(y, x)  # Calculate the angle to move along the parabola
            self.turtle_cmd.linear.x = self.linear_speed
            self.turtle_cmd.angular.z = self.linear_speed * math.tan(angle)  # Adjust scaling for angular velocity
            self.turtle_cmd_pub.publish(self.turtle_cmd)
            loop_rate.sleep()

        # Stop the Turtlebot after completing the parabolic path
        self.turtle_cmd.linear.x = 0.0
        self.turtle_cmd.angular.z = 0.0
        self.turtle_cmd_pub.publish(self.turtle_cmd)

def main(args=None):
    rclpy.init(args=args)

    node = TurtlebotParabolicNode()

    try:
        # Move in the parabolic path
        node.move_parabolic()
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
