# Docker Fundamentals
A gentle introduction to Docker, containers creation and management, 
and containerized development.

## Course Goals
The course contained in this repository is meant to provide a basic understanding 
of Docker principles, how it works, how to create, manage and run containers, 
and how to develop a container for a personal application. 
It offers a hands-on experience with Docker commands, Dockerfiles, and container 
management including also a brief presentation of Docker Compose.

## Table Of Contents
The outline of the course is as follows: 
- [Virtual Machines & Containers](sections/01_virtual_machines_and_containers.md)
  - [Virtual Machines](sections/01_virtual_machines_and_containers.md#virtual-machines)
  - [Containers](sections/01_virtual_machines_and_containers.md#containers)
  - [Key Differences & Comments](sections/01_virtual_machines_and_containers.md#key-differences--comments)
  - [Container History & First Experiments](sections/01_virtual_machines_and_containers.md#container-history--first-experiments)
- [Docker](sections/02_docker.md)
  - [Installing Docker](sections/02_docker.md#installing-docker)
  - [Create First Container](sections/02_docker.md#create-first-container)
  - [Create an Ubuntu Container](sections/02_docker.md#create-an-ubuntu-container)
- [Docker Commands](sections/03_docker_commands.md)
  - [Local Development & Working Environment](sections/03_docker_commands.md#local-development--working-environment)
  - [Docker Containers Working Modes](sections/03_docker_commands.md#docker-containers-working-modes)
  - [List Running Containers](sections/03_docker_commands.md#list-running-containers)
  - [Stop Containers](sections/03_docker_commands.md#stop-containers)
  - [List Stopped Containers](sections/03_docker_commands.md#list-stopped-containers)
  - [View the Last Started Container](sections/03_docker_commands.md#view-the-last-started-container)
  - [View Containers Logs](sections/03_docker_commands.md#view-containers-logs)
  - [Restart Containers](sections/03_docker_commands.md#restart-containers)
- [Docker Images](sections/04_docker_images.md)
  - [Containers vs Images](sections/04_docker_images.md#containers-vs-images)
  - [Object-Oriented Programming & Containers](sections/04_docker_images.md#object-oriented-programming--containers)
  - [Creating a New Image](sections/04_docker_images.md#creating-a-new-image)
  - [Images History](sections/04_docker_images.md#images-history)
  - [Building & Caching](sections/04_docker_images.md#building--caching)
  - [Namespaces & Images Management](sections/04_docker_images.md#namespaces--images-management)
  - [Listing Available Images](sections/04_docker_images.md#listing-available-images)
  - [Searching for Images](sections/04_docker_images.md#searching-for-images)
  - [Downloading Images](sections/04_docker_images.md#downloading-images)
  - [Images & Tags](sections/04_docker_images.md#images-and-tags)
  - [Images and Multiple Architecture](sections/04_docker_images.md#images-and-multiple-architectures)
- [Docker Networking & Volumes](sections/05_docker_networking_and_volumes.md)
  - [Networking](sections/05_docker_networking_and_volumes.md#networking)
  - [Volumes](sections/05_docker_networking_and_volumes.md#volumes)
- [Docker Compose](sections/06_docker_compose.md#docker-compose)
  - [Docker Compose Usage](sections/06_docker_compose.md#docker-compose-usage)
- [Build Our First Docker Application](sections/07_build_our_first_docker_app.md)
  - [Dockerfile](sections/07_build_our_first_docker_app.md#dockerfile)
  - [Build the Container](sections/07_build_our_first_docker_app.md#build-the-container)
  - [Run the Container](sections/07_build_our_first_docker_app.md#run-the-container)
  - [Run the Container with Configuration File](sections/07_build_our_first_docker_app.md#run-the-container-with-configuration-file)
  - [Stop & Remove the Container](sections/07_build_our_first_docker_app.md#stop--remove-the-container)

<!-- TODO: - Add section comparing different container technologies -->

---

# Credits
Thanks to Dr. Marco Picone for sharing content and suggestions for the design of this course. The materials shared and used during the design are [here](https://github.com/Distributed-IoT-Software-Arch-Course/docker-playground).

# License  
- The **code** in this repository is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  
- The **documentation and educational materials** are licensed under **CC BY 4.0**. See [LICENSE-docs.md](LICENSE-docs.md) for details.  
