# Docker Commands
## Local Development & Working Environment

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

## Docker Containers Working Modes

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

## List Running Containers

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

## Stop Containers

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

## List Stopped Containers

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

## View the Last Started Container

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

## View Containers Logs

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

## Restart Containers

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

## Let's Experiment!
>[!TIP]
> 
> Test Docker commands using the `jpetazzo/clock` image! 