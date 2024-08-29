# Optimization and Ray-Tracing Algorithm

## Description
This program is designed for optimization and ray-tracing algorithms. It is developed in Python within a Jupyter Notebook environment. The Python used when developing is Python 3.8.

The folder *data* contains examples of the ray-tracing algorithms result. This folder is also used as a processing path. The input is in folder *LMC_raw* and the result is in folder *LMC_rayTracing*.

Folder *Python* contains custom libraries and dependency files required to build and run the script.

## Explanation for the files
Here is a brief explanation regarding the files inside the folder:
1. *LMC_optimization.ipynb*\
This script processes the optimization of multiple LMCs placement. It uses *Static.txt* file as input. It will run the Monte Carlo simulation to find optimal configurations. Its output is the coordinates of each LMC and *report.log* file.
2. *LMC_Trial_rayTracing.ipynb*\
This script calculates the visibility value for each frame of LMC data. Its input is interpolated LMC data and its output is LMC data with visibility value.
3. *report.log*\
This is a report file after running the *LMC_optimization.ipynb* script. It contains a summary of the process.
4. *Static.txt*\
This file contains a reference hand pose that is used for optimization. It is used in *LMC_optimization.ipynb* as an input.