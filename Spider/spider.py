import os

counter = 1
wordlists = [
	'raft-large-directories-lowercase.txt',
	'raft-large-files-lowercase.txt'
]
threads = 20
extensions = [
	'php',
	'aspx',
	'asp',
	'txt',
	'jsp',
	'vb',
	'htm',
]
URLS = []

#starts gobuster on different urls
def start(url):
	global counter,wordlists,threads
	for w in wordlists:
		print('[*] Running wordlists')
		os.system("gobuster dir -w %s -o urls.%d -t %d -x %s"%(w,counter,threads,','.join(extensions)))
	export()


#Reads all urls.x files and compiles them into urls.txt
def export():
	global wordlists,URLS
	urls = []
	for i in range(1,len(wordlists)+1):
		with open("urls.%d"%(i),'r') as f:
			for x in f.readlines():
				if x not in urls:
					urls.append(x)
	print("[*] Extracted a total of %d urls"%(len(urls)))
	
	with open("urls.txt",'w') as f:
		for i in urls:
			f.write(i)

# Reads urls from urls.txt and returns a list
def get():
	urls = []
	with open("urls.txt",'r') as f:
		for i in f.readlines():
			urls.append(i)

	return urls

