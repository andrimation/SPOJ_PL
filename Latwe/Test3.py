import sys


data = list((sys.stdin.read()).split())

counter = 0

for x in range(len(data)):
	print("counter", counter)
	try:
		if data[x-1] != "42" and data[x] == "42" and x != 0:
			counter += 1
		else:
			pass
	except:
		pass
	print(data[x])
	if counter == 3:
		break