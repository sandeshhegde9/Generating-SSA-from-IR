df=open('DF','r')
block=open('block1.txt','r')
d=df.read()
b=block.read()
lines=b.split("\n")
for z in range(len(lines)):
	lines[z]=lines[z].strip("\t")
blocks={}
for i in range(len(lines)):
	if lines[i].isdigit():
		blocks[lines[i]]=None
		a=[]
		for j in range(i+1,len(lines)):
			if not lines[j].isdigit():
				a.append(lines[j])
			else:break
			blocks.update({lines[i]:a})
print blocks
dom={}
do=d.split("\n")
for line in do:
	lin=line.split()
	if len(line)>1:
		a=lin[1:]
		dom[lin[0]]=a;
print
print
print dom
print
print
for key in blocks:
	a=[]
	for line in blocks[key]:
		if "==" not in line:
			var=line.split("=")
			a.append(var[0])
	for df in dom[key]:
	#	print df
		b=""
		for line in blocks[df]:
			for v in a:
				if v in line:
					b=b+v+"=phi("+v+","+v+")\n"
		if b!="":
			c=b.split("\n")
			for x in c:
				blocks[df].insert(0,x)
#	blocks.update({key:b})
	
print dom
print
print
print blocks
