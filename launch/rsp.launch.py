import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    pkg_path = os.path.join(get_package_share_directory('agri_bot'))
    urdf_file = os.path.join(pkg_path, 'description', 'robot.urdf.xacro')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation time'),
        
        DeclareLaunchArgument(
            'urdf_file',
            default_value=urdf_file,
            description='URDF/XACRO file to load'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'robot_description': ParameterValue(
                    Command(['xacro ', LaunchConfiguration('urdf_file')]),
                    value_type=str
                )
            }]
        )
    ])
