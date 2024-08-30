# Multiple Leap Motion Controller and Placement Optimization

Paper Title: **Optimizing Interaction Space: Enlarging the Capture Volume for Multiple Portable Motion Capture Devices**\
Conference: **International Conference on Intelligent Robots and Systems 2024 (IROS 2024)** (accepted)\
Authors: **Muhammad Hilman Fatoni<sup>1,2,\*</sup> Christopher Herneth <sup>1,\*</sup>, Junnan Li<sup>1</sup>, Fajar Budiman<sup>1,2</sup>, Amartya Ganguly<sup>1</sup>, and Sami Haddadin<sup>1</sup>**

1\. Munich Institute of Robotics and Machine Intelligence (MIRMI), Technische Universität München (TUM), Germany.\
2\. Institut Teknologi Sepuluh Nopember (ITS), Indonesia.\
\*equal contribution

Correspondence: muhammadhilman.fatoni@tum.de

## Description
This application is designed for the acquisition of data from multiple Leap Motion Controller (LMC), optimization of LMC placements, and performance analysis by evaluating hand anthropometrics and LMC visibility against the Marker-based Motion Capture (MMC).\
The code is developed using C++ and Python language in VSCode IDE, and specially tailored for a Windows environment.

## Repository Overview
The repository is organized into several folders, each containing distinct code or scripts corresponding to different stages of the sequential workflow. Each folder includes detailed explanations of the processes involved. Below is an overview of the contents of each folder or file:
1. [**Folder .vscode**](.vscode)\
Available if you want to run all the programs using VS Code. The settings to build and run the binary from the .cpp code are written in settings.json file.
2. [**Folder multi_lmc**](multi_lmc)\
Contain code written in C++ to acquire data from multiple LMCs and to interpolate the acquired data. There are several external libraries needed to run the application. 
3. [**Folder optimization**](optimization)\
Contain script written in Python to optimize the placement configuration of multiple LMCs and to run ray-tracing algorithm for LMC Visibility calculation.
4. [**Folder processing**](processing)\
Contain script written in Python to analyze the performance of LMCs configuration placement by measuring hand anthropometrics and visibility rate of LMC.
5. **File requirements.txt**\
Contain requirement libraries used for Python development in this project. The Python script is developed using **Python 3.8**. Please use this file to generate the virtual environment.

Here is the sequential workflow to run the whole application process:
1. **LMCs Configuration Optimization**\
Utilizing the script from **Folder optimization ([LMC_optimization.ipynb](optimization/LMC_optimization.ipynb))** and an available reference pose, there will be output how the placement of multiple LMCs is configured.
2. **LMCs Data Acquisition**\
LMCs data is acquired by running the code inside **Folder multi_lmc ([MultiLMC_Plot.cpp](multi_lmc/src/MultiLMC_Plot.cpp))**. The output from the application is raw LMC data.
3. **LMCs Data Interpolation**\
Run the second code inside **Folder multi_lmc ([MultiLMC_Interpolate.cpp](multi_lmc/src/MultiLMC_Interpolate.cpp))**. It will generate interpolated LMC data.
4. **LMCs Visibility Calculation**\
Using the interpolated LMC data, run a script from **Folder optimization ([LMC_Trial_rayTracing.ipynb](optimization/LMC_Trial_rayTracing.ipynb))**. It will generate LMC data with visibility value for each frame.
5. **Analyzing**\
This folder is used to analyze the performance of placement configuration by calculating hand anthropometrics. Utilizing input from LMCs data (from step 4) and MMC data, the script inside **Folder processing ([Extract.ipynb](processing/Extract.ipynb))** will calculate the finger lengths, range of motion of fingers, and visibility rate of LMCs.

## Requirements
**Hardware**. This project used a Laptop and peripherals with these specifications:
* 11th Gen Intel(R) Core(TM) i9 processor
* 32GB RAM
* 2 USB 3.0 ports (necessary for 4LMCs)
* 2 USB extender

**Software.** Please install:
1. **Ultraleap SDK**.
This project needs Ultraleap software in order to work. It is built using Ultraleap Gemini SDK version 5.6.1. The information regarding the SDK can be found at https://leap2.ultraleap.com/downloads/leap-motion-controller/.\
Detailed explanation of how to utilize the API is decsribed at https://docs.ultraleap.com/api-reference/tracking-api/index.html. 
2. **CMake**. This project uses CMake version 3.26.
3. **MSVisual Studio Community 2022** (*recommended*). This project is built using MSVC Compiler from MSVisual Studio Community 2022. 
4. **VSCode IDE** (*recommended*). This project is developed within VSCode IDE in Windows 11 Environment. 
5. **Python**. This project is developed using Python 3.8

## Funding
This work was supported by the Federal Ministry of Education and Research of the Federal Republic of Germany (BMBF) by funding the project AI.D under Project Number 16ME0539K.\
The first author completed this work while receiving a scholarship funded by Indonesia Endowment Fund for Education (LPDP).

## Cite As:
This work is unpublished yet. Please refer to IEEE repository when published for citation.\
Paper Title: **Optimizing Interaction Space: Enlarging the Capture Volume for Multiple Portable Motion Capture Devices** 

## License
 Multiple Leap Motion Controller and Placement Optimization © 2024 is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The full license texts can be found in the [`LICENSE`](LICENSE.md) file.

 [![LICENSE](https://img.shields.io/badge/LICENSE-CC%20BY--NC--SA%204.0-0000FF?labelColor=FF0000)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

 [![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

