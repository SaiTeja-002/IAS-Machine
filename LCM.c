#include<stdio.h>
int main()
{
    int a, b, gcd=1;
    scanf("%d %d", &a, &b);
    for(int i=b;i>0;i--)
    {
        if(a%i == 0 && b%i == 0)
        {
            gcd = i;
            break;
        }
    }
    printf("GCD = %d\n", gcd);
    int lcm = (a*b)/gcd;
    printf("LCM = %d", lcm);
}