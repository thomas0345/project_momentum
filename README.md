# project_momentum

This project aims to explore momentum strategies in different equity markets in order to identify the best lookback period. Further it incorporates several robustness checks to solidify the results.

# Installation Guide

Before running through the following lines in the terminal, make sure docker is installed on your local machine from which you are accessing this project.

first, clone this project to the local machine using:
```bash
git clone https://github.com/thomas0345/project_momentum.git
```

second, navigate to the project folder using:
```bash
cd project_momentum
```

third, build a docker image for the project using:
```bash
docker build -t project_momentum .
```

fourth, run the docker container using:
```bash
docker run -it --rm -p 127.0.0.1:8888:8888 project_momentum
```

fifth, access the report, by using:
```bash
docker run -it --rm -p 127.0.0.1:8888:8888 -v $(pwd)/reports/paper:/app/reports/paper project_momentum
```

fifth, access the notebook for a walk through, by copying the full URL (including the token) from the terminal and paste it into your browser of choice.
The URL will start like this:    http://127.0.0.1:8888/tree?token=

Organization still needs to be finalized!

## Project Organization
<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

```
├── LICENSE            <- Open-source license
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         project_momentum and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── project_momentum   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes project_momentum a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

