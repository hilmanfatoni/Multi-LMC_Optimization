#ifndef MULTILMC_PROCESS_H
#define MULTILMC_PROCESS_H

#include <cstdint>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <string>

struct HAND_VECTOR {
  float x;
  float y;
  float z;
};

struct HandData {
  uint32_t device_id;
  int64_t frame_id;
  float framerate;
  int64_t timestamp;  
  uint32_t nHands;
  
  HAND_VECTOR PositionData[30];

  /*
  1. Palm Position
  2. Palm Normal
  3. Palm Direction
  4. Arm Proximal
  5. Arm Distal
  6. Thumb (5) : 1. Metacarpals Prev Joint, 2. Metacarpals Next Joint 
      3. Proximal Phalanges Next Joint, 4. Intermediate Phalanges Next Joint,
      5. Distal Phalanges Next Joint. 
  7. Index Finger (5) : 1. Metacarpals Prev Joint, 2. Metacarpals Next Joint 
      3. Proximal Phalanges Next Joint, 4. Intermediate Phalanges Next Joint, 
      5. Distal Phalanges Next Joint.
  8. Middle Finger (5) : 1. Metacarpals Prev Joint, 2. Metacarpals Next Joint 
      3. Proximal Phalanges Next Joint, 4. Intermediate Phalanges Next Joint, 
      5. Distal Phalanges Next Joint.
  9. Ring Finger (5) : 1. Metacarpals Prev Joint, 2. Metacarpals Next Joint 
      3. Proximal Phalanges Next Joint, 4. Intermediate Phalanges Next Joint, 
      5. Distal Phalanges Next Joint.
  10. Little Finger (5) : 1. Metacarpals Prev Joint, 2. Metacarpals Next Joint 
      3. Proximal Phalanges Next Joint, 4. Intermediate Phalanges Next Joint, 
      5. Distal Phalanges Next Joint.
  */   
};

//Initilization of writing data to file for each device, return filepath in std::str
std::ofstream initSaveFile(std::string project_path,  int numDevice);

//Function to save data of each device.
void SaveDataDevice(std::ofstream &fileDevice, HandData HandData);

//calculate vector from coodinates (a, b : coordinate)
HAND_VECTOR VectCalc(HAND_VECTOR a, HAND_VECTOR b);

//calculate result of dot product from vector (a, b : vector) / coordinates 
//with base from center (0,0,0)
float VectDotProd(HAND_VECTOR a, HAND_VECTOR b);

//calculate result of cross product from vector (a, b : vector) / coordinates 
HAND_VECTOR VectCrossProd(HAND_VECTOR a, HAND_VECTOR b);

//calculate magnitude of vector from coordinates (A, B : coordinate)
float MagVect_Coord(HAND_VECTOR a, HAND_VECTOR b);

//calculate degree from Coordinate (a, b, c : coordinate) 
float DegCalc_Coord(HAND_VECTOR a, HAND_VECTOR b, HAND_VECTOR c);

//calculate degree from Coordinate 4 point (a, b, c, d : coordinate)
float DegCalc_Coord4point(HAND_VECTOR a, HAND_VECTOR b, HAND_VECTOR c, HAND_VECTOR d);

//calculate magnitude of vector (a : vector)
float MagVect(HAND_VECTOR a);

//calculat unit vector (a : vector)
HAND_VECTOR VectUnit(HAND_VECTOR a);

//calculate degree from vector (a, b : vector)
float DegCalc_Vect(HAND_VECTOR a, HAND_VECTOR b);

float wristflex_angle(HAND_VECTOR a, HAND_VECTOR b, HAND_VECTOR c, HAND_VECTOR d);

float wristflex_angle2(HAND_VECTOR a, HAND_VECTOR b, HAND_VECTOR c);

float wristdev_angle(HAND_VECTOR a, HAND_VECTOR b, HAND_VECTOR c, HAND_VECTOR d);

float elbowpronation(HAND_VECTOR a, HAND_VECTOR b);

float elbowflex(HAND_VECTOR a, HAND_VECTOR b);

void angle_calc(HandData handdata, float angle[5], float wrist_angle[2], float elbow_angle[2]);

void RadtoDeg(float radians[5], float degrees[5]);

int SendCmd(float AngleData);

int SendCmdThumb(float AngleData);

int SendCmdThumbAb(float AngleData);

void ProcessUDP(float UDP_angle[9], float angle[5], float wrist_angle[2], float elbow_angle[2]);

#endif