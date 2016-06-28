//takes list of edges as input and gives list of dominators for each node as output.
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void addnode(int,int[]);
void init(int[][500]);
void intersection(int[][500],int,int);
void Union(int[][500],int,int);
int graph[500][2],n,nodeCount=0,k;
unsigned int bitnode[10];

/*void copy(int a[][500],int pos1,int pos2)
{
	int i,j=2;
	a[pos1][1]=(pos1+1);
	for(i=1;a[pos2][i]!=0;i++){
		a[pos1][j]=a[pos2][i];
		j++;}
}*/
main()
{
	int i,j,h,nodes[500],dom[500][500],b[500][500],val,temp[500]; //'dom' matrix holds the dominators for all nodes.
	scanf("%d",&n);
	for(i=0;i<n;i++)
		for(j=0;j<2;j++)
			scanf("%d",&graph[i][j]);
	for(i=0;i<n;i++)							//list of all present nodes.
	{
		addnode(graph[i][0],nodes);	
		addnode(graph[i][1],nodes);
	}
	init(dom);
	for(i=0;nodes[i]!=0;i++)
	{
		dom[nodes[i]-1][0]=nodes[i];
	}
	for(i=0;i<nodeCount;i++)				//for each node gets all nodes from there's an edge to that node.
	{								//gets the intersection of dominator of all predecessor of a node.
		init(b);						//because dom(a)= a U (intersection(dom(predecessors))).
		k=0;							//stores the result is 'dom' matrix.
		for(j=0;j<n;j++)
		{
			if(nodes[i]==graph[j][1])
			{
				if(graph[j][1]>graph[j][0])
				{
					k++;	
					if(k!=1)
						intersection(dom,graph[j][1]-1,graph[j][0]-1);
					else Union(dom,graph[j][1]-1,graph[j][0]-1);
				}
			}
		}
	}
	for(i=0;i<500;i++)
		Union(dom,i,i);
	for(i=0;dom[i][0]!=0;i++)
	{
		for(j=0;dom[i][j]!=0;j++)
			printf("%d ",dom[i][j]);
		printf("\n");
	}
}


void init(int a[][500])
{
	int i,j;
	for(i=0;i<500;i++)
		for(j=0;j<500;j++)
			a[i][j]=0;
}

void insertvalue(int a[][500],int val,int k)
{
	int i,n,pos;
	for(i=0;a[k][i]!=0;i++);
	a[k][i]=val;
}


void Union(int a[][500],int pos1,int pos2)		//performs union on 2 rows(pos1,pos2) of matrix a using bitwise operations.
{
	int i,j,pos,n,h,count,value,index=1;
	unsigned int b[10],c[10];
	for(h=0;h<10;h++)
	{
		b[h]=0;
		c[h]=0;
	}

	for(i=0;a[pos1][i]!=0;i++)
	{
		n=a[pos1][i]/32;
		pos=a[pos1][i]%32;
		b[n]=b[n]|(1<<pos);
	}

	for(i=0;a[pos2][i]!=0;i++)
	{
		n=a[pos2][i]/32;
		pos=a[pos2][i]%32;
		c[n]=c[n]|(1<<pos);
	}

	for(i=0;i<10;i++)
	{
		b[i]=b[i]|c[i];
	}

	for(h=0;h<10;h++)
	{
		count=0;
		while(b[h]>0)
		{
			
			if(b[h]%2==1)
			{
				value=32*h+count;
			//	printf("%d ",value);
				a[pos1][index++]=value;
			}
			b[h]=b[h]>>1;
			count++;
		}

	}
}



void intersection(int a[][500],int pos1,int pos2)	//performs intersection on 2 rows(pos1,pos2) of matrix a using bitwise operations.
{
	int i,j,pos,n,h,count,value,index=1;
	unsigned int b[10],c[10];
	for(h=0;h<10;h++)
	{
		b[h]=0;
		c[h]=0;
	}

	for(i=1;a[pos1][i]!=0;i++)
	{
		n=a[pos1][i]/32;
		pos=a[pos1][i]%32;
		b[n]=b[n]|(1<<pos);
	}

	for(i=1;a[pos2][i]!=0;i++)
	{
		n=a[pos1][i]/32;
		pos=a[pos2][i]%32;
		c[n]=c[n]|(1<<pos);
	}

	for(i=0;i<10;i++)
	{
		b[i]=b[i]&c[i];
	}

	for(h=0;h<10;h++)
	{
		count=0;
		while(b[h]>0)
		{
			if(b[h]%2==1)
			{
				value=32*h+count;
			//	printf("%d ",value);
				a[pos1][index++]=value;
			}
			b[h]=b[h]>>1;
			count++;
		}

	}
	for(i=index;i<500;i++)
		a[pos1][i]=0;
}

void addnode(int val,int nodes[])  			//adds a node to nodes list. avoids repetition.
{
	int pos,n,h,count,index=0,value;
	unsigned int temp;
	n=val/32;
	pos=val%32;
	bitnode[n]=bitnode[n]|(1<<pos);
	for(h=0;h<10;h++)
	{
		count=0;
		temp=bitnode[h];
		while(temp>0)
		{
			if(temp%2==1)
			{
				value=32*h+count;
				nodes[index++]=value;
			}
			temp=temp>>1;
			count++;
		}

	}
	nodeCount=index;
}
