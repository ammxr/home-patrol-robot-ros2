# ubuntu 22.04 + ros2 humble w/ desktop tools 
FROM osrf/ros:humble-desktop

ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash","-lc"]

# install dependancies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ros-humble-navigation2 \
      ros-humble-nav2-bringup \
      ros-humble-slam-toolbox \
      ros-humble-gazebo-ros-pkgs \
      python3-colcon-common-extensions \
      python3-pip \
      && rm -rf /var/lib/apt/lists/*

# setup non-root user
ARG USER=ros
ARG UID=1000
RUN useradd -m -u ${UID} ${USER} || true
USER ${USER}
WORKDIR /home/${USER}

ENV ROS_WORKSPACE=/home/${USER}/ros2_ws
