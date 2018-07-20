import os

def rename_files():
	file_list = os.listdir(r"/Users/arvida/myProject/prank")
	#print(file_list)
	saved_path = os.getcwd()
	os.chdir(r"/Users/arvida/myProject/prank")
	for file_name in file_list:
		print("New Name - "+file_name)
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files()
