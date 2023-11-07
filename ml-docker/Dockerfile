# Start from the official NVIDIA PyTorch image that includes all the goodies for top distributed and singla node Pytorch
FROM nvcr.io/nvidia/cuda:12.0.0-cudnn8-devel-ubuntu22.04

# Set default shell to bash
SHELL ["/bin/bash", "-c"] 

# Update system
RUN apt update
RUN apt upgrade -y

# Install favourite tools
RUN apt install aptitude wget tree -y

# Install key libraries for OpenGL
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0


# Install conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh -O ~/miniconda.sh
RUN bash ~/miniconda.sh -b -p /opt/conda

# Set the default shell command to be conda environment 'base' + bash
SHELL ["/opt/conda/bin/conda", "run", "-n", "base", "/bin/bash", "-c"]

# Create conda environment called main
RUN conda create -n main python=3.10 -y

# Set the default shell command to be conda environment 'main' + bash
SHELL ["/opt/conda/bin/conda", "run", "-n", "main", "/bin/bash", "-c"]

# Ensure conda is configured for bash and fish
RUN conda init bash
RUN conda init fish

# Install mamba on conda, which is a C++ version of conda with parallel support for installs and dependency resolution
RUN conda install -c conda-forge mamba -y

# Install favourite conda packages
RUN mamba install -c conda-forge starship fish jupyterlab git black git-lfs tmux glances gh micro bat exa -y
RUN mamba install -c conda-forge git-crypt nvitop -y

# Install PyTorch
RUN echo y | pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install git-lfs and configure credential helper
RUN git lfs install
RUN git config --global credential.helper store

# Install project being worked on, assumes we are running this from the root of the repo, modify the below to suit your package
RUN mkdir /app/
ADD requirements.txt /app/

ADD simple-ml /app/simple-ml
ADD setup.py /app/
RUN echo y | pip install -r /app/requirements.txt
RUN echo y | pip install /app/[dev]

# Start from bash when the container launches
ENTRYPOINT ["/bin/bash"]