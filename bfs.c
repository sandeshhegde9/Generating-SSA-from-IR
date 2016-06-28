#include<stdio.h>
#include<stdlib.h>
struct Q
{
	int a[1000];
	int front,rear;
};
unsigned int bitnode[10]={0,0,0,0,0,0,0,0,0,0};
int delete(struct Q*);
void insert(struct Q*,int);
int checknode(int,int[]);
void addnode(int,int[]);
main()
{
	int i,j,graph[500][2],n,val,nodes[500],g[500][4],change[500][2],index=0,k=1,count=0;
	FILE *file;
	file=fopen("changes","w");
	struct Q q;
	q.front=0;
	q.rear=-1;
	for(i=0;i<100;i++)
		nodes[i]=0;	
	scanf("%d",&n);
	for(i=0;i<n;i++)
		for(j=0;j<2;j++)
		{
			scanf("%d",&graph[i][j]);
			g[i][j]=graph[i][j];
			g[i][2+j]=0;
		}
	insert(&q,1);
	addnode(1,nodes);
	while((q.rear>=q.front))
	{
		val=delete(&q);
		change[index][0]=val;
		change[index][1]=k;
		index++;

	//	addnode(val,nodes);
	//	printf("%d ",val);
		for(j=0;j<n;j++)
		{
			if(g[j][0]==val&&g[j][2]==0)
			{
				g[j][0]=k;
				g[j][2]=1;
			}
			if(g[j][1]==val&&g[j][3]==0)
			{
				g[j][1]=k;
				g[j][3]=1;
			}

		}
		k++;
		for(i=0;i<n;i++)
		{
			if(val==graph[i][0])
			{
				if(checknode(graph[i][1],nodes))
				{
					insert(&q,graph[i][1]);
					addnode(graph[i][1],nodes);
				}
			}
		}
	}
	for(i=0;nodes[i]!=0;i++)
		count++;
		fprintf(file,"%d\n",count);
	for(i=0;i<count;i++)
	{
		fprintf(file,"%d %d\n",change[i][0],change[i][1]);
	}
	printf("%d\n",n);
	for(i=0;i<n;i++)
	{
		for(j=0;j<2;j++)
			printf("%d ",g[i][j]);
		printf("\n");
	}

}

int checknode(int val,int nodes[])
{
	int i;
	for(i=0;nodes[i]!=0;i++)
	{
		if(nodes[i]==val)
			return 0;
	}
	return 1;
}

int delete(struct Q *q)
{
	int a;
	if(q->rear<q->front)
		return 0;
	else
	{
		a=q->a[q->front];
		q->front++;
		return a;
	}
}

void insert(struct Q *q,int val)
{
	if(q->rear>=1000)
		return;
	else
	{
		q->rear++;
		q->a[q->rear]=val;
		return;
	}
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
}
