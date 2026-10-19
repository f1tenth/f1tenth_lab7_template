"""What the autograder runs on Levine (levine_blocked, three laps, and the pose checks):

    ros2 launch mpc levine_launch.py

Everything the graded run needs goes here: one node or several, Python or
C++, the waypoints to follow and the parameter values that suit Levine
(spielberg_launch.py is Spielberg's). Start your own nodes only: the
simulator is already running.
"""
from launch import LaunchDescription
from launch_ros.actions import Node

# 'mpc_node.py' is scripts/mpc_node.py, 'mpc_node' is the C++
# src/mpc_node.cpp: name the one you wrote
EXECUTABLE = 'mpc_node.py'

# `track` tells the skeleton which waypoints to load; add this track's values
# for the other parameters your node declares, e.g. 'max_speed': 6.0, or give
# it a full .yaml config file
PARAMETERS = {'track': 'levine'}


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mpc',
            executable=EXECUTABLE,
            output='screen',
            parameters=[PARAMETERS],
        ),
    ])
