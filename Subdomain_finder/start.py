import os,sys
sys.path.insert(1, '/root/Desktop/Vinyl')
import add  

def check(subdomain):
	with open("subdomains.txt",'r') as f:
		for i in f.readlines():
			if i == subdomain:
				return False
	return True

def start_sublistr(domain):
	os.system("sublist3r -d %s -o output.txt"%(domain))
	with open("output.txt",'r') as f:
		for i in f.readlines():
			if "<BR>" in i:
				x = i.split('<BR>')
				for y in x:
					if(check(y)):
						add.subdomain(y)
			if check(i):
				add.subdomain(i)

def start_amass(domain):
	os.system("amass enum -d %s -o output.txt"%(domain))
	with open("output.txt",'r') as f:
		for i in f.readlines():
			if check(i):
				add.subdomain(i)

def start_subbrute(domain):
	os.system("python3 /opt/subbrute/subbrute.py -s /opt/SecList/Discovery/DNS/subdomains-top1million-110000.txt -o output.txt %s"%(domain))
	with open("output.txt",'r') as f:
		for i in f.readlines():
			if check(i):
				add.subdomain(i)

def main():
	start_sublistr(sys.argv[1])
	start_amass(sys.argv[1])
	start_subbrute(sys.argv[1])

main()