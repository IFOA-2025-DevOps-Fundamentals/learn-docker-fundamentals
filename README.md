# Docker Fundamentals
A gentle introduction to Docker, containers creation and management, and containerized development.

## Course Goals
The course contained in this repository is meant to provide a basic understanding of Docker principles, how it works, how to create, manage and run containers, and how to develop a container for a personal application. It offers a hands-on experience with Docker commands, Dockerfiles, and container management including also a brief presentation of Docker Compose.

## TOC
The outline of the course is as follows: 
- [Virtual Machines & Containers](#virtual-machines--containers)
  - [Virtual Machines](#virtual-machines)
  - [Containers](#containers)
  - [Key Differences & Comments](#key-differences--comments)
  - [Container History & First Experiments](#container-history--first-experiments)
- [Docker](#docker)
  - [Installing Docker](#installing-docker)
  - [Create First Container](#create-first-container)
  - [Create an Ubuntu Container](#create-an-ubuntu-container)
  - [Local Development & Working Environment](#local-development--working-environment)
  - [Docker Containers Working Modes](#docker-containers-working-modes)
  - [List Running Containers](#list-running-containers)
  - [Stop Containers](#stop-containers)
  - [List Stopped Containers](#list-stopped-containers)
  - [View the Last Started Container](#view-the-last-started-container)
  - [View Containers Logs](#view-containers-logs)
  - [Restart Containers](#restart-containers)
  - [Containers vs Images](#containers-vs-images)
  - [Object-Oriented Programming & Containers](#object-oriented-programming--containers)
  - [Creating a New Image](#creating-a-new-image)
  - [Images History](#images-history)
  - [Building & Caching](#building--caching)
  - [Namespaces & Images Management](#namespaces--images-management)
  - [Listing Available Images](#listing-available-images)
  - [Searching for Images](#searching-for-images)
  - [Downloading Images](#downloading-images)
  - [Images & Tags](#images-and-tags)
  - [Images and Multiple Architecture](#images-and-multiple-architectures)
  - [Networking](#networking)
  - [Volumes](#volumes)
  - [Docker Compose](#docker-compose)
- [Build Our First Docker Application](#build-our-first-docker-application)
  - [Dockerfile](#dockerfile)
  - [Build the Container](#build-the-container)
  - [Run the Container](#run-the-container)
  - [Run the Container with Configuration File](#run-the-container-with-configuration-file)
  - [Stop & Remove the Container](#stop--remove-the-container)

## Virtual Machines & Containers
![vms_vs_containers.png](images/vms_vs_containers.png)

In the world of virtualization and cloud computing, 
two primary technologies are widely used: **Virtual Machines (VMs)** and **Containers**. 
Both have their unique characteristics and different use cases. 
Understanding the differences between them is essential for choosing the right technology for your infrastructure needs.
Additional information and references can be found at the following Links: [https://www.atlassian.com/microservices/cloud-computing/containers-vs-vms](https://www.atlassian.com/microservices/cloud-computing/containers-vs-vms)

### Virtual Machines

Virtual Machines (VMs) are software-based emulations of physical computers that run on a physical host machine.
Their main characteristics are:

1. **Hypervisor-Based**: VMs run on a hypervisor, which can be either Type 1 (bare-metal) or Type 2 (hosted).
2. **Complete OS**: Each VM includes a full operating system (guest OS) along with the application and its dependencies.
3. **Isolation**: VMs provide strong isolation between different VMs as each VM runs a separate OS.
4. **Resource Allocation**: VMs require more system resources (CPU, memory, storage) because each VM runs its own OS.
5. **Boot Time**: VMs typically have longer boot times compared to containers because they need to boot the entire OS.

> [!NOTE]  
> - Bare metal hypervisors: the VMs execute directly on the hardware, without the need of an underlying operating system. They have direct access to underlying physical resources (CPU, RAM, memory, network). Examples: VMware ESXi, MS Hyper-V, Xen, KVM. 
> - Host hypervisors: VMs execute on top of an existing OS. It introduces some overhead. Examples: VMware Workstation, VirtualBox, Parallels desktop.

VMs change the way we think about hardware and software and open up new possibilities for IT infrastructure.
They are widely used in various scenarios, including:

- Running applications that require strong isolation.
- Legacy application support that requires a specific OS.
- Multi-tenant environments where security and isolation are priorities.
- Running different operating systems on the same physical hardware.

### Containers

On the other hand, Containers are a form of operating system-level virtualization 
that allows multiple isolated **user-space instances** to run on a single host OS.
User-space instance means that each container runs as a separate process in the host OS, instead of booting a full OS like VMs.
This approach provides a lightweight and efficient way to run applications in isolated environments without the overhead of a full OS.
A container is a lightweight, standalone, and executable package that includes the application and its dependencies and 
that uses shared resources from the host OS and a layered file system. The main characteristics of containers are:

1. **Lightweight**: Containers share the host OS kernel and are much more lightweight than VMs.
2. **Fast Boot Time**: Containers can start almost instantly as they do not require booting an entire OS.
3. **Resource Efficiency**: Containers use fewer resources since they share the host OS and libraries.
4. **Portability**: Containers package the application and its dependencies, making them portable across different environments.
5. **Isolation**: Containers provide process-level isolation using namespaces and control groups (cgroups).

The rise of containers has transformed the way we develop, deploy, and manage applications.
In particular they enabled the following use cases:

- Microservices architectures where each service runs in its own container.
- Continuous Integration/Continuous Deployment (CI/CD) pipelines.
- Running multiple instances of the same application.
- Developing and testing environments due to easy reproducibility.

## Credits
Thanks to Dr. Marco Picone for sharing content and suggestions for the design of this course. The materials shared and used during the design are [here](https://github.com/Distributed-IoT-Software-Arch-Course/docker-playground).

## License  
- The **code** in this repository is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  
- The **documentation and educational materials** are licensed under **CC BY 4.0**. See [LICENSE-docs.md](LICENSE-docs.md) for details.  
