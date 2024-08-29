# Multiple Leap Motion Controller Acquistion Program

## Description
This is the program to acquire data from multiple Leap Motion Controller (LMC) and to interpolate the acquired data.
Written in C++ language and built using CMake. It is developed using VSCode with MSVC Compiler from MSVisual Studio Community 2022 within Windows 11 environment.

The folder *data* contains examples of recorded data and processed results from the experiments. It has LMC data recorded in initial (naiv) placement and results from the interpolation process. This folder is also used as a processing path.

Folder *ext_lib, include, and lib* contains external libraries and dependency files required to build and run the code.

Folder *src* contains the code of this project.

## Explanation for each code
In folder *src* there are three *.cpp files* and one *CMakeLists.txt* file. Start building the binary using CMake from this folder by configuring the *CMakeLists.txt*. Here is brief explanation regarding the *.cpp files*:
1. *MultiDeviceSampleCPP.cpp*\
This code is needed for the initial build when configuring CMakelists.txt. It will generate the required dependencies to run the hand tracking application. 
2. *MultiLMC_Plot.cpp*\
This code is for tracking the hand and acquiring the marker of the hand. The output from this code is raw LMC data.
3. *MultiLMC_Interpolate.cpp*\
This code is for interpolating raw LMC data in order to get a 100Hz sampling rate. Its input is raw LMC data and its output is interpolated LMC data.

## External Library
This code uses external libraries with their own corresponding purpose:

    Ultraleap : SDK for hand tracking and acquiring the hand data from multiple LMCs.
    Freeglut  : Library for hand-tracking visualization using OpenGL.
    ALGLIB    : Library for interpolation calculation of LMC data.
