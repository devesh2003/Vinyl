from bs4 import BeautifulSoup
import requests

urls = []
scripts = []

def start():
	with open("urls.txt",'r') as f:
		for i in f.readlines():
			r = requests.get(i,verify=False)
			src = r.content
			print("[*] Spidering source of %s for scripts and creds"%(url))
			spider_source(src)
	compile()
			
#add url to urls
def add():
	pass

#append all urls to url.txt
def compile():
	global urls
	with open("urls.txt",'a') as f:
		for i in urls:
			f.write(i)

#Spider script for creds,tokens and urls
def spider_script(url):
	pass

#find script links through the source and pass it to spider_script()
def spider_source(src):
	pass
