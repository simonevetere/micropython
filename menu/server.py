import os

def get_app():
	path = "micropython/"
	dir_list = os.listdir(path)

	return str(dir_list)