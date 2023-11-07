## Simple Dockerfile

# Use the official Ubuntu runtime as a parent image
FROM ubuntu:20.04
# Update system
RUN apt-get update

# Install Python
RUN apt-get install -y python3 pip
RUN pip install rich

# Add a script to the image
RUN mkdir /app
COPY helloworld.py /app/helloworld.py

RUN chmod +x /app/helloworld.py

# Run the script when the container launches
CMD ["/bin/bash"]
