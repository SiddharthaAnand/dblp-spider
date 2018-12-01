'''
method to read stored credentials from a file to connect to the mongo database.
'''


def read_credential(file_name=None):

	with open(file_name, "r") as _file:
		_lines = _file.readlines()
		_file.close()
		user_name = _lines[0].strip().split()[1]
		pwd = _lines[1].strip().split()[1]
		url = _lines[2].strip().split()[1]
		return user_name, pwd, url

