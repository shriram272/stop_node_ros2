
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="screen" ,
            arguments=["1", "0", "0", "0", "0", "0", "odom", "laser", ]
        )
    ])