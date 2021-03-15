import os

def send_alert(msg):
	os.system("python /root/Desktop/Vinyl/send_alert.py \"%s\""%(msg))

def subdomain(sub):
	with open("subdomains.txt",'a') as f:
		f.write(sub)
	send_alert("New Subdomain : %s"%(sub))

def vuln(vul,sub):
	with open("vulns.txt","a") as f:
		f.write("Vulnerability : %s\nSubdomain : %s\n\n"%(vul,sub))
	send_alert("Vulnerability : %s\nSubdomain : %s"%(vul,sub))
