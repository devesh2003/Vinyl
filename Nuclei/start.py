import sys,os
sys.path.insert(1, '/root/Desktop/Vinyl')
import add 

def start():
	os.system('for i in $(cat /root/Desktop/Vinyl/Subdomain_finder/subdomains.txt);do echo "https://"$i; done > main.txt')
	os.system("nuclei -stats -v -t /root/nuclei-templates/ -l main.txt -o vulns.txt -c 5")
	with open("vulns.txt","r") as f:
		for i in f.readlines():
			if "info" not in i:
				os.system("python3 /root/Desktop/Vinyl/send_vuln.py \"%s\""%(i))

def main():
	start()

main()