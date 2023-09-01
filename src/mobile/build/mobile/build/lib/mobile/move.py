import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge




class sensor(Node):
    
    def __init__(self):
        super().__init__("move")
        
        self.sub_name =self.create_subscription(Image,'/camera/image_raw',self.camera_cb,10)
        self.out =cv2.VideoWriter('/Home/Videos/output1.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,(640,80))

        self.bridge = CvBridge()
    def camera_cb(self,data):
        self.get_logger().info('Receiving video frame')
        frame= self.bridge.imgmsg_to_cv2(data)
        edge= cv2.Canny(frame,100,200)
        self.out.write(edge)
        cv2.imshow('frame', edge)
        cv2.waitKey(1)    
def main(args=None):
    rclpy.init(args=args)
    move = sensor()
    rclpy.spin(move)
    rclpy.shutdown()
 