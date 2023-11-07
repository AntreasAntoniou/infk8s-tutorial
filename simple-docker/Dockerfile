## Simple Dockerfile

# Use the official Ubuntu runtime as a parent image
FROM ubuntu:20.04

# Update system
RUN apt-get update

# Install Python
RUN apt-get install -y python3 pip
RUN pip install rich

# Add a script to the image
COPY helloworld.py /

# Run the script when the container launches
CMD ["python3", "/helloworld.py"]
