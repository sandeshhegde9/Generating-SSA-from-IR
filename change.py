f1=open('block1.txt','r')
f3=open('blocks','w')
#a=f1.read()
#print a
for line in f1:
	f2=open('changes','r')
	flag=True
	for i in range(100):
		if line==str(i)+"\n":
			flag=False
			lin=line.split()
			for line1 in f2:
				if line1.find(lin[0]+" ")!=-1:
					lin2=line1.split()
					f3.write(lin2[1]+"\n")
					break
	if(flag):f3.write(line)
	f2.close()
f1.close()
f3.close()
