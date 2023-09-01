
import rclpy
from turtlesim.msg import Pose
from rclpy.node import Node


class PoseSub(Node):
    
    def __init__(self):
        super().__init__("pose")
        self.pose =self.create_subscription(Pose,"/turtle1/pose",self.callback,10)

    def callback(self,msg: Pose):
        self.get_logger().info(str(msg))
def main(args=None):
    rclpy.init(args=args)
    node = PoseSub()
    rclpy.spin(node)
    rclpy.shutdown()