/* C equivalent code of Factorial() */
#include<stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int k = 1;
    int a = n;
    do{
    a += 1;
    k *= n;
    a = n;
    a -= 1;
    n = a;
    a -= 1;
    }while(a>=0);
    int ans=k;
    printf("%d", ans);
}