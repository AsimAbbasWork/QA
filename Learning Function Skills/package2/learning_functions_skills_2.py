import os
from os import path

def replace_text(file_path, search_string, replace_string):
	
	if path.exists(file_path) == True:
		if os.path.getsize(file_path) == 0:
			return 'Custom Message: File is Empty'
		else:
			search_string_found = False
			with open(file_path, 'r') as f:
				lines = f.readlines()
			
			for line in range(0, len(lines)) :
				if search_string in lines[line]:
					lines[line] = "{}\n".format(replace_string)
					search_string_found = True
				

			
			if search_string_found == False:
				return 'Search string not found in file'
			else:
				with open(file_path, 'w') as f:
					f.writelines(lines)
					return "Replace String Inserted Successfully"

	else:
		return "Custom Message : File does not exist"
    




