Tutorial steps:

1. `docker build ml-docker -t ml-docker:latest`
2. `docker run ml-docker:latest`
3. `docker run --gpus all --name <container-instance-name> --shm-size=12gb --env-file .env -v /container/mount/folder/:/machine/folder/to/mount/ -it <container_name>`
4. Do dev work, experiments etc. 