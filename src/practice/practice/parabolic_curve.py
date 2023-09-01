import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class ParabolicCurveNode(Node):
    def __init__(self):
        super().__init__('parabolic_curve_node')
        self.turtle_pose_sub = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10
        )
        self.turtle_pose_sub  # prevent unused variable warning
        self.turtle_cmd_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.turtle_cmd = Twist()
        self.a = 0.5  # Parabolic curve parameter

    def pose_callback(self, msg):
        x = msg.x
        y = msg.y
        theta = msg.theta

        # Calculate the parabolic curve motion
        v = self.a * x
        w = self.a

        # Adjust the linear and angular speed to follow the parabolic curve
        self.turtle_cmd.linear.x = v
        self.turtle_cmd.angular.z = w

        self.turtle_cmd_pub.publish(self.turtle_cmd)


def main(args=None):
    rclpy.init(args=args)

    node = ParabolicCurveNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()