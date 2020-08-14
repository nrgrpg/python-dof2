''' Python DOF2 library v1.0

Discord: [NRG]Dark#4052

'''

import os.path




def DOF2_Get(file, key):
	file = open(file, encoding='UTF-8')
	List = file.read()
	file.close

	List = List.split('\n')

	for x in List:
		if(x.find(key) == 0):
			return x[x.find('=')+2:]			
	return -1



def DOF2_Set(file, key, value):
	filex = open(file, encoding='UTF-8')
	List = filex.read()
	filex.close

	List = List.split('\n')
	affected = 0
	for index,x in enumerate(List):
		if(x.find(key) == 0): 
			List[index] = List[index].replace(DOF2_Get(file,key),str(value))
			affected+=1

	if(affected == 0):
		List.append(str(key) + ' = ' + str(value))

	file2 = open(file, 'w+',encoding='UTF-8')
	for x in List:
		if(x == ''): continue
		file2.write(x + '\n')
	file2.close

	return affected



def DOF2_FileExists(file):
	if os.path.isfile(file):
	    return True
	else:
	    return False

def DOF2_CreateFile(file):
	if(DOF2_FileExists(file) == False):
		f = open(file, "w")
		f.close
		return 1
	else:
		return 0

def DOF2_RemoveFile(file):
	if(DOF2_FileExists(file)):
		os.remove(file)
		return 1
	else:
		return 0
