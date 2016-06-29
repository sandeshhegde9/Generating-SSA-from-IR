
#for creating dictionary with keys s block no and elements are lists which contains code
import re
f1=open('block1.txt','r')
dicti={}
a=[]
f1=open('block1.txt','r')
line1=1
f1.next()
for line in f1:	
	if not line.strip().isdigit():
		lin=line.strip()
		a.append(lin)
	else: 
		a=[]
		line1=line.strip()
	dicti.update({int(line1):a})	
print dicti
dict=dicti.copy()
f1.close()


#generating phi without renaming variables using DF and is put into dictionary
print("\n\n")
f1=open('DF','r')
dictio={}
for line in f1:
	line.strip()
	lin=line.split(" ")
	for values in dicti[int(lin[0])]:
		if values.find(" = ")!=-1 and values.find("phi(")==-1:
			lin1=values.split(" ")
			#print lin1[0]
			obj=[str(lin1[0])+" = "+"phi("+str(lin1[0])+","+str(lin1[0])+")"]
			for i in range(1,len(lin)-1):
				if obj not in dicti[int(lin[i])]:				
					lin[i].strip()
					dicti[int(lin[i])]=obj+dicti[int(lin[i])]
			obj=[]
#to remove repeated insertion of same phi		
from collections import OrderedDict
for i in dicti:
	dicti[i]=list(OrderedDict.fromkeys(dicti[i]))
print dicti

df=open('DF','r')
d=df.read()
dom={}
do=d.split("\n")
nodeCount=int(do[0])

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
	for j in range(len( dicti[int(node)])):
		if not dicti[int(node)][j].isdigit():
			lin=dicti[int(node)][j].strip()
			lin=re.split('[ =*-/+]',lin)		#splits the line at =,+,-,*,/. and and stores in lin[]
			#print "here"
			#print lin				#goes thruogh lin[] and if a variable is found, checks for its count in var{}
			for i in range(len(lin)):		#if key isn't found, inserts the variable as new key and intializes its count to 0.
				#l=dicti[node][j].split('=')	#if key is found its count is incremented.
				if 't' in lin[i] and 'phi' not in lin[i]:
					flag=1
					if lin[i] not in var:	#after that the variable is renamed.
						var[lin[i]]=1
						if lin[i]=='t32':
							print var
						flag=0
					elif i==0 and flag==1:
						var[lin[i]]+=1
					if 'goto' not in lin[i] and i!=len(lin)-1:
						dicti[int(node)][j]=dicti[int(node)][j].replace(lin[i]+' ',lin[i]+'_'+str(var[lin[i]]))
					elif i==len(lin)-1:
						dicti[int(node)][j]=dicti[int(node)][j].replace(lin[i],lin[i]+'_'+str(var[lin[i]]))
						if 'phi' in dicti[int(node)][j]:
							dicti[int(node)][j]=dicti[int(node)][j].strip('_1')


		#print dicti[int(node)][j]
for i in range(1,len(dicti)):
	print str(i)
	print dicti[i]
print
print
print dicti



