#inserts 'phi' function t IR and renames the variables to get SSA.
import re
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
nodeCount=int(do[0])
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

f3=open('graph1.txt','r')
edge=f3.read()
ed=edge.split("\n")
edges=[]
for line in ed:
	t=line.split()
	if len(t)>=1:
		edges.append(t)
print edges
q=[]				#q is bfs order.
q.append('1')			#this part of code gets the BFS order of the CFG.
for j in range(nodeCount):
	for i in range (1,len(edges)):
		if edges[i][0]==q[j]:
			if edges[i][1] not in q:
				q.append(edges[i][1])
print
print
print q

var={}				#'var' is a dict having variables and their counts. used for renaming and updated as a new definition occurs.
for node in q:
	for j in range(len( blocks[node])):
		if not blocks[node][j].isdigit():
			lin=blocks[node][j].strip('\t\n ')
			lin=re.split('[ =*-/+]',lin)		#splits the line at =,+,-,*,/. and and stores in lin[]
#			print lin				#goes thruogh lin[] and if a variable is found, checks for its count in var{}
			for i in range(len(lin)):		#if key isn't found, inserts the variable as new key and intializes its count to 0.
				#l=blocks[node][j].split('=')	#if key is found its count is incremented.
				if 't' in lin[i] and 'phi' not in lin[i]:
					if lin[i] not in var:	#after that the variable is renamed.
						var[lin[i]]=1
					elif i==0:var[lin[i]]+=1
					if 'goto' not in lin[i]:
						blocks[node][j]=blocks[node][j].replace(lin[i],lin[i]+'_'+str(var[lin[i]]))

		print blocks[node][j]
print
print
print blocks

"""pos=0
pos2=3
for node in q:
	for i in range(len(blocks[node])):
		if 'phi' in blocks[node][i]:
			va=re.split('[(:,]',blocks[node][i])
			for j in range(1,len(edges)):
				if edges[j][1]==node:
					for line1 in blocks[edges[j][1]]:
						lin=re.split('=:',line1)
						if lin[pos1]==va[1]:
							va[pos2]=lin[1]
							pos1=pos1+2
							pos2=pos2+2
							break
					st=""
					for w in va:
						st=st+w
			blocks[node][i]=st
print
print
print
print blocks"""							
