import os, re, csv

def exists(file):
	return os.path.isfile(file)
	
def rename(file,newfile):
	os.rename(file,newfile)
	
def remove(file):
	if exists(file):
		os.remove(file)

def linecount(file):
	#print(file)
	if exists(file):
		with open(file,'r') as f:
			numlines = 0
			for line in f:
				numlines = numlines + 1
			return numlines
	return False

def currdir(file):
	return os.path.split(os.path.realpath(file))[0]


def clean_fields(row):
	return row.strip().replace('$','').lower().upper()

def get_headers(file):
	with open(file,'r') as f:
		return clean_fields(f.readline()).replace('"','').replace(' ','_').lower().split(',')

def to_array(file):
	resultarr = []
	with open(file, 'r') as f:
		for line in f:
			resultarr.append(line)
	return resultarr

def to_dict_array(csv_file):
	rows = []
	with open(csv_file, 'r') as f:
		headers = clean_fields(f.readline()).replace('"','').replace(' ','_').lower().split(',')
		reader = csv.DictReader(f, headers)
		for row in reader:
			rows.append(row)
	return rows

def get_diff(newfile, oldfile):
	new = to_array(newfile)
	diff_file = newfile + '.diff'

	changes = []
	if exists(oldfile):
		old = to_array(oldfile)
		changes = set(new) - set(old)
	else:
		changes = new[1:]

	with open(diff_file, 'w+') as f:
		f.write(new[0])
		for row in changes:
			f.write(row)

	changes = to_dict_array(diff_file)
	os.remove(diff_file)
	return changes

def get_changed_rows(new, old):
	changed = {}
	changed['rows'] = get_diff(new, old)
	changed['count'] = len(changed['rows'])
	changed['has_changed'] = changed['count'] > 0
	changed['headers'] = get_headers(new)
	return changed

def csv_to_dictarray(filename, headers):
	mainarr = []
	with open(filename,'r') as f:
		for line in f:
			rowdict = {}
			index = 0
			for col in row:
				rowdict[headers[index]] = col
				index = index + 1
			mainarr.append(rowdict)
	return mainarr

