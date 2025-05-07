from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="buttons_server",
            executable="server_stand_up"
        ),
        Node(
            package="buttons_server",
            executable="hear_server"
<<<<<<< HEAD
        ),
        Node(
            package="button_analyzer",
            executable="button_analyzer"
        ),
        Node(
            package="low_level_control",
            executable="low_level_control"
        )

=======
        )
>>>>>>> 6f4835ade37443ce8aa8931b2b87ada43ecaac6b
    ])