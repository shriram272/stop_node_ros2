import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped
import math
import csv
import matplotlib

class TurtlebotTraceNode(Node):
    def __init__(self):
        super().__init__('turtlebot_trace_node')
        self.turtle_cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.turtle_cmd = Twist()
        self.linear_speed = 0.2  # Adjust the linear speed as needed

        # Create a subscriber for odometry
        self.turtle_odom_sub = self.create_subscription(
            PoseStamped,
            'odom',  # Replace 'odom' with the actual odometry topic used in your setup
            self.odom_callback,
            10
        )
        self.turtle_odom_sub

        # Initialize the path as an empty list to store poses
        self.path = []

    def move_parabolic(self):
        num_steps = 10
        loop_rate = self.create_rate(10)  # Create a loop rate of 10 Hz

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

    def odom_callback(self, msg):
        # Store the pose information received from odometry
        self.path.append(msg.pose)

    def save_path_to_file(self, file_name='turtlebot_path.csv'):
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for pose in self.path:
                x = pose.position.x
                y = pose.position.y
                writer.writerow([x, y])

def main(args=None):
    rclpy.init(args=args)
    node = TurtlebotTraceNode()

    try:
        # Move in the parabolic path
        node.move_parabolic()

        # Save the path to a CSV file
        node.save_path_to_file()

        # Plot the path (optional, requires matplotlib)
        node.plot_path()

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
