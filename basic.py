

def edgegenir():
	f1=open('input.txt','r')
	f2=open('graph.txt','w')
	i=0

	for i, l in enumerate(f1):
		pass
	n= i + 1
	i=1
	n1=0
	a=[]
	f1=open('input.txt','r')
	dict={}

	#for generating blocks
	#a keeps the starting label with : and ending goto's label of a block
	#if starting label is missing then -1 is stored... same holds for ending
	#dict has key indicating the block no and it has a
	for line in f1:
	    n1=n1+1
	    #check if it is "goto" or ":"
	    if line.find('goto',0,len(line))!=-1 or line.find(':',0,len(line))!=-1:
		#has both starting and ending labels
		if line.find('goto',0,len(line))!=-1 and  len(a)!=0:
		    last=line.split()
		    last=last[-1]
		    a.append(last)
		    dict.update({i:a})
		    i=i+1
		    a=[]
		    continue
		#only "goto" without starting label or ":" i.e only goto in this block
		if line.find('goto',0,len(line))!=-1 and len(a)==0:
		    a.append(-1)
		    last=line.split()
		    last=last[-1]
		    a.append(last)
		    dict.update({i:a})
		    i=i+1
		    a=[]
		    continue
		#":" always is a new block 
		if line.find(':',0,len(line))!=-1 and len(a)==0:
		    a.append(line.strip(':\n'))
		    continue
		#no "goto in this block i.e, the block is between two ":"s
		if line.find(':',0,len(line))!=-1 and len(a)!=0:
		    #for the previous block
		    a.append(-1)
		    dict.update({i:a})
		    a=[]
		    #this block
		    i=i+1
		    a.append(line.strip(':\n'))
		    continue
	#1st line without label. So starting label is -1
	    elif n1==1:
		a.append(-1)
	    elif n1!=1 and len(a)!=0 and n1!=n:
		continue
	#last line without goto            
	    elif n1==n :
		a.append(-1)
		dict.update({i:a})

	#display the blocks
	#print dict

	#for generating edges

	#for direct edges
	for i in range(1,len(dict)):
		#for j in dict[i]:
		if dict[i][0]==-1 and dict[i][1]==-1:
		        b=i+1
		        f2.write(str(i)+" "+str(b)+"\n")
		elif dict[i][0]==-1 and i==1:
			b=i+1
			f2.write(str(i)+" "+str(b)+"\n")
		elif dict[i][0]==-1 :
		        continue
		else:
		        b=i+1
		        f2.write(str(i)+" "+str(b)+"\n")

	#to connect to the label given by goto
	for i in range(1,len(dict)):
		if dict[i][1]!=-1:
		        label=dict[i][1]
		        for j in range(1,len(dict)+1):
		                if dict[j][0]!=-1 and j!=i:
		                        if dict[j][0]==label and (i+1)!=j:
		                                f2.write(str(i)+" "+str(j)+"\n")
		                                break
		                else:
		                        continue



	f2=open('graph.txt','r')
	for i, l in enumerate(f2):
		pass
	n= i + 1

	f1.close()
	f2.close()
	f1=open('graph.txt','r')
	f2=open('graph1.txt','w')
	f2.write(str(n)+"\n")
	for line in f1:
		f2.write(line)
	f2.close()
	f1.close()

#for regenerating block
def regenir():
	f1=open('block1.txt','w')
	f2=open('input.txt','r')
	i=0
	for line in f2:
		#f2.write(str(i)+"\n")
		if (line.find('goto',0,len(line))!=-1 or line.find(':',0,len(line))!=-1) and i!=0:
			if line.find('goto',0,len(line))!=-1:
				line1=next(f2)
				if (line1.find(':',0,len(line1))==-1 ):
					#print line
					f1.write((line))
					i=i+1
					f1.write(str(i)+"\n"+line1)
				
				elif(line1.find(':',0,len(line1))!=-1) :				
					f1.write(line)
					i=i+1
					f1.write(str(i)+"\n"+line1)
					continue
		
			elif line.find(':',0,len(line))!=-1:
				i=i+1
				f1.write(str(i)+"\n"+line)
				continue	
		else:
			if i==0:
				i=i+1
				f1.write(str(i)+"\n")
			f1.write(line)
	f1.close()
	f2.close()

edgegenir()
regenir()
