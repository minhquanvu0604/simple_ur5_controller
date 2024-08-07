#! /usr/bin/env python3

import os, sys

import numpy as np
from threading import Thread
from enum import Enum
from copy import deepcopy

import rospy
import tf2_ros
from sensor_msgs.msg import JointState



# Add path
current_dir = os.path.dirname(__file__) # dir scripts
parent_dir = os.path.dirname(current_dir)  # dir python
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

sys.path.append('/home/quanvu/ros/apple_ws/src/simple_ur5_controller/python')


# Importing planner module
from src.UR5e import UR5e
from src.collision_manager import CollisionManager
from src.utility import *


CONTROL_RATE = 10  # Hz
HOME_CONFIG = "home"
UP_CONFIG = "up"


class MissionPlanner:
    
    def __init__(self) -> None:
        rospy.init_node("simple_ur5_controller", log_level=1, anonymous=True)
        rospy.loginfo("Initialising MissionPlanner")
        self._rate = rospy.Rate(CONTROL_RATE)

        # Initialize the UR3e controller
        self.robot = UR5e()
        self._system_halted = False
        self._success = True

        # @NOTE: no Collision at the moment
        # self.collisions = CollisionManager(self.robot.get_scene())

        # Setup the scene with ur3e controller and homing
        # self.robot.go_to_target_pose_name(UP_CONFIG)
        # self.robot.open_gripper_to(width=580, force=200)

        # @TODO: review this method
        # # TF2 listener and broadcaster to deal with the transformation
        # self.tf_buffer = tf2_ros.Buffer()
        # self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)
        # self.tf_broadcaster = tf2_ros.TransformBroadcaster()

        # TODO: review estop thread
        # Initialize the safety thread
        # self._safety_thread = Thread(target=self.safety_check)
        # self._safety_thread.start()

        rospy.on_shutdown(self._cleanup)

        self._system_loop()


    def _system_loop(self) -> None:

        # home = [17.47, -85.7, 82.5, -86.4, -86.4, 10]

        goal1 = Pose()
        goal1.position.x = -0.3
        goal1.position.y = 0.5
        goal1.position.z = 0.6
        goal1.orientation = self.robot.get_current_pose().orientation
        self.robot._group.go(goal1, wait=True)
        self.robot._group.clear_pose_targets()
        rospy.sleep(1)
        
        goal2 = Pose()
        goal2.position.x = 0
        goal2.position.y = 0.6
        goal2.position.z = 0.5
        goal2.orientation = self.robot.get_current_pose().orientation
        self.robot._group.go(goal2, wait=True)
        self.robot._group.clear_pose_targets()
        rospy.sleep(1)
        
        goal3 = Pose()
        goal3.position.x = 0.3
        goal3.position.y = 0.2
        goal3.position.z = 0.6
        goal3.orientation = self.robot.get_current_pose().orientation
        self.robot._group.go(goal3, wait=True)
        self.robot._group.clear_pose_targets()
  

    def _cleanup(self) -> None:
        rospy.loginfo("Cleaning up")
        # self._safety_thread.join()
        self.robot.shutdown()
        # self.collisions.remove_collision_object()
        rospy.loginfo("Clean-up completed")


if __name__ == "__main__":
    mp = MissionPlanner()