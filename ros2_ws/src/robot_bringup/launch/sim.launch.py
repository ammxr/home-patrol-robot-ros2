from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro
import os

def generate_launch_description():
    # Path to the world file
    world = '/home/ros/worlds/bookstore/bookstore.world'

    # Locate and process the Xacro file
    xacro_file = os.path.join(
        get_package_share_directory('robot_description'),
        'urdf',
        'patrol_robot.xacro'
    )
    robot_description_config = xacro.process_file(xacro_file)
    robot_desc = robot_description_config.toxml()

    # Robot State Publisher (publishes TF and robot_description)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}],
        output='screen'
    )

    # Launch Gazebo with the imported world
    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', '--mute', world,
             '-s', 'libgazebo_ros_factory.so', # ros service to communicate with gazebo (otherwise gazebo runs standalone with no connection to ros)
            ],
        output='screen'
    )

    # Spawn the robot in Gazebo (at origin)
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'patrol_bot', '-topic', 'robot_description', '-x', '0', '-y', '0', '-z', '0.1'],
        output='screen'
    )



    # Static transform for base_footprint -> base_link
    # Without this the TF base_footprint and base_link are 2 separate branches
    base_footprint_to_base_link = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_footprint_to_base_link',
        arguments=[
            '0', '0', '0.05',   # x y z (z = wheel radius)
            '0', '0', '0',      # roll pitch yaw
            'base_footprint',
            'base_link'
        ],
        output='screen'
    )


    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        base_footprint_to_base_link,
        spawn_entity
    ])

