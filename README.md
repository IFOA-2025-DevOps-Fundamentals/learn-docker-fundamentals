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
> - Bare metal hypervisors: 
>   - VMs execute directly on the hardware, without the need of an underlying operating system. 
>   - They have direct access to underlying physical resources (CPU, RAM, memory, network). 
>   - Examples: VMware ESXi, MS Hyper-V, Xen, KVM. 
> - Host hypervisors: 
>   - VMs execute on top of an existing OS. It introduces some overhead. 
>   - Examples: VMware Workstation, VirtualBox, Parallels desktop.

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

The command will download the `busybox` image from the Docker Hub, create a container from it, and run the `echo hello world` command inside the container.

> [!NOTE]
>
> More information about the `busybox` image [here](https://hub.docker.com/_/busybox).

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
![img.png](images/figlet_hello.png)

>[!TIP]
> 
> Now you can try to do the same with another simple terminal program: `neofetch`. 
> 
> Additional information about `neofetch` can be found [here](https://github.com/dylanaraps/neofetch).

Now we can exit the container by logging out of the shell, with **^D** or exit.
After the exit, try to run figlet again. Does that work? (It shouldn't; except if, by coincidence, you are running on a machine where figlet was installed before.)
The reasons are:

- We ran an ubuntu container on an Linux/Windows/macOS host.
- They have different, independent packages.
- Installing something on the host doesn't expose it to the container (And vice-versa).
- This is also true even if both the host and the container have the same Linux distro!
- We can run any container on any host. (One exception: Windows containers can only run on Windows hosts; at least for now.)

> [!NOTE]
> 
> More information about `docker run` [here](https://docs.docker.com/reference/cli/docker/container/run/)

### Local Development & Working Environment

When we use local VMs (with e.g. VirtualBox or VMware), our workflow looks like this:
- create VM from base template (Ubuntu, CentOS...)
- install packages, set up environment
- work on project
- when done, shut down VM
- next time we need to work on project, restart VM as we left it
- if we need to work on multiple projects, we need multiple VMs
- if we have to change something in the environment, we need to update the VM template or the VM itself

Over time, the VM configuration evolves, diverges.
We don't have a clean, reliable, deterministic way to provision that environment.

On the other hand with Containers and Docker the workflow looks like this:

- create container image with our dev environment
- run container with that image
- work on project
- when done, shut down container
- next time we need to work on project, start a new container   <!-- ? On the same project? -->
- if we need to change the environment, we create a new image   <!-- ? Image or layer? -->

We have a clear definition of our environment, and can share it reliably with others.


### Docker Containers Working Modes

With Docker we have three main working modes:

- **Interactive Mode:** 

  allows direct user interaction with a Docker container, providing a shell prompt within the container's environment. 
  
  Ideal for debugging, testing, or exploring the containerized environment interactively.
  
  Example Command: `docker run -it <image_name> /bin/bash`

- **Non-Interactive Mode:** 
  
  runs a container without direct user interaction, suitable for automated processes or scripted workflows. 
  
  Commonly used in CI/CD pipelines or automated deployment scenarios.

  Example Command: `docker run <image_name> my_script.sh`

- **Background Mode:** 

  also known as detached mode runs a container in the background, freeing up the terminal for other commands while the container continues running. 

  Useful for long-running processes or services that don't require immediate user interaction.

  Example Command: `docker run -d <image_name>`


<!-- TODO: add a new chapter: Docker commands from command line -->

### List Running Containers

How can we check that our container is still running?
With `docker ps`, just like the UNIX `ps` command, lists running processes.

```bash
docker ps
```

The output will be something like:

```bash
CONTAINER_ID  IMAGE           ...   CREATED         STATUS        ...
47d677dcfba4  jpetazzo/clock  ...   2 minutes ago   Up 2 minutes  ...
```

Docker tells us:
- The (truncated) **ID** of our container.
- The **image** used to start the container.
- That our container has been **running** (***Up***) for a couple of minutes.
- ***Other information*** (COMMAND, PORTS, NAMES) that we will explain later.


### Stop Containers

There are several ways to stop a container:

- **Graceful Stop**:
  - *Command*: `docker stop <container_name or container_id>`
  - *Description*: Initiates a graceful shutdown of the container, allowing it to complete any ongoing processes and save state before stopping.
  - *Use Case*: Recommended for standard shutdown procedures to prevent data loss or corruption.
- **Forced Stop**:
  - *Command*: `docker kill <container_name or container_id>`
  - *Description*: Forces the immediate termination of the container, forcefully stopping all processes without waiting for them to complete.
  - *Use Case*: Useful when a container is unresponsive or needs to be stopped abruptly.
- **Stopping All Containers (works only on Linux)**:
  - *Command*: `docker stop $(docker ps -q)`
  - *Description*: Stops all running containers at once using a single command.
  - *Use Case*: Streamlines the process of stopping multiple containers simultaneously.
- **Stopping by Name (works only on Linux)**:
    - *Command*: `docker stop $(docker ps -q --filter "name=<container_name>")`
    - *Description*: Stops containers based on their name, allowing more precise control.
    - *Use Case*: Useful when targeting specific containers in a multi-container environment.

Some of these commands and options effective and available on Linux because of the shell syntax.


### List Stopped Containers

We can also see stopped containers, with the -a (--all) option.

```bash
docker ps -a
```

the result will be something like:

```bash
CONTAINER_ID IMAGE          ... CREATED     STATUS
068cc994ffd0 jpetazzo/clock ... 21 min. ago Exited (137) 3 min. ago
57ad9bdfc06b jpetazzo/clock ... 21 min. ago Exited (137) 3 min. ago
47d677dcfba4 jpetazzo/clock ... 23 min. ago Exited (137) 3 min. ago
5c1dfd4d81f1 jpetazzo/clock ... 40 min. ago Exited (0)  40 min. ago
b13c164401fb ubuntu         ... 55 min. ago Exited (130) 53 min. ago
```


### View the Last Started Container

When many containers are already running, it can be useful to see only the last container that was started.
This can be achieved with the **-l ("Last")** flag:

```bash
docker ps -l
```

The output will be something like:

```bash
CONTAINER_ID IMAGE          ... CREATED          STATUS    ...
068cc994ffd0 jpetazzo/clock ... 2 minutes ago Up 2 minutes ...
```

### View Containers Logs

Docker logs containers output.
We can then view the collected logs by a container:

```bash
docker logs <container_name or container_id>
```

The output will be something like:

```bash
$ docker logs 0682392183219831209
Fri Feb 20 00:39:52 UTC 2015
Fri Feb 20 00:39:53 UTC 2015
```

We specified a prefix of the full container ID.
You can, of course, specify the full ID.
The logs command will output the entire logs of the container.
(Sometimes, that will be too much. Let's see how to address that.)

To avoid being spammed with several pages of output, we can use the `--tail` option
The parameter is the number of lines that we want to see.

```bash
docker logs --tail 5 0682392183219831209
```

In this case, we will see the last 5 lines of the logs for the target container with the specified ID.

Just like with the standard UNIX command tail `-f`, we can follow the logs of our container
This will display the last line in the log file.
Then, it will continue to display the logs in real time.
Use `^C` to exit

The command is:

```bash
docker logs -f 0682392183219831209
``` 

The commands can be combined to show the last 5 lines and then follow the logs:

```bash
docker logs --tail 5 -f 0682392183219831209
```


### Restart Containers

There are several ways to restart a container:

- **Manual Restart:**
  - *Command*: `docker restart <container_name or container_id>`
  - *Description*: Manually restarts a stopped or running container, applying changes or simply restarting the container.
  - *Use Case*: Convenient for applying configuration updates or addressing minor issues without recreating the container.
- **Automated Restart Policies:**
  - *Docker Run Option*: `--restart=<policy>`
  - *Description*: Defines restart policies during the initial container launch, specifying conditions for automatic restarts (e.g., "always," "unless-stopped," or "on-failure" - more information [here](https://docs.docker.com/engine/containers/start-containers-automatically/)).
  - *Use Case*: Ensures container availability and resilience by automatically restarting in case of failure or system reboot.
- **Restarting Multiple Containers (Linux Command):**
  - *Command*: `docker restart $(docker ps -q)`
  - *Description*: Restarts all running containers at once using a single command.
  - *Use Case*: Efficiently manages the restart of multiple containers simultaneously.
- **Restarting with Delay:**
  - *Docker Run Option*: `--restart-delay=<duration>`
  - *Description*: Introduces a delay before restarting a container, helping to prevent rapid restart loops in case of repeated failures.
  - *Use Case*: Mitigates issues and allows time for troubleshooting before automatic restart attempts.

As previously explained some of these commands and options effective and available on Linux because of the shell syntax.


<!-- TODO: new section -->
### Docker Images

Now that we have the basics of Docker containers, let's move on to Docker images in order to understand how they work and how to manage them.
Docker Image are a lightweight, standalone, and executable package that encapsulates all the necessary elements to run a piece of software, 
including the code, runtime, libraries, and system tools.
Docker images can be built from scratch or based on existing images available on Docker Hub or other container registries.
They are the building blocks of containers and provide a consistent environment for running applications across different environments.

Components of a Docker Image are:
- **Filesystem Snapshot**: A read-only snapshot of the filesystem with the application code, dependencies, and configurations.
- **Metadata**: Information about the image, including its name, version, and dependencies.

In order to to build a Docker image, we need to create a **Dockerfile**, which is a text file that contains a set of instructions for building the image.

Docker images have a **Layered Architecture**, where each instruction in the Dockerfile adds a new layer to the image.
This layered approach enables efficient caching, reusability, and smaller incremental updates.

A visual text based representation of the layered architecture is shown below:

![docker_layers.png](images/docker_layers.png)

In the layered architecture, ***each instruction*** in the Dockerfile creates a ***new layer*** in the image.
When a new image is built, Docker ***reuses existing layers from the cache***, only rebuilding the layers that have changed.
We have the ***current container layer that is writable*** and can be modified during runtime. <!-- ? What does it mean? -->
The other layers are read-only and shared among multiple containers based on the same image.

For example, we can start from an Ubuntu image and add a new layer with the installation of our dependencies, and applications
such as using `Python`, `Java`, or `Node.js`.

The main management operations for Docker images are:

- **Build**: Create a new image from a Dockerfile.
- **Pull**: Download an image from a container registry.
- **Push**: Upload an image to a container registry.

You can build and keep your images locally, or you can push them to a container registry to share them with others or use them in different environments supporting the same containerization platform and simple deployment.

**Docker Registry** are services that store and distribute Docker images, allowing users to share and access images across different environments.
Those services can be public or private, and the most popular one is Docker Hub.

Each Image has a unique identifier called a **Digest**, which is a cryptographic hash of the image content.
The digest is used to verify the integrity of the image and ensure that it has not been tampered with.
Images can be versioned using **tags**, which are human-readable labels that point to specific versions or configurations of the image.
For example `latest`, `1.0`, or `stable`. A semantic versioning pattern is often used for tags, such as `1.2.3` or following a pattern like: `<major>.<minor>.<patch> (e.g., 1.2.3)`. 

A visual representation of the main Pull and Push concepts together with the idea of Docker registry is shown below ([Source](https://www.tutorialspoint.com/docker/docker_hub.htm)):

![docker_image_push_pull.png](images/docker_image_push_pull.png)


### Containers vs Images

<!-- TODO: Transform the following bullet point into a table -->
- **Definition**:
  - *Docker Image*: A blueprint or snapshot that includes the application code, dependencies, libraries, and configurations. It is a static, immutable file used to create containers.
  - *Docker Container*: A running instance of a Docker image, encapsulating the application and its environment. Containers are dynamic, allowing for interaction and modification.
- **Purpose**:
  - *Docker Image*: Designed for distribution and sharing. It serves as a portable, self-sufficient package that can be run on any system.
  - *Docker Container*: Geared towards execution. It represents a lightweight, isolated environment where applications can run consistently across various environments.
- **Lifecycle**:
  - *Docker Image*: Static and unchanging once created. It serves as the foundation for one or more containers.
  - *Docker Container*: Dynamic and created from an image, runs applications, and can be stopped or removed without affecting the underlying image.
- **Mutability**:
  - *Docker Image*: Immutable. Any changes require creating a new image.
  - *Docker Container*: Mutable. Changes made during runtime, but those changes are lost once the container stops (unless committed to a new image).
- **Storage**:
  - *Docker Image*: Stored as layers in a registry (e.g., Docker Hub) and cached locally. Read-only.
  - *Docker Container*: Temporary storage in the container's writable layer. Read-write during runtime, changes persist until the container stops.

As a general rule of thumb, **images** are used for **distribution and sharing**, while **containers** are used for **execution and runtime environments**.

From the **same image** we then can create **multiple containers**, each with its own isolated environment and runtime characteristics as illustrated below:

![same_image_multiple_containers.png](images/same_image_multiple_containers.png)


### Object-Oriented Programming & Containers

It is possible to think of Docker containers as instances of a class in object-oriented programming.
In object-oriented programming, a **class is a blueprint** for creating objects (instances) that share common attributes and behaviors.
Some points associated with this analogy are:

- **Images vs. Classes**:
  - *Images (Containers)*: Conceptually similar to classes in Object-Oriented Programming (OOP).
  - *Explanation*: Images serve as blueprints or templates for containers, defining the application, dependencies, and configurations. They are static and represent the potential for creating multiple instances.
- **Layers vs. Inheritance**:
  - *Layers (Containers)*: Conceptually similar to inheritance in OOP.
  - *Explanation*: Layers in Docker images represent incremental changes. Each layer adds or modifies specific aspects, analogous to how inheritance allows new classes to inherit characteristics from existing classes, promoting code reuse and modification.
- **Containers vs. Instances**:
  - *Containers (Docker)*: Conceptually similar to instances in OOP.
  - *Explanation*: Containers are the dynamic, runnable instances created from Docker images. They represent the execution environment for applications, much like instances in OOP are specific occurrences of a class with unique states.

<!-- TODO: Restart from "Creating a New Image" -->


<!-- TODO: Use the following containers for examples: -->
<!-- TODO: - jpetazzo/clock                           -->
<!-- TODO: - Portainer                                -->
<!-- TODO: - UptimeKuma                               -->
<!-- TODO: - Snippetbox                               -->
<!-- TODO: - WG-Easy (forse)                          -->
---

## Credits
Thanks to Dr. Marco Picone for sharing content and suggestions for the design of this course. The materials shared and used during the design are [here](https://github.com/Distributed-IoT-Software-Arch-Course/docker-playground).

## License  
- The **code** in this repository is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  
- The **documentation and educational materials** are licensed under **CC BY 4.0**. See [LICENSE-docs.md](LICENSE-docs.md) for details.  
