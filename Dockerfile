# Pull base image
FROM resin/rpi-raspbian:wheezy
MAINTAINER Ralph Marschall <marschallralph@gmail.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
	gcc \
    python \
    python-dev \
    python-pip \
    #python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Copy required files
COPY ServoBlaster /app
COPY requirements.txt /app
COPY web /app

# Define working directory
WORKDIR /app

# Install Python packages
RUN pip install -r requirements.txt

# Add RPIO manually, because it can only be installed on the Raspberry Pi,
# unlike the requirements.txt which can be run everywhere.
RUN pip install rpio


# Install ServoBlaster user deamon
# TODO

# Run Flask App
# TODO

# Define default command
CMD ["bash"]