from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

def generate_launch_description():
    world = '/home/ros/worlds/bookstore/bookstore.world'
    urdf  = '/home/ros/ros2_ws/install/robot_description/share/robot_description/urdf/patrol_robot.urdf'

    return LaunchDescription([
        # launching Gazebo with imported world
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '--mute', world],
            output='screen'),

        # spawning our robot into Gazebo (need to remove turtlebot from map)
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'patrol_bot', '-file', urdf, '-x', '0', '-y', '0', '-z', '0.1'],
            output='screen'),
    ])

