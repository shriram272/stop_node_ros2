#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "nav2_msgs/action/navigate_to_pose.hpp"

class StopBot : public rclcpp::Node
{
public:
    StopBot() : Node("stop_bot_node")
    {
        this->action_client_ = rclcpp_action::create_client<nav2_msgs::action::NavigateToPose>(
            this->get_node_base_interface(),
            this->get_node_graph_interface(),
            this->get_node_logging_interface(),
            this->get_node_waitables_interface(),
            "/navigate_to_pose");
    }

    void stop_robot()
    {
        if (!action_client_->wait_for_action_server(std::chrono::seconds(10)))
        {
            RCLCPP_ERROR(this->get_logger(), "Action server not available after waiting");
            return;
        }

        auto future_goal_handle = action_client_->async_send_goal(nav2_msgs::action::NavigateToPose::Goal());

        if (rclcpp::spin_until_future_complete(this->get_node_base_interface(), future_goal_handle) !=
            rclcpp::FutureReturnCode::SUCCESS)
        {
            RCLCPP_ERROR(this->get_logger(), "Send goal call failed :()");
            return;
        }

        rclcpp_action::ClientGoalHandle<nav2_msgs::action::NavigateToPose>::SharedPtr goal_handle = future_goal_handle.get();
        if (!goal_handle) {
            RCLCPP_ERROR(this->get_logger(), "Goal was rejected by server");
            return;
        }

        // The goal is empty and should be immediately aborted (you may expand this logic as needed)
        auto future_cancel = action_client_->async_cancel_goal(goal_handle);

        if (rclcpp::spin_until_future_complete(this->get_node_base_interface(), future_cancel) !=
            rclcpp::FutureReturnCode::SUCCESS)
        {
            RCLCPP_ERROR(this->get_logger(), "Failed to cancel goal");
        }
    }

private:
    rclcpp_action::Client<nav2_msgs::action::NavigateToPose>::SharedPtr action_client_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<StopBot>();
    node->stop_robot();
    rclcpp::shutdown();
    return 0;
}
