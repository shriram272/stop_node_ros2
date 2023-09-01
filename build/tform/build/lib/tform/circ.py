
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="tform",
            executable="circ",
            output="screen" ,
            arguments=["0", "0", "0", "0", "0", "0", "odom", "laser"]
        )
    ])