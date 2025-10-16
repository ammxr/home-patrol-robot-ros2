# 🏠 Home Patrol Robot

**Home Patrol Robot** is a ROS 2-based simulation designed to navigate and patrol an indoor environment using the Gazebo simulator.
It includes a custom bookstore world and a simple differential-drive robot model defined with URDF/Xacro, spawnable directly into Gazebo.

---

## Start Instructions

### 1. Launch the Docker Container
Build and start the simulation environment:
```bash
docker compose up -d
```

### 2. Enter the Running Container
```bash
docker exec -it ros2_sim bash
```

### 3. Source ROS 2 and Your Workspace
Inside the container:
```bash
source /opt/ros/humble/setup.bash
source /ros2_ws/install/setup.bash
```

### 4. Launch the Simulation
Run the main simulation launch file:
```bash
ros2 launch robot_bringup sim.launch.py
```

This will:
- Start Gazebo with the **bookstore** world  
- Spawn the custom **patrol_bot** model  
- Initialize the `robot_state_publisher` and `gazebo_ros` interfaces  

---

## Independantly Testing the Gazebo Map

### View the Bookstore World Only
If you just want to test the environment without launching ROS 2 nodes, execute the following from inside the container shell:
```bash
gazebo --verbose --mute /home/ros/worlds/bookstore/bookstore.world
```

---

## Rebuilding and Running the Launch File Manually

If you have made changes to the robot description or launch files:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

Then go back to the home directory (so Gazebo can find the `models/` folder) and run:
```bash
export GAZEBO_MODEL_DATABASE_URI=""   # Prevents Fuel-related warnings
ros2 launch robot_bringup sim.launch.py
```

---

## 📁 Project Structure

```
home_patrol_robot/
├── docker-compose.yml          # Container setup and environment config
├── worlds/                     # Custom Gazebo worlds (e.g., bookstore)
├── models/                     # Model resources for Gazebo
├── ros2_ws/
│   ├── src/
│   │   ├── robot_description/  # URDF/Xacro robot definitions
│   │   ├── robot_bringup/      # Launch files and bringup logic
│   │   └── follow_waypoints/   # Navigation / movement logic
│   ├── build/
│   ├── install/
│   └── log/
└── README.md
```
