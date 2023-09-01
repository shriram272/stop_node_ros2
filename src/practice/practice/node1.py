import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class vel(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer=self.create_timer(0.5,self.velocity)
        self.get_logger().info("draw circle")
    
    def velocity(self):
        msg=Twist()
        msg.linear.x=2.0
        msg.angular.z=1.0
        self.cmd_vel.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = vel()
    rclpy.spin(node)
    rclpy.shutdown()


