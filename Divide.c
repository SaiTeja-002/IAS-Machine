/* C equivalent code of Divide() */
#include<stdio.h>
int main()
{
    int a, b, c;
    scanf("%d %d", &a, &b);     //Taking two numbers 'a' and 'b' as the input from the user
    c = a/b;        //Storing the value of their division into a third variable 'c'
    printf("%d", c);        //Printing the value of the third variable
}