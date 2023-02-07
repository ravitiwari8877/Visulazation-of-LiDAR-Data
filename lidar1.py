#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:01:35 2023

@author: ravitiwari
"""

# importing rewuired Lib

import numpy as np
import open3d as o3d
import laspy

# Reading the .las file using .read() inbuilt method of laspy

las = laspy.read('/Users/ravitiwari/Downloads/Lidar/Dataset/points.las')

# Extracting feature from the .las file

features =list(las.point_format.dimension_names)

print(features)

'''We have X, Y, and Z for the point data, intensity, classification, 
GPS time, and some other essential dimensions'''

# Let check what type of data they store
print("X - Cooridinate: ",las.X)
print("Y- Cooridinate: ",las.Y)
print("Z - Cooridinate: ",las.Z)

print("Intensity: ",las.intensity)

print("GPS Time: ", las.gps_time)

'''Classification is another essential dimension that you can call with 
las.classification that will provide an array of numbers.'''

print(set(list(las.classification)))

'''Ok In our case, we have {1, 2, 7, 9, 10, 12, 13} , 7 classification in the las file. 
1 = Unassigned
2 = Ground
7 = Low Point
9 = Water
10 = Rail
12 = Reserved / Overlap
13 =Wire - Guard (Shield)
'''

# Creating, Filtering, and Writing Point Cloud Data
'''To create 3D point cloud data, we can stack together with the X, Y, and Z dimensions, using Numpy'''
point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))
print(point_data)


#3D Point Cloud Visualization
'''Laspy has no visualization methods so that we will use the open3d library. 
We first create the open3D geometries and pass the point data we have created earlier'''

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])



