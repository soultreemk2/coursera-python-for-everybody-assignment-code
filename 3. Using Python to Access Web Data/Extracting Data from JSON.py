# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib
import json

url = input("Enter location: ")
address = urllib.urlopen(url)
data = address.read()

total = 0

while True:
	if len(url)<1: break

	print("Retrieving: ", address)
	print("Retrieved ", len(data)," characters")

	info = json.loads(data)
	info = info["comments"]
	# dictionary가 여러개 이므로 for문 사용
	for item in info:
		print("Count: ",item["count"])
		total += int(item["count"])
		print("Sum: ", total)
	print("Final sum: ", total)
	break
