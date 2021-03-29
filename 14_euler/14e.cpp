#include<iostream>
double sequence(int  x, double n);

int main ()
{
  int y=0;
  for(int i=1;i<1000001;i++)
    {
      int w=sequence(i,0);
      std::cout<<"w="<<w<<" y="<<y<<" i="<<i<<std::endl;
      if(y<w)
	{
	  y=w;
	    std::cout<<"Number "<<i<<std::endl;
	}

    }
  return 0;
}
double sequence(int  x, double n)
{
  if (x%2==0 && x!=1)
    {
      std::cout<<x/2<<std::endl;
      return sequence(x/2,n+1);
    }
  else
    {
      if(x!=1)
	{
	  return sequence(3*x+1,n+1);
	}
      return n;
    }
  
}
