from os import listdir
from shutil import copy2
import time
directory="/home/thomas/Desktop/special/"
backupDirectory="/home/thomas/Backup/"
currentList = []

while True:
	newList=listdir(directory)
	difference=list(set(newList)-set(currentList))
	print difference
	if len(difference)!=0:
		for i in range(0,len(difference)):
			copy2(directory+difference[i],backupDirectory+difference[i])
		currentList=newList
	time.sleep(5)
