# Use an official Python runtime as a parent image (lightweight)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for Python and LaTeX
RUN apt-get update && apt-get install -y \
    texlive-full \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire folder structure into the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose ports for Jupyter and Dash
EXPOSE 8888 8061

# Run LaTeX report compilation first, then launch Jupyter Notebook
CMD pdflatex -output-directory=/app/reports/paper /app/reports/paper/momentum_report.tex && \
    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root /app/momentum_notebook.ipynb
