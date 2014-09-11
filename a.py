import urlparse
lvhecai=[]
login=[]
with open('lvhecai.txt','r') as f:
	for line in f.readlines():
		host=urlparse.urlparse(line.strip())[1]
		#print host
		lvhecai.append(host)

with open('login.txt','r') as f:
        for line in f.readlines():
                host=urlparse.urlparse(line.strip())[1]
                #print host
		login.append(host)

result_set=set(lvhecai) - set(login)
for re_host in result_set:
	print re_host
