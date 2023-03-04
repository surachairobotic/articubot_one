import launch
import launch_ros.actions
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    ekf_config = launch.substitutions.LaunchConfiguration('ekf_config', default='$(find articubot_one)/config/ekf.yaml')

    ekf_node = launch_ros.actions.Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter',
        output='screen',
        parameters=[{'use_sim_time': True}],
        remappings=[('odom', '/agv/odom'), ('imu/data', '/imu/imu'), ('imu/mag', '/imu/mag')],
        arguments=['load', ekf_config])

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('ekf_config', default=ekf_config),

        ekf_node
    ])


# Author: Addison Sears-Collins
# Date: August 31, 2021
# Description: Launch a basic mobile robot
# https://automaticaddison.com

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():

  # Set the path to different files and folders.
  pkg_share = FindPackageShare(package='articubot_one').find('articubot_one')
  default_launch_dir = os.path.join(pkg_share, 'launch')
  #robot_localization_file_path = "~/dev_ws/src/articubot_one/config/ekf.yaml" 
  
  # Launch configuration variables specific to simulation
  headless = LaunchConfiguration('headless')
  model = LaunchConfiguration('model')
  rviz_config_file = LaunchConfiguration('rviz_config_file')
  use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
  use_rviz = LaunchConfiguration('use_rviz')
  #use_sim_time = LaunchConfiguration('use_sim_time')
  use_simulator = LaunchConfiguration('use_simulator')
  world = LaunchConfiguration('world')

  # Declare the launch arguments  
  declare_use_sim_time_cmd = DeclareLaunchArgument(
    name='use_sim_time',
    default_value='True',
    description='Use simulation (Gazebo) clock if true')

  # Start robot localization using an Extended Kalman filter
  start_robot_localization_cmd = Node(
    package='robot_localization',
    executable='ekf_node',
    name='ekf_filter_node',
    output='screen',
    parameters=[os.path.join(get_package_share_directory("articubot_one"), 'config', 'hos_ekf.yaml'), 
    {'use_sim_time': False}])
  
  # Create the launch description and populate
  ld = LaunchDescription()

  # Add any actions
  ld.add_action(start_robot_localization_cmd)

  return ld
