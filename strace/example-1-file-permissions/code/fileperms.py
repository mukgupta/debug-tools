import sys
try:
	file = sys.argv[1]
	ff = open(file)
	print ff.readlines()
except:
	pass