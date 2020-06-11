#include<stdio.h>
#include<cs50.h>
int main(void)
{
    printf("how many stars?");
    int x = get_int("enter:");

    for(int i=0;i <= x;i++)
        printf("*");

    printf("\n");
}