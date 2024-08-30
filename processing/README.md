# Extracting Hand Anthropometrics Data

## Description
This program is designed to analyze the performance of placement configuration and extracting hand anthropometrics. It is also used to compare the LMC data with MMC data. It is developed in Python within a Jupyter Notebook environment. The Python used when developing is Python 3.8.

The folder *data* contains examples of the results. This folder is also used as a processing path. The input is in folder *\_process_* and the output is in folder *\_result_*.

## Explanation for the files
Here is a brief explanation regarding the files inside the folder:

1. *Extract.ipynb*\
This script analyzes the performance of placement configuration and extracting hand anthropometrics. It uses data from folder *\_process_* as an input. The inputs are from LMC and MMC. It calculates finger lengths, range of motion of fingers, and visibility rate of LMCs.
2. *LMC_Vicon_util.py*\
This script is a custom library which is used to built and run the *Extract.ipynb* notebook. It contains modified Kalman Filter to handle NaN data. The Kalman Filter is adopted from https://github.com/andrewhouston113/Multi-Leap-Motion-Setup.