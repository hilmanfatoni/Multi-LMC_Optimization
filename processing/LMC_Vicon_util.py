import numpy as np
import plotly.graph_objects as go
import os
import warnings

# Read from VICON trc file
def readFile_trc(filepath):
  '''
    marker_xyz = [len timeseries, num markers, x, y, z]
  '''
  dr_flag = False # datarate flag in next line = False
  xyz_cntr = 0

  marker_xyz = []
  timeseries = []
  frameseries = []
  markerList = []
  DataRate = None
  Units = None
  info_header = None
  info_data = None

  with open(filepath) as f:
    lines = f.readlines()

    for l, line in enumerate(lines):
      if 'DataRate' in line:
        info_header = line.split()
        dr_flag = True
        continue
      elif 'Frame#' in line and 'Time' in line:
        temp = line.split()
        markerList = temp[2:] # 0 frame#, 1 Time
        xyz_cntr += 1
        continue

      if dr_flag == True: # flag was set in previous line
        info_data = line.split()
        DataRate = float(info_data[0])
        Units = info_data[info_header.index('Units')]
        dr_flag = False

      if xyz_cntr >= 4:
        temp = line.split()
        if len(temp) > 0:
          frameseries.append(temp[0])
          timeseries.append(temp[1])
          marker_xyz.append([float(t) if 'Nan' not in t else np.nan for t in temp[2:]])

      xyz_cntr += 1 # jump X1, X2, Z1 ... line, or empty line afterwards

    marker_xyz = np.array(marker_xyz)
    marker_xyz[np.where(np.isnan(marker_xyz))] = np.nan
    marker_xyz = marker_xyz.reshape(marker_xyz.shape[0], int(marker_xyz.shape[1]/3), 3)

    data_dict = {}
    data_dict['time'] = timeseries
    data_dict['frame'] = frameseries
    data_dict['info_header'] = info_header
    data_dict['info_data'] = info_data
    data_dict['DataRate'] = DataRate
    data_dict['Units'] = Units
    data_dict['markerList'] = markerList
    data_dict['marker_xyz'] = marker_xyz

    for mi, mn in enumerate(markerList):
      data_dict[mn] = marker_xyz[:, mi, :]

  return markerList, marker_xyz, timeseries, frameseries, DataRate, data_dict


### pos_markers is only marker ndarray 
def plot_hand(fig, pos_markers, color='blue', names=np.arange(0, 30)):
  # omit marker palm normal and palm direction (marker 1 and 2)
  pos_markers = pos_markers[[0] + [i for i in range (3,30)], : ]
  
  lineplot_order =  [1, 2, 3, 4, 5, 6, 7, 6, 5, 9, 10, 11, 12, 11, 10, 9, 14, 15, 16, 17, 16, 15 ,14, 19, 20, 21, 22, 21, 20, 19, 24, 25, 26, 27, 26, 25, 24, 
                     23, 18, 13, 8, 3, 2, 23]
  pos_markers = pos_markers[lineplot_order]

  if fig is None:
    fig = go.Figure()
  fig.add_trace(go.Scatter3d(
    x=pos_markers[:, 0],
    y=pos_markers[:, 1],
    z=pos_markers[:, 2],
    mode='markers+lines',

    marker=dict(
        size=5,
        color=color,
    )
  ))

  fig.update_layout(
    width=1024,
    height=512,
    scene = dict(
      xaxis=dict(),
      yaxis=dict(),
      zaxis=dict(),

      aspectmode='data', #this string can be 'data', 'cube', 'auto', 'manual'
      #a custom aspectratio is defined as follows:
      
      aspectratio=dict(x=1, y=1, z=1)
    ),

    scene_camera = dict(
      up=dict(x=0, y=20, z=0),
      center=dict(x=0, y=0, z=0),
      eye=dict(x=-2, y=3, z=-0.5)
    )
  )

  return fig

def plot_hand_4LMC(fig, pos_markers1, pos_markers2, pos_markers3, pos_markers4):
  # omit marker palm normal and palm direction (marker 1 and 2)
  pos_markers1 = pos_markers1[[0] + [i for i in range (3,30)], : ]
  pos_markers2 = pos_markers2[[0] + [i for i in range (3,30)], : ]
  pos_markers3 = pos_markers3[[0] + [i for i in range (3,30)], : ]
  pos_markers4 = pos_markers4[[0] + [i for i in range (3,30)], : ]
    
  lineplot_order =  [1, 2, 3, 4, 5, 6, 7, 6, 5, 9, 10, 11, 12, 11, 10, 9, 14, 15, 16, 17, 16, 15 ,14, 19, 20, 21, 22, 21, 20, 19, 24, 25, 26, 27, 26, 25, 24,
                       23, 18, 13, 8, 3, 2, 23]
  pos_markers1 = pos_markers1[lineplot_order]
  pos_markers2 = pos_markers2[lineplot_order]
  pos_markers3 = pos_markers3[lineplot_order]
  pos_markers4 = pos_markers4[lineplot_order]

  if fig is None:
    fig = go.Figure()
  fig.add_trace(go.Scatter3d(
    x=pos_markers1[:, 0],
    y=pos_markers1[:, 1],
    z=pos_markers1[:, 2],
    mode='markers+lines',
    marker=dict(
        size=5,
        color="red",
    ),
    name = "LMC1"
  ))

  fig.add_trace(go.Scatter3d(
    x=pos_markers2[:, 0],
    y=pos_markers2[:, 1],
    z=pos_markers2[:, 2],
    mode='markers+lines',
    marker=dict(
        size=5,
        color="blue",
    ),
    name = "LMC2"
  ))


  fig.add_trace(go.Scatter3d(
    x=pos_markers3[:, 0],
    y=pos_markers3[:, 1],
    z=pos_markers3[:, 2],
    mode='markers+lines',
    marker=dict(
        size=5,
        color="green",
    ),
    name = "LMC3"
  ))

  fig.add_trace(go.Scatter3d(
    x=pos_markers4[:, 0],
    y=pos_markers4[:, 1],
    z=pos_markers4[:, 2],
    mode='markers+lines',
    marker=dict(
        size=5,
        color="black",
    ),
    name = "LMC4"
  ))
  
  fig.update_layout(
    width=1024,
    height=512,
    scene = dict(
      xaxis=dict(),
      yaxis=dict(),
      zaxis=dict(),            
      aspectmode='data', 
      aspectratio=dict(x=1, y=1, z=1)
    ),
    scene_camera = dict(
      up=dict(x=0, y=20, z=0),
      center=dict(x=0, y=0, z=0),
      eye=dict(x=-2, y=3, z=-0.5)
    )
  )

  return fig

def plot_hand_interactive(pos_markers, position):
  fig = go.Figure()
  plot_hand(fig, pos_markers[position], names=np.arange(0, pos_markers.shape[0]))
  fig.show()

def plot_hand_interactive_4LMC(pos_markers1, pos_markers2, pos_markers3, pos_markers4, position):
  fig = go.Figure()
  plot_hand_4LMC(fig, pos_markers1[position], pos_markers2[position], pos_markers3[position], pos_markers4[position])
  fig.show()

# create transformation matrix
def create_transformation_matrix(config):
  x = config [0]
  y = config [1]
  z = config [2]
  pitch = config [3] * np.pi/180
  roll = config [4] * np.pi/180
  yaw = config [5] * np.pi/180

  """
  Create a 4x4 transformation matrix based on position and orientation.
  Arguments:
  x, y, z : float : Position coordinates
  pitch, roll, yaw : float : Rotation angles (in radians) around X, Y, Z axes respectively
  Returns:
  numpy.ndarray : Transformation matrix
  """
  # Define rotation matrices for each axis
  Rx = np.array([[1, 0, 0],
                  [0, np.cos(pitch), -np.sin(pitch)],
                  [0, np.sin(pitch), np.cos(pitch)]])

  Ry = np.array([[np.cos(roll), 0, np.sin(roll)],
                  [0, 1, 0],
                  [-np.sin(roll), 0, np.cos(roll)]])

  Rz = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                  [np.sin(yaw), np.cos(yaw), 0],
                  [0, 0, 1]])

  # Combine rotation matrices
  rotation_matrix = np.matmul(Rz, np.matmul(Ry, Rx)) #first
  rotation_matrix_homogeneous = np.vstack([rotation_matrix, [0, 0, 0]])
  rotation_matrix_homogeneous = np.hstack([rotation_matrix_homogeneous, [[0], [0], [0], [1]]])

  # Create translation matrix
  translation_matrix = np.array([[1, 0, 0, x],
                                  [0, 1, 0, y],
                                  [0, 0, 1, z],
                                  [0, 0, 0, 1]])

  transformation_matrix = np.matmul(translation_matrix, rotation_matrix_homogeneous)

  return transformation_matrix

def create_rotation_matrix(config):
  x = config [0]
  y = config [1]
  z = config [2]
  pitch = config [3] * np.pi/180
  roll = config [4] * np.pi/180
  yaw = config [5] * np.pi/180

  """
  Create a 4x4 transformation matrix based on position and orientation.
  Arguments:
  x, y, z : float : Position coordinates
  pitch, roll, yaw : float : Rotation angles (in radians) around X, Y, Z axes respectively
  Returns:
  numpy.ndarray : Transformation matrix
  """
  # Define rotation matrices for each axis
  Rx = np.array([[1, 0, 0],
                  [0, np.cos(pitch), -np.sin(pitch)],
                  [0, np.sin(pitch), np.cos(pitch)]])

  Ry = np.array([[np.cos(roll), 0, np.sin(roll)],
                  [0, 1, 0],
                  [-np.sin(roll), 0, np.cos(roll)]])

  Rz = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                  [np.sin(yaw), np.cos(yaw), 0],
                  [0, 0, 1]])

  # Combine rotation matrices
  rotation_matrix = np.matmul(Rz, np.matmul(Ry, Rx)) #first
  rotation_matrix_homogeneous = np.vstack([rotation_matrix, [0, 0, 0]])
  rotation_matrix_homogeneous = np.hstack([rotation_matrix_homogeneous, [[0], [0], [0], [1]]])

  return rotation_matrix_homogeneous

def create_translation_matrix(config):
  x = config [0]
  y = config [1]
  z = config [2]
  pitch = config [3] * np.pi/180
  roll = config [4] * np.pi/180
  yaw = config [5] * np.pi/180

  # Create translation matrix
  translation_matrix = np.array([[1, 0, 0, x],
                                  [0, 1, 0, y],
                                  [0, 0, 1, z],
                                  [0, 0, 0, 1]])

  return translation_matrix

# converting vicon marker to lmc marker sequence
# arg only marker_xyz, return marker only in LMC format sequence
def convert_vicon_to_lmc(posmarker):
  vicon_converted = np.zeros((posmarker.shape[0],30,3))

  vicon_converted [:,0] = posmarker[:,6]  #palm
  vicon_converted [:,3] = posmarker[:,0]  #arm proximal / elbow
  vicon_converted [:,4] = (posmarker[:,1] + posmarker[:,2]) / 2 #arm distal / wrist

  ### thumb ###
  vicon_converted [:,5] = posmarker[:,4]
  vicon_converted [:,6] = posmarker[:,4]
  for i in range(7,10):
    vicon_converted [:,i] = posmarker[:,i]

  ### index ###
  vicon_converted [:,10] = posmarker[:,5]
  for i in range(11,15):
    vicon_converted [:,i] = posmarker[:,i-1]

  ### middle ###
  # finding points 1/3 between index and little
  vicon_converted [:,15] = posmarker[:,5] + ((posmarker[:,3] - posmarker[:,5]) * 0.33)
  for i in range(16,20):
    vicon_converted [:,i] = posmarker[:,i-2]

  ### ring ###
  # finding points 2/3 between index and little
  vicon_converted [:,20] = posmarker[:,5] + ((posmarker[:,3] - posmarker[:,5]) * 0.66)
  for i in range(21,25):
    vicon_converted [:,i] = posmarker[:,i-3]

  ### little ###
  vicon_converted [:,25] = posmarker[:,3]
  for i in range(26,30):
    vicon_converted [:,i] = posmarker[:,i-4]

  return vicon_converted

## Alignment
def alignment (posmarker, trans_matrix):
  ids = [1, 2, 3, 4]

  for id_val in ids:
    for i in range(posmarker.shape[1]):
      temp = posmarker[id_val-1,i]
      column_of_ones = np.ones((posmarker.shape[2], 1), dtype=posmarker.dtype)
      temp = np.hstack((temp, column_of_ones))
      for j in range(posmarker.shape[2]):
        temp [j,:] = np.matmul(trans_matrix[id_val-1],temp [j,:])

      posmarker[id_val-1,i] = temp [:,0:3]

  return posmarker

# calculate angle from four 3D points or two lines
def calculate_angle_from4point (p1, p2, p3,p4):
  p12_vect = p2 - p1
  p34_vect = p4 - p3
  p12_mag = np.sqrt(np.sum((p2 - p1)**2))
  p34_mag = np.sqrt(np.sum((p4 - p3)**2))

  divider = p12_mag * p34_mag
  if (divider == 0):
    angle = 0
  else:
    val = (np.matmul(p12_vect , p34_vect)) / divider
    angle = np.degrees(np.arccos(val))
  return angle

# calculate length and angle from hand markers
def calculate_length_angle (posmarker):
  finger_length = np.zeros ((posmarker.shape[0],5))
  segment_length = np.zeros ((posmarker.shape[0],14))
  angle_joint = np.zeros ((posmarker.shape[0],6))
  index_joint = np.zeros ((posmarker.shape[0],3))
  thumb_joint = np.zeros ((posmarker.shape[0],2))
  wrist_joint = np.zeros ((posmarker.shape[0],1))

  for i in range(0,posmarker.shape[0]):
    # thumb segment length: intermediate phalanges, distal phalanges
    segment_length [i,0] = np.sqrt(np.sum((posmarker[i,8] - posmarker[i,7])**2))
    segment_length [i,1] = np.sqrt(np.sum((posmarker[i,9] - posmarker[i,8])**2))
    # index segment length: proximal phalanges, intermediate phalanges, distal phalanges
    segment_length [i,2] = np.sqrt(np.sum((posmarker[i,12] - posmarker[i,11])**2))
    segment_length [i,3] = np.sqrt(np.sum((posmarker[i,13] - posmarker[i,12])**2))
    segment_length [i,4] = np.sqrt(np.sum((posmarker[i,14] - posmarker[i,13])**2))
    # middle segment length: proximal phalanges, intermediate phalanges, distal phalanges
    segment_length [i,5] = np.sqrt(np.sum((posmarker[i ,17] - posmarker[i ,16])**2))
    segment_length [i,6] = np.sqrt(np.sum((posmarker[i ,18] - posmarker[i ,17])**2))
    segment_length [i,7] = np.sqrt(np.sum((posmarker[i ,19] - posmarker[i ,18])**2))
    # ring segment length: proximal phalanges, intermediate phalanges, distal phalanges
    segment_length [i,8] = np.sqrt(np.sum((posmarker[i ,22] - posmarker[i ,21])**2))
    segment_length [i,9] = np.sqrt(np.sum((posmarker[i ,23] - posmarker[i ,22])**2))
    segment_length [i,10] = np.sqrt(np.sum((posmarker[i ,24] - posmarker[i ,23])**2))
    # little segment length: proximal phalanges, intermediate phalanges, distal phalanges
    segment_length [i,11] = np.sqrt(np.sum((posmarker[i ,27] - posmarker[i ,26])**2))
    segment_length [i,12] = np.sqrt(np.sum((posmarker[i ,28] - posmarker[i ,27])**2))
    segment_length [i,13] = np.sqrt(np.sum((posmarker[i ,29] - posmarker[i ,28])**2))

    # thumb length
    finger_length [i,0] = segment_length [i,0] + segment_length [i,1]
    # index length
    finger_length [i,1] = segment_length [i,2] + segment_length [i,3] + segment_length [i,4]
    # middle length
    finger_length [i,2] = segment_length [i,5] + segment_length [i,6] + segment_length [i,7]
    # ring length
    finger_length [i,3] = segment_length [i,8] + segment_length [i,9] + segment_length [i,10]
    # little
    finger_length [i,4] = segment_length [i,11] + segment_length [i,12] + segment_length [i,13]

    #index MCP
    index_joint[i,0] = calculate_angle_from4point(posmarker[i,10],posmarker[i,11],posmarker[i,11],posmarker[i,12])
    #index PIP
    index_joint[i,1] = calculate_angle_from4point(posmarker[i,11],posmarker[i,12],posmarker[i,12],posmarker[i,13])
    #index DIP
    index_joint[i,2] = calculate_angle_from4point(posmarker[i,12],posmarker[i,13],posmarker[i,13],posmarker[i,14])
    #thumb MCP
    thumb_joint[i,0] = calculate_angle_from4point(posmarker[i,6],posmarker[i,7],posmarker[i,7],posmarker[i,8])
    #thumb DIP
    thumb_joint[i,1] = calculate_angle_from4point(posmarker[i,7],posmarker[i,8],posmarker[i,8],posmarker[i,9])
    #wrist joint
    wrist_joint[i,0] = calculate_angle_from4point(posmarker[i,3],posmarker[i,4],posmarker[i,4],posmarker[i,0])

  angle_joint [:,0:3] = index_joint [:,0:3]
  angle_joint [:,3:5] = thumb_joint [:,0:2]
  angle_joint [:,5] = wrist_joint [:,0]

  return finger_length, angle_joint, segment_length

def calculate_visibility(LMC_visib):
  ids = [1, 2, 3, 4]
  visibility = np.zeros((4,4,5))

  for id_val in ids:
    # range of thumb, index, middle, ring, and little
    for i in range (0,5): 
      visibility[id_val-1,0,i] = np.count_nonzero(LMC_visib[id_val-1,:,i] == -1, axis=0)
      visibility[id_val-1,1,i] = np.count_nonzero(LMC_visib[id_val-1,:,i] == 0, axis=0)
      visibility[id_val-1,2,i] = np.count_nonzero(LMC_visib[id_val-1,:,i] == 1, axis=0)
      ''' visibility row 4 : 
        value = -1 : hand not detected
        value = 0 : detected but all from model, not truly detected
        0 < value <= 1 : true detected rate
      '''
      if (not visibility[id_val-1,1,i]==0 or not visibility[id_val-1,2,i]==0) :
        visibility[id_val-1,3,i] = visibility[id_val-1,2,i] / (visibility[id_val-1,1,i] + visibility[id_val-1,2,i])
      else :
        visibility[id_val-1,3,i] = -1 # hand not detected
  
  return visibility

'''KALMAN FILTER ALGORITHM'''
import pandas as pd

def init_kalman(x, y):
  x[0,0] = y
  x[1,0] = 0
  p = [[100,0],[0,300]]
  return x, p

def prediction(x, p, q, f):
  x = np.matmul(f,x)
  p = np.matmul(np.matmul(f,p),np.transpose(f))+q
  return x, p

def update(x, p, y, r, h):
  # suppress runtimewarning because the calculation of nan value
  warnings.filterwarnings("ignore", category=RuntimeWarning)
  Inn = y - np.matmul(h,x)
  S = np.matmul(np.matmul(h,p),np.reshape(h,(2,1)))+r
  K = np.matmul(p,np.reshape(h,(2,1)))/S
  
  x = x + K*Inn
  p = p - np.matmul(np.multiply(K,h),p)
  return x, p

def generate_signal(signal):

  var = signal.rolling(window=30, center=True, min_periods=1).var()
  
  data = {'signal': np.array(signal),
      'var': np.reshape(var,len(var))}
  
  s = pd.DataFrame(data, columns = ['signal', 'var'])
  return s

def fuse_signals(sig1,sig2,sig3,sig4):
  # generating signal from marker of each LMC
  s1 = generate_signal(sig1)
  s2 = generate_signal(sig2)
  s3 = generate_signal(sig3)
  s4 = generate_signal(sig4)
  
  dt = 0.01
  n = len(s1)
  x = np.zeros((2,1)) #state matrix
  p = np.zeros((2,2)) #covariance matrix-
  x_arr = np.zeros((n,2)) #kalman filter output through the whole time
  q = [[0.04,0],[0,1]] #system noise
  f = [[1,dt],[0,1]] #transition matrix
  h = np.array([1,0]) #observation matrix
    
  start = False
  for i, row in s1.iterrows():             
    if (start == False) &  (not np.isnan(s1.iloc[i,0])):
      #initialize the state using the 1st sensor if not nan
      x, p = init_kalman(x, s1.iloc[i, 0]) 
      x_arr[i,:] = np.rot90(x)
      start = True
    elif (start == False) &  (not np.isnan(s2.iloc[i,0])):
      #initialize the state using the 2nd sensor if not nan
      x, p = init_kalman(x, s2.iloc[i, 0]) 
      x_arr[i,:] = np.rot90(x)
      start = True
    elif (start == False) &  (not np.isnan(s3.iloc[i,0])):
      #initialize the state using the 3rd sensor if not nan
      x, p = init_kalman(x, s3.iloc[i, 0]) 
      x_arr[i,:] = np.rot90(x)
      start = True
    elif (start == False) &  (not np.isnan(s4.iloc[i,0])):
      #initialize the state using the 4th sensor if not nan
      x, p = init_kalman(x, s4.iloc[i, 0]) 
      x_arr[i,:] = np.rot90(x)
      start = True
    elif start==True :
      x, p = prediction(x,p,q,f)

      if (not np.isnan(s1.iloc[i]).any()):
        x, p = update(x,p,s1.iloc[i,0],s1.iloc[i,1],h)
      if (not np.isnan(s2.iloc[i]).any()):
        x, p = update(x,p,s2.iloc[i,0],s2.iloc[i,1],h)
      if (not np.isnan(s3.iloc[i]).any()):
        x, p = update(x,p,s3.iloc[i,0],s3.iloc[i,1],h)
      if (not np.isnan(s4.iloc[i]).any()):
        x, p = update(x,p,s4.iloc[i,0],s4.iloc[i,1],h)
            
      # rotate to match the x_arr, x from shape (2,1) change to (1, 2)
      x_arr[i,:] = np.rot90(x)
    else :
      x_arr[i,:] = np.nan

  return x_arr


'''SAVING FILE'''
# save segment length, finger length, and angle joint (for Vicon)
def save_length_angle (savefilename, filename, finger_length, angle_joint, segment_length):
  filename = os.path.splitext(filename)[0]
  
  statistic_segment_length = np.zeros((3,14))
  statistic_finger_length = np.zeros((3,5))
  statistic_angle_joint = np.zeros((3,6))

  statistic_segment_length[0] = np.nanmin(segment_length,axis=0)
  statistic_segment_length[1] = np.nanmax(segment_length,axis=0)
  statistic_segment_length[2] = np.nanmean(segment_length,axis=0)
  statistic_finger_length[0] = np.nanmin(finger_length,axis=0)
  statistic_finger_length[1] = np.nanmax(finger_length,axis=0)
  statistic_finger_length[2] = np.nanmean(finger_length,axis=0)
  statistic_angle_joint[0] = np.nanmin(angle_joint, axis=0)
  statistic_angle_joint[1] = np.nanmax(angle_joint, axis=0)
  statistic_angle_joint[2] = statistic_angle_joint[1] - statistic_angle_joint[0]

  with open((savefilename+".txt"), "a") as file:
    file.write("________________________________________________________________________VICON Data________________________________________________________________________\n")
    file.write("Filename:\t" + filename + "\n")
    file.write("Segment Length (min, max, average per row) in mm\n")
    file.write("Thumb_interm\tThumb_distal\t"+
               "Index_proxi\tIndex_interm\tIndex_distal\t"+
               "Middle_proxi\tMiddle_interm\tMiddle_distal\t"+
               "Ring_proxi\tRing_interm\tRing_distal\t"+
               "Little_proxi\tLittle_interm\tLittle_distal\n")
    np.savetxt(file, statistic_segment_length, fmt="%f", delimiter="\t")
    file.write("Finger Length (min, max, average per row) in mm\n")
    file.write("Thumb\tFinger\tMiddle\tRing\tLittle\n")
    np.savetxt(file, statistic_finger_length, fmt="%f", delimiter="\t")
    file.write("Angle Joint (min, max, range of motion per row in degree)\n")
    file.write("Thumb\tFinger\tMiddle\tRing\tLittle\n")
    np.savetxt(file, statistic_angle_joint, fmt="%f", delimiter="\t")
    file.write("\n")
    file.write("\n")
  

# save segment length, finger length, angle joint, and visibility (for LMC)
def save_length_angle_visib (savefilename, filename, finger_length, angle_joint, segment_length, visibility):
  filename = os.path.splitext(filename)[0]
  
  statistic_segment_length = np.zeros((3,14))
  statistic_finger_length = np.zeros((3,5))
  statistic_angle_joint = np.zeros((3,6))

  statistic_segment_length[0] = np.nanmin(segment_length,axis=0)
  statistic_segment_length[1] = np.nanmax(segment_length,axis=0)
  statistic_segment_length[2] = np.nanmean(segment_length,axis=0)
  statistic_finger_length[0] = np.nanmin(finger_length,axis=0)
  statistic_finger_length[1] = np.nanmax(finger_length,axis=0)
  statistic_finger_length[2] = np.nanmean(finger_length,axis=0)
  statistic_angle_joint[0] = np.nanmin(angle_joint, axis=0)
  statistic_angle_joint[1] = np.nanmax(angle_joint, axis=0)
  statistic_angle_joint[2] = statistic_angle_joint[1] - statistic_angle_joint[0]

  with open((savefilename+".txt"), "a") as file:
    file.write("________________________________________________________________________LMC Data________________________________________________________________________\n")
    file.write("Filename:\t" + filename + "\n")
    file.write("Segment Length (min, max, average per row) in mm\n")
    file.write("Thumb_interm\tThumb_distal\t"+
               "Index_proxi\tIndex_interm\tIndex_distal\t"+
               "Middle_proxi\tMiddle_interm\tMiddle_distal\t"+
               "Ring_proxi\tRing_interm\tRing_distal\t"+
               "Little_proxi\tLittle_interm\tLittle_distal\n")
    np.savetxt(file, statistic_segment_length, fmt="%f", delimiter="\t")
    file.write("Finger Length (min, max, average per row) in mm\n")
    file.write("Thumb\tFinger\tMiddle\tRing\tLittle\n")
    np.savetxt(file, statistic_finger_length, fmt="%f", delimiter="\t")
    file.write("Angle Joint (min, max, range of motion per row in degree)\n")
    file.write("Thumb\tFinger\tMiddle\tRing\tLittle\n")
    np.savetxt(file, statistic_angle_joint, fmt="%f", delimiter="\t")
    file.write("\n")
    #save visibility
    file.write("Visibility LMC1\n") 
    file.write("Thumb\tFinger\tMiddle\tRing\tLittle\n")
    np.savetxt(file, visibility[0], fmt="%0.2f", delimiter="\t")
    file.write("Visibility LMC2\n") 
    file.write("Thumb\tFinger\tMiddle\tRing\tLittle\n")
    np.savetxt(file, visibility[1], fmt="%0.2f", delimiter="\t")
    file.write("Visibility LMC3\n") 
    file.write("Thumb\tFinger\tMiddle\tRing\tLittle\n")
    np.savetxt(file, visibility[2], fmt="%0.2f", delimiter="\t")
    file.write("Visibility LMC4\n") 
    file.write("Thumb\tFinger\tMiddle\tRing\tLittle\n")
    np.savetxt(file, visibility[3], fmt="%0.2f", delimiter="\t")
    file.write("\n")
    file.write("\n")
