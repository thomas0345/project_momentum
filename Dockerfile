# Use an official Python runtime as a parent image (lightweight)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for Python and LaTeX
RUN apt-get update && apt-get install -y \
    texlive-full \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the openout_any policy to allow LaTeX to write output files anywhere
ENV openout_any=a

# Copy the entire folder structure into the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose ports for Jupyter
EXPOSE 8888

# Default to show usage instructions
CMD ["echo", "Usage: docker run <options> <command>. Available commands: paper, presentation, jupyter"]

# Define entrypoints for tasks
ENTRYPOINT ["/bin/bash", "-c"]
