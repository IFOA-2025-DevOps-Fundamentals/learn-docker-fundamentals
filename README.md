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

---

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

- **Microservices architectures** where each service runs in its own container.
- **Continuous Integration/Continuous Deployment** (CI/CD) pipelines.
- **Running multiple instances** of the same application.
- **Developing and testing environments** due to easy reproducibility.


### Key Differences & Comments

Some of the main differences between Virtual Machines and Containers are summarized in the table below:

| Feature              | Virtual Machines                   | Containers                                            |
|----------------------|------------------------------------|-------------------------------------------------------|
| **Isolation**        | Full OS isolation                  | Process-level isolation                               |
| **Boot Time**        | Minutes                            | Seconds                                               |
| **Resource Usage**   | High (full OS per VM)              | Low (shared OS kernel)                                |
| **Performance**      | Lower due to overhead of hypervisor| Near-native performance                               |
| **Portability**      | Limited to hypervisor compatibility| High portability across environments                  |
| **Management**       | Requires hypervisor management     | Managed by container orchestrators (e.g., Kubernetes) |
| **Security**         | Strong isolation                   | Good isolation but depends on the host OS             |
---

Both Virtual Machines and Containers have their advantages and use cases. 
Virtual Machines provide strong isolation and are suitable for running multiple operating systems on the same hardware. 
Containers, on the other hand, are lightweight, fast, and ideal for microservices and environments where 
resource efficiency and portability are crucial.

Choosing between VMs and Containers depends on the specific needs of your application and infrastructure. 
In many modern applications, a combination of both technologies is used to leverage the strengths of each.


### Container History & First Experiments

>Computer containers are lightweight, portable, and executable software packages 
>that encapsulate applications and their dependencies, 
>ensuring consistent and efficient deployment across various computing environments.


The evolution of containers has been a significant milestone in software development and deployment practices.
Some of the main milestones in the history of containers are:
- **IBM VM/370** (1972): Introduced virtual machines (VMs) for running multiple operating systems on a single physical machine.
- **Linux VServers** (2001): Introduced lightweight virtualization for isolating processes and resources.
- **Solaris Containers** (2004): Provided operating system-level virtualization for Solaris systems.
- **FreeBSD Jails** (1999-2000): Introduced OS-level virtualization for FreeBSD systems.
- **Docker** (2013): Revolutionized containerization with a user-friendly platform for building, sharing, and running containers.
- *Kubernetes* (2014): Introduced container orchestration for managing and scaling containerized applications.


## Docker

Docker is a leading platform for developing, shipping, and running applications in containers.
Its key Features are:
- **Containerization Simplified:** Offers an easy-to-use platform for creating, deploying, and running applications in containers.
- **Image-Based Packaging:** Utilizes Docker images, which package applications and their dependencies, ensuring consistency across different environments.
- **Efficient Resource Utilization:** Lightweight containers share the host OS kernel, minimizing resource overhead and maximizing efficiency.
- **Rapid Deployment:** Accelerates application delivery by enabling quick and consistent deployment across various infrastructure environments.


Docker  is now s a comprehensive platform encompassing tools, services, and a thriving ecosystem to manage the entire application lifecycle such as:

- **Docker Engine**: At its core, Docker Engine powers the creation and execution of containers, providing the fundamental technology for building and running applications.
- **Docker Images**: Docker introduces the concept of Docker Images — portable, consistent, and shareable packages that encapsulate an application and its dependencies.
- **Docker Desktop**: Docker Desktop, a user-friendly application, simplifies the development and deployment of containerized applications on local machines.
- **Docker Hub**: Docker Hub, a cloud-based registry, serves as a centralized repository for Docker Images, fostering collaboration and simplifying distribution across the developer community.
- **Docker Compose**: Docker Compose allows users to define and manage multi-container applications, facilitating complex setups and orchestrating the interaction between containers.
- **Docker Swarm**: Docker Swarm, a built-in orchestration tool, enables the management of a cluster of Docker hosts, ensuring scalability, load balancing, and fault tolerance.
- **Integration with Kubernetes**: Docker seamlessly integrates with Kubernetes, a leading container orchestration platform, providing users the flexibility to leverage Kubernetes' advanced features.

**We will use command line tools to learn foundational concepts, then if you want you can also use Docker Desktop :)**


### Installing Docker 

There are many ways to install Docker (Please check here: https://docs.docker.com/engine/install/).
We can arbitrarily distinguish:

- Installing ***Docker on an existing Linux machine*** (physical or VM)
- Installing ***Docker on macOS or Windows***
- Installing ***Docker on cloud VMs***

**Docker Desktop** available for Mac and Windows that is will Integrated with the host OS:
- installed like normal user applications on the host
- provides user-friendly GUI to edit Docker configuration and settings
- Only support running one Docker VM (with multiple containers) at a time

From an internal point of view Docker Desktop: 

- Leverages the host OS virtualization subsystem (e.g. the Hypervisor API on macOS)
- Under the hood, runs a tiny VM (transparent to our daily use)
- Accesses network resources like normal applications (and therefore, plays better with enterprise VPNs and firewalls)
- Supports filesystem sharing through volumes (we'll talk about this later)

An example of the Docker Desktop GUI is shown below:

![docker_desktop.png](images/docker_desktop.png)


### Create First Container

In your Docker environment, just run the following command:

```bash
docker run busybox echo hello world
```

The command will download the `busybox` image from the Docker Hub, create a container from it, 
and run the `echo hello world` command inside the container.

The result will be the output of the `echo` command, which is `hello world`.
If you don't have the `busybox` image locally, Docker will download it from the Docker Hub before creating the container.

The output of the command will be like:

![img_1.png](images/docker_hello_world.png)



### Create an Ubuntu Container

Let's run a more exciting container:

```bash
docker run -it ubuntu
```

This is a brand new container.

It runs a bare-bones, with no additional software installed, Ubuntu Linux distribution.
Additional command line options assocaited to `-it` that is a combination of two options:

- **i** tells Docker to connect us to the container's stdin.
- **t** tells Docker that we want a pseudo-terminal on the target container

The results will be something like:

```bash
root@04c0bb0a6c07:/#
```

where `04c0bb0a6c07` is the container ID and `#` is the command prompt.
We now have a terminal inside the container and we can try to execute some linux commands

Try to run the figlet (a computer program that generates text banners, 
in a variety of typefaces, composed of letters made up of conglomerations of smaller ASCII characters) command in our container

```bash <!-- TODO: Change with Neofetch -->
root@04c0bb0a6c07:/# figlet hello
```

The output will be:

```bash
bash: figlet: command not found
```

This is because the `figlet` command is not installed in the Ubuntu container by default.
We can install it by running the following command to update the package list and install the `figlet` package:

```bash
root@04c0bb0a6c07:/# apt-get update
```

Now we can install the `figlet` package:

```bash
root@04c0bb0a6c07:/# apt-get install figlet
```

If you run the `figlet hello` command again:

```bash
root@04c0bb0a6c07:/# figlet hello
```

The output will be:
<!-- TODO: Change with Neofetch -->
![img.png](images/figlet_hello.png)

Now we can exit the container by logging out of the shell, with **^D** or exit.
Now try to run figlet. Does that work? (It shouldn't; except if, by coincidence, you are running on a machine where figlet was installed before.)
The reasons are:

- We ran an ubuntu container on an Linux/Windows/macOS host.
- They have different, independent packages.
- Installing something on the host doesn't expose it to the container (And vice-versa).
- This is also true even if both the host and the container have the same Linux distro!
- We can run any container on any host. (One exception: Windows containers can only run on Windows hosts; at least for now.)


<!-- TODO: Use the following containers for examples: -->
<!-- TODO: - jpetazzo/clock                           -->
<!-- TODO: - Portainer                                -->
<!-- TODO: - UptimeKuma                               -->
<!-- TODO: - Snippetbox                               -->
<!-- TODO: - WG-Easy (forse)                           -->


---

## Credits
Thanks to Dr. Marco Picone for sharing content and suggestions for the design of this course. The materials shared and used during the design are [here](https://github.com/Distributed-IoT-Software-Arch-Course/docker-playground).

## License  
- The **code** in this repository is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  
- The **documentation and educational materials** are licensed under **CC BY 4.0**. See [LICENSE-docs.md](LICENSE-docs.md) for details.  
