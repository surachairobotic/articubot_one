import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Declare the names of the frames
    map_frame = 'map'
    odom_frame = 'odom'
    base_footprint_frame = 'base_footprint'
    laser_link_frame = 'laser_link'
    imu_link_frame = 'imu_link'
    camera_link_frame = 'camera_link'
    chassis_link_frame = 'chassis'

    # Declare the static transform nodes
    map_odom_broadcaster = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', map_frame, odom_frame],
        output='screen'
    )

    odom_base_broadcaster = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', odom_frame, base_footprint_frame],
        output='screen'
    )

    base_laser_broadcaster = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', chassis_link_frame, laser_link_frame],
        output='screen'
    )

    base_imu_broadcaster = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', chassis_link_frame, imu_link_frame],
        output='screen'
    )

    base_camera_broadcaster = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', chassis_link_frame, camera_link_frame],
        output='screen'
    )

    # Create the launch description and add the nodes
    ld = LaunchDescription()
    #ld.add_action(map_odom_broadcaster) # comment when open slamtoolbox
    #ld.add_action(odom_base_broadcaster) # comment when open slamtoolbox
    ld.add_action(base_laser_broadcaster)
    ld.add_action(base_imu_broadcaster)
    ld.add_action(base_camera_broadcaster)

    return ld
