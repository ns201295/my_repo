#import<stdio.h>
void main()
{
  int T,N,i,j,a,tc,ans[100000];
  char S[100000];
  scanf("%d",&T);
  for(tc=0 ; tc < T ; tc++)
    {
      a = 0;
      scanf("%d",&N);
      scanf("%s",S);
      for(i = 0; i < N ; i++)
	{
	  if(S[i] == '0')
	    continue;
	  for(j = i ; j < N ; j++)
	    {
	      if(S[j] == '1')
		a++;
	    }
	}
      ans[tc] = a;
    }
  for(i = 0;i < T;i++)
    printf("%d\n",ans[i]);
  //return 0;
}
