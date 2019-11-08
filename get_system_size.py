#!/usr/bin/env python
# ~*~ coding:utf-8 ~*~

"""
This allow to calculate the system size
print the cellbasis for NAMD
"""

__author__ = "Emmanuel Edouard MOUTOUSSAMY"
__version__  = "1.0.0"
__date__ = "2015/09"
__copyright__ = "CC_by_SA"
__dependencies__ = "sys, numpy"

import numpy as np
import argparse
import sys


def GetArgs():

	"""
	Get the arguments: pdb a)
	:return: arg.i = PDB and arg.d = distance from the bilayer plane
	"""
	parser = argparse.ArgumentParser(description='IBS composition Anlaysis') #Title

	parser.add_argument('-i', metavar = "pdb", type = str, help = "pdb file") #Argument for the pdb
	parser.add_argument('-w', metavar="wat", default=0, type=bool, help= "take only water molecule", required=False) #distance

	args = parser.parse_args()

	return args


def get_coord(pdb,wat):
	"""
	collect the coordinate from a PDB file
	:param pdb: a pdb file format: http://cupnet.net/pdb-format/
	:return:a numpy array containing the coordinate of your system
	"""

	flag = 0

	if wat:
		watornotwat = "TIP3"
	else:
		watornotwat = "ATOM"

	with open(pdb,"r") as input_file:
		for line in input_file:
			if line[0:4] == "ATOM" and watornotwat in line:
				x = float(line[30:38]) #get x coord
				y = float(line[38:46]) #get y coord
				z = float(line[46:54]) #get z coord

				if flag ==0:
					coord = np.array([x,y,z]) #initinialze numpy array
					flag = 1

				else:
					coord = np.vstack((coord,[x,y,z])) #numpy aray extension



	return coord


def CoordInfo(coord):
	"""
	calculate the geometrical center of the system and the system size
	:param coord: a numpy array containing the coordinate of your system
	:return: system size in X, system size in Y, system size in Z, center of geometry (COG) x,COG Y, COG Z
	"""
	argx = max(coord[:,0]) - min(coord[:,0]) #get the larger x dist
	argy = max(coord[:,1]) - min(coord[:,1]) #get the larger y dist
	argz = max(coord[:,2]) - min(coord[:,2]) #get the larger z dist

	centerx= np.mean(coord[:,0])
	centery = np.mean(coord[:,1])
	centerz = np.mean(coord[:,2])

	return argx,argy,argz,centerx,centery,centerz

if __name__ == '__main__':

	args = GetArgs()  # get arguments
	coord = get_coord(args.i,args.w)
	argx, argy, argz, centerx, centery, centerz = CoordInfo(coord)


	print("""cellBasisVector1 {0} 0 0\ncellBasisVector2 0 {1} 0\ncellBasisVector3 0 0 {2}\ncellOrigin {3} {4} {5}\n
	""".format(argx,argy,argz,centerx,centery,centerz))
