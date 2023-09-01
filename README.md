# stop_node_ros2

https://github.com/shriram272/stop_node_ros2/assets/99411053/ce52a3f9-3ab4-4f60-910d-0641cf92bc3c




INSTRUCTIONS
1.The navigation package is used for making a single launch file for launching rviz and gazebo and used for testing the navigation parameters like costmap etc.
ros2 launch navigation navigation.py   --- This command launches turtlebot3 in gazebo and rviz

2> The my_stop_bot package contains the node for stpping the turtlebot once its run.
ros2 run my_stop_bot stop_bot --- activates the node which stops the bot annd node is killed.
