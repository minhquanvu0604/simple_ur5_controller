# Simple UR5 Controller
Used for setting up the UR5e manipulator using Universal Robot ROS Driver and MoveIt

## Resources
### Universal Robot ROS Driver - [link](https://github.com/ros-industrial/universal_robot)
- Install the External Control URCap - DONE
- Set the IP Address for the ROS PC 
- Tutorials for e-Series robot
- Set up tool communication on an e-Series robot
- Extract robot's calibration using ur_calibration
- Start the robot driver

```roslaunch ur_robot_driver <robot_type>_bringup.launch robot_ip:=192.168.56.101```

...


## Dependency
- ROS Noetic - Ubuntu 20.04

- Control real hardware - [Universal_Robots_ROS_Driver](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver)
```bash
sudo apt install ros-noetic-ur-robot-driver
```

- Control in Gazebo Simulation - ur_gazebo
```bash
sudo apt-get install ros-noetic-ur-gazebo
```

- MoveIt!
```bash
sudo apt install ros-noetic-moveit
```

- MoveIt! Config
```bash
sudo apt-get install ros-noetic-ur5e-moveit-config
```

# Launching UR5 model with base
To be done
## Launching Simulation
To be done


# Launching only the UR5 
## Launching Real Hardware
Start the robot driver

```roslaunch ur_robot_driver ur5e_bringup.launch robot_ip:=192.168....```

Launch UR5e MoveIt config

```roslaunch ur5e_moveit_config moveit_planning_execution.launch```

Starting up RViz with a configuration including the MoveIt! Motion Planning plugin

```roslaunch ur5e_moveit_config moveit_rviz.launch```

## Launching Simulation
Bring up the simulated robot in Gazebo

```roslaunch ur_gazebo ur5e_bringup.launch ```

Setting up the MoveIt! nodes to allow motion planning

```roslaunch ur5e_moveit_config moveit_planning_execution.launch sim:=true```

Starting up RViz with a configuration including the MoveIt! Motion Planning plugin

```roslaunch ur5e_moveit_config moveit_rviz.launch```

Launch the test node to go through a set of waypoints in cfg/list_poses.json. First cd to simple_ur5_controller/python/scripts/

```python3 reach_waypoints.py```
