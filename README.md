# cross-sectional momentum optimal look back

This project aims to explore cross-sectional momentum strategies in different equity markets in order to identify the best lookback period. Further it incorporates several robustness checks to solidify the results.

Testing various lookback periods, we find that in line with Jegadeesh and Titman (1993), the best performing lookback windows are indeed around the 9-12 month lookback thresholds. Specifically we find that a lookback window of ten months achieves the highest total return (13.05\%) and also the highest Sharpe Ratio of 0.53. Compared to the benchmark achieving a total return of 8.16\% and a Sharpe Ratio of 0.33, we find a significant positive outperformance in our chosen time frame. Further, we find some evidence of the mentioned long-term reversal of momentum strategies, in such a magnitude that some longer lookbacks such as 14, 20 and 23 even underperform the benchmark, as can be seen in the figure below. However there seems not to be a consistent pattern in the sense of the longer the lookback the worse is the performance and hence this leaves room for further research.

The interested reader however is invited to launch the notebook to investigate different time frames and examine the complete code. Additionally, one can compile the report and presentation in order to get a more in depth look into the overall results. Finally, through the notebook one can access an interactive dash app in order to compare the different lookback strategies to the benchmark and toggle between including or excluding transaction costs, in order to get a better feel for the results.

![main_result](reports/figures/fig_bm.png)

We encourage researchers to further develop this project by investigating the conncetion between long-term value interaction with momentum as the reason for the momentum reversal effect, first pointed out by Nagel (2001).

# Installation Guide

This project contains code to:
1. Analyze momentum strategies step-by-step in a jupyter notebook
2. Run an interactive Dash app for exploring NAV visualizations
3. Summarize the results and generate a report and a presentation in LaTeX

## Prerequisites
Ensure Docker is installed on your local machine and that it is running:
- Docker (latest version): [Install Docker](https://docs.docker.com/get-docker/)

## Terminal Instructions
first, clone this project to your local machine using:
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

fourth, compile the report using:
```bash
docker run -it --rm -v $(pwd)/reports/paper:/app/reports/paper project_momentum \
"pdflatex -output-directory=/app/reports/paper /app/reports/paper/momentum_report.tex && \
cd /app/reports/paper && bibtex momentum_report && \
pdflatex -output-directory=/app/reports/paper /app/reports/paper/momentum_report.tex && \
pdflatex -output-directory=/app/reports/paper /app/reports/paper/momentum_report.tex"
```

fifth, compile the beamer presentation using:\
(Note to press enter if you encounter a ? during the compilation process in order to skip warnings.)
```bash
docker run -it --rm -v $(pwd)/reports/presentation:/app/reports/presentation project_momentum \
"pdflatex -output-directory=/app/reports/presentation /app/reports/presentation/momentum_presentation.tex && \
pdflatex -output-directory=/app/reports/presentation /app/reports/presentation/momentum_presentation.tex && \
pdflatex -output-directory=/app/reports/presentation /app/reports/presentation/momentum_presentation.tex"
```

sixth, launch the jupyter notebook for an interactive walk through using:
```bash
docker run -it --rm -p 127.0.0.1:8888:8888 -p 127.0.0.1:8061:8061 -v $(pwd):/app project_momentum \
"jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"
```
and access the notebook for a walk through, by copying the full URL (including the token) from the terminal and paste it into your browser of choice.
The URL will look like this:    http://127.0.0.1:8888/tree?token=<TOKEN>

### Trouble shooting
- If you rerun the code multiple times, make sure that your previous docker container is closed, otherwise the port for the jupyter notebook will be occupied. Same goes for the host server. Further make sure the directory does not already exist in the folder you try to clone the repository into.



## Project Organization
<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

```
├── LICENSE                                 <- Open-source license
├── README.md                               <- The top-level README for users, including short summary of the project
├── data
│   ├── processed                           <- The processed dataframes are stored in this folder
│   └── raw                                 <- The original data pulled from the Yfinance API is stored in this folder
│
├── requirements.txt                        <- The requirements file for reproducing the analysis environment
│
├── momentum_notebook.ipynb                 <- A walk-through notebook to explore the data analysis step-by-step
│
├── Dockerfile                              <- Dockerfile containing setup to run whole project through docker implementation
│
├── reports                                 <- Generated analysis in PDF, LaTeX, etc.
     │
     ├── paper                              <- Academic-style paper
     │   ├── figures                        <- Figures used in the LaTeX report
     │   ├── momentum_report.tex            <- LaTex code in order to compile PDF report
     │   └── references.bib                 <- References used in the report
     │
     └── presentation                       <- Short presentation with most important findings
         ├── figures                        <- Figures used in the LaTeX report
         └── momentum_presentation.tex      <- LaTex code in order to compile PDF presentation
```

--------

