import os
import textract

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
	list_of_files[dirpath] = []
	for filename in filenames:
		if filename.endswith('.pdf'): 
			list_of_files[dirpath].append(os.sep.join([dirpath, filename]))


forbiddenWords = ["vulnerable", "entitlement", "diversity", "transgender", "fetus", "evidence-based","science-based"]

f = open("forbiddenWordFileCount.csv", 'w')

for x in list_of_files.keys():
	for y in list_of_files[x]:
		forbiddenCount = 0
		text = str(textract.process(y))
		for t in forbiddenWords:
			if t in text:
				forbiddenCount += 1
		f.write(x + "," + y + "," + str(forbiddenCount) + "\n")

f.close()