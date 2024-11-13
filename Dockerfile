# Use an official Python runtime as a parent image (lightweight)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Copy the momentum notebook into the container
COPY momentum_notebook.ipynb /app/

# Install any necessary packages outlined in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Start Jupyter Notebook server (shutdown after 1h)
CMD ["sh", "-c", "jupyter notebook --ip=127.0.0.1 --port=8888 --no-browser --allow-root --NotebookApp.shutdown_no_activity_timeout=3600 /app/momentum_notebook.ipynb"]



