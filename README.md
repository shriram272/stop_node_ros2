# stop_node_ros2


[Screencast from 09-04-2023 09:48:08 PM.webm](https://github.com/shriram272/stop_node_ros2/assets/99411053/adaa8182-a4fb-45eb-82a9-8f1f6aa61db4)



INSTRUCTIONS
1.The navigation package is used for making a single launch file for launching rviz and gazebo and used for testing the navigation parameters like costmap etc.
ros2 launch navigation navigation.py   --- This command launches turtlebot3 in gazebo and rviz

2> The my_stop_bot package contains the node for stpping the turtlebot once its run.
ros2 run my_stop_bot stop_bot --- activates the node which stops the bot annd node is killed.
