FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy input file to the container
COPY input.txt /app/input.txt

# Install basic utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Set default command
CMD ["/bin/bash"]
