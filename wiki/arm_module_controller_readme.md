# Arm Module UR5 Controller
Used for setting up the UR5e manipulator using Universal Robot ROS Driver and MoveIt
- [Setup guide](wiki/setup.md#dependency)
- [Docker](wiki/setup.md#docker)
- [Resources](wiki/resource.md)

## Codebase Structure
- `cpp` codebase in cpp (Python code maybe be ported to cpp for performance in the end). Not yet developed, only has scratch files 
- `python` code base in Python, using MoveIt Python API
    - `src` libraries
        - `collision_manager.py`, `gripper.py` extra settings for controller, not used for now
        - `UR5e.py` robot main planner and controller, using MoveIt
        - `utility.py`
    - `scripts.py` executables to run ROS nodes 
        - `run_robot_controller.py` ROS node to coordinate the mission of the robot, operate on an instance of the UR5e controller. For testing purposes, it can either:
            - Directly read a json file of poses and controll the robot to reach those goals
            - Receive goals one by one through service call, complete them sequentially
        - `move_robot_client.py` ROS client to make service call that sends pose goals to the controller
- `launch` ROS launch files to launch a custom robot (UR5e with added gripper, base, camera, etc). Not yet developed, only has scratch files 
- `srv` set up ROS service
- `urdf` custom URDF to add camera, based, etc. Not yet developed, only has scratch files 
- `docker` Docker setup the package


## Important Notes
```bash
move_group = MoveGroupCommander("manipulator")
move_group.get_current_pose()
```

get_current_pose() returns pose in base_link frame, while ing UR teach pendant Move tab, frame Base shows XYZRPY in base frame

In CHANGELOG.rst:
"Note that 'base' is essentially 'base_link' but rotated by 180
  degrees over the Z-axis. This is necessary as the visual and
  collision geometries appear to also have their origins rotated
  180 degrees wrt the real robot."

## MVPS Integration
This project integrates with MVPS - private repo, which is an active perception pipeline for reconstruction. [Document here](wiki/mvps_integration.md).
