#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
    fstream file;
	file.open("JACK3.DAT");
	if(file.good())
	{
        int n;
        file >> n;
        int p[1000];
        int pi[1000];
        int r[1000];
        int c[1000];
        
        p[0]=0;
        r[0]=0;
        c[0]=0;
        pi[0]=0;
        for(int i = 1; i<=n; i++)
        {
            file >> r[i];
            file >> p[i];
            pi[i]=i;
            cout<<r[i]<<" // "<<p[i]<<endl;
        }
        file.close();
        
        for(int i = 1; i<n; i++)
        {     
            for(int j = 1; j<n; j++)
            {               
                if(r[pi[j-1]] >= r[pi[j]])
                {
                    swap(pi[j-1], pi[j]);
                }
            }
        }
        
        for(int i = 1; i<n; i++)
        {
            cout<<"c ["<<i<<"]"<<c[pi[i]] = max(r[pi[i]],c[i-1])+p[i];
        }
        



    
    }
}