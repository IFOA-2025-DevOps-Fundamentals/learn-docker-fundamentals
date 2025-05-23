# Docker Compose

There are scenarios where we need to run multiple containers that work together to provide a complete application.
Handling multiple containers can be complex, especially when we need to manage their dependencies and configurations.

>[!NOTE]
> Docker Compose is a tool that ***simplifies the process of defining and running multi-container*** Docker applications.

Key Features are:
- **Declarative Configuration**: Define services, networks, and volumes in a YAML file
- **Single Command**: Use for example docker-compose up to start and initialize the entire application stack

It is possible to define services and their deployment in terms of image, ports, volumes, and environment variables

Other different solutions and systems to manage containers and containerized applications are available, such as **Kubernetes**, **OpenShift**, and **Docker Swarm**. 
In this playground we are going to use Docker Compose to manage the containers and the application stack.

Docker compose works with a YAML file called `docker-compose.yml` that defines the services, networks, and volumes for the application stack.
For example if we want to create a simple deployment where we have a Python container and a MySQL container we can define the following `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  web:
    image: myapp:1.0
    container_name: python_web_app
    ports:
      - "5000:5000"
    volumes:
      - ./config:/app/config
    networks:
      - my_network
    depends_on:
      - db

  db:
    image: mysql:8.0
    container_name: mysql_db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: mydatabase
      MYSQL_USER: myuser
      MYSQL_PASSWORD: mypassword
    volumes:
      - ./db_data:/var/lib/mysql
    networks:
      - my_network

networks:
  my_network:
    driver: bridge
```

Now we are going to analyze the content of the `docker-compose.yml` file in order to understand the structure and the content.

```yaml
version: '3.8'
```
Specifies the version of the Docker Compose file format. 
Version 3.8 is used here, which is compatible with Docker Engine version 19.03.0 and above.

The next step is to define the services to be run in the Docker containers.

```yaml
web:
    image: myapp:1.0
    container_name: python_web_app
    ports:
      - "5000:5000"
    volumes:
      - ./config:/app/config
    networks:
      - my_network
    depends_on:
      - db
```

Involves the following key elements:

- `image`: Specifies the Docker image to use for the container. Here, it uses `myapp:1.0` previously built and available on the Docker host (if the image is not available, Docker Compose will pull it from a registry).
- `container_name`: Sets the name of the container to `python_web_app`.
- `ports`: Maps port 5000 of the container to port 5000 on the host machine.
- `volumes`: Mounts host directories into the container:
  - `./config:/app/config`: Mounts the `config` directory on the host to `/app/config` in the container.
- `networks`: Connects the container to the `my_network` network (if the network does not exist, Docker Compose will create it).
- `depends_on`: Ensures that the `db` service starts before the `web` service. This allows the `web` service to wait for the `db` service to be ready before starting.

For second microservice, the `db` service, the following key elements are defined:

```yaml
db:
  image: mysql:8.0
  container_name: mysql_db
  restart: always
  environment:
    MYSQL_ROOT_PASSWORD: rootpassword
    MYSQL_DATABASE: mydatabase
    MYSQL_USER: myuser
    MYSQL_PASSWORD: mypassword
  volumes:
    - ./db_data:/var/lib/mysql
  networks:
    - my_network
```

- `image`: Specifies the Docker image to use for the container. Here, it uses `mysql:8.0`.
- `container_name`: Sets the name of the container to `mysql_db`.
- `restart`: Always restarts the container if it stops.
- `environment`: Sets environment variables for MySQL (the support for environment variables is specific to the MySQL image and the associated Dockerfile and its documentation on Docker Hub).
  - `MYSQL_ROOT_PASSWORD`: Sets the root password for the MySQL database.
  - `MYSQL_DATABASE`: Specifies the name of the default database to create.
  - `MYSQL_USER`: Specifies the name of the user.
  - `MYSQL_PASSWORD`: Sets the password for the user.
- `volumes`: Mounts the `db_data` directory on the host to `/var/lib/mysql` in the container. This allows MySQL data to persist between container restarts (also this is a best practice to persist data generated by the database and the correct path is documented on the container information).
- `networks`: Connects the container to the `my_network` network.

The fact that the `web` service depends on the `db` service ensures that the ***database service starts before the web service***.
Furthermore, if two containers are connected to the same network, they can communicate with each other using the service name as the hostname.
This is fundamental and ***avoids the need to use IP addresses to communicate between containers***.
See Section [Docker & Networking](../README.md#docker--networking) for more information.

The next section of the docker compose file defines the custom bridge network that the services will use to communicate with each other.

```yaml
networks:
  my_network:
    driver: bridge
```

The above portion of the configuration defines a custom bridge network named `my_network` that the services will use to communicate with each other.

As additional notes: 

- Ensure the `./config`, and `./db_data` directories ***exist on your host machine***.
- You can adjust the paths and environment variables as needed for your specific setup.
- To bring up the application, run `docker-compose up` (or `docker compose up`) in the directory containing this Docker Compose file (See next Sub-Sections).

## Docker Compose Usage

Run the application described in the compose file

```bash
docker-compose up
```

You can also run the application as a daemon in background

```bash
docker-compose up -d
```

You can view active containers associated to the composed application: 

```bash
docker-compose ps
```

To view the logs of all running containers at once, run the following command:

```bash
docker-compose logs
```

To view the logs of a specific target docker compose SERVICE NAME (not container name) by its name, run the following command:

```bash
docker-compose logs python_web_app
```

To retrieve the four most recent lines of the log from all running containers, run the following command:

```bash
docker-compose logs --tail=4
```

We can continuously watch the log output in real-time by passing the -f (short for "--follow") flag to the docker-compose logs command. Run the following command to stream the logs:

```bash
docker-compose logs -f --tail=4
```

To view the logs generated until five minutes ago, run the following command:

```bash
docker-compose logs --until=5m
```

For example, to view logs that occurred between 3 P.M. and 4 P.M on May 31st, run the following command:

```bash
docker-compose logs –since=2023-05-31T15:00:00 –until=2023-05-31T16:00:00
```

You can stop the entire application with all its container using:

```bash
docker-compose down
```

You can stop, remove everything with the following command: 

```bash
docker-compose rm -fsv
```

>[!NOTE]
>
> In recent version, `docker-compose` has been replaced with `docker compose`.

## Let's Experiment!
Now try to create the following services: 
- Portainer (more info [here](https://docs.portainer.io/start/install-ce/server/docker/linux))
- Uptime-Kuma (more info [here](https://uptime.kuma.pet/))
- Snippet-Box (more info [here](https://github.com/pawelmalak/snippet-box))

Part of the exercise is to find the image online to retrieve its name and the selected version.

Finally, setup your working environment on VSCode and implement the service: 
- [ ] make a folder for each service you want to implement; 
- [ ] inside of each folder, create a `docker-compose.yaml` file; 
- [ ] if necessary, in the compose file specify binded folders names ending with `-volume` (e.g., for Portainer the created folder containing the service data can be name `portainer-volume`);
- [ ] Run the container, and check the result!

