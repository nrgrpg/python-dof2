from dof2 import *

PATH = 'C:/Users/User/Desktop/samp03svr/scriptfiles/accounts/'  #path to the files




nick = input('Type the nickname:')

PATH = PATH + nick + '.ini' #add extension

print('Directory: ' + PATH)

if(DOF2_FileExists(PATH) == True):
	print("The file exists")
else:
	print("The file doesn't exists")
	DOF2_CreateFile(PATH)
	print("File Created")
	DOF2_Set(PATH,"Level","30")
	print("Level: " + DOF2_Get(PATH,"Level"))
