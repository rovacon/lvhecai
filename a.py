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

#result_set=set(lvhecai) | set(login)
result_set=set(lvhecai) - set(login)
def rev(list):
	newlist=[]
	for re_host in list:
		newlist.append(re_host[::-1])
	#newlist.sort()
	return newlist
	#print '"'+re_host+'" : "time=30,", \\'

rev_sorted = rev(result_set)
rev_sorted.sort()
result=rev(rev_sorted)
for host in result:
	print '"'+host+'" : "time=30,", \\'
	#print '"'+host+'":"3,2,336,lbgproxy.zc.u3.ucweb.com:8080",\\'
