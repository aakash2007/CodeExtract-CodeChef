
def write_to_file(obj, fl_code, lang):
	fl_name = fl_code + lang
	with open(fl_name,'w') as fl:
		fl.write(obj)