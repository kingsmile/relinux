import sys
import time
char = "|"
for i in range(0, 800):
	sys.stdout.write("\r[")
	for x in range(1, 100):
		if x <= (i / 8):
			sys.stdout.write("=")
		elif x == ((i / 8) + 1):
			sys.stdout.write(char)
		else:
			sys.stdout.write(" ")
	sys.stdout.write("] " + str(i) + "/800 " + str(int(float(float(float(i / 8) / 100) * 100))) + "%")
	sys.stdout.flush()
	if char == "|":
		char = "/"
	elif char == "/":
		char = "-"
	elif char == "-":
		char = "\\"
	elif char == "\\":
		char = "|"
	time.sleep(0.3)
