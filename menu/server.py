import os

def get_app():
	path = "micropython/"
	dir_list = os.listdir(path)

	dir_list.remove('menu')
	dir_list.remove('.git')
	dir_list.remove('.gitignore')

	return str(dir_list)