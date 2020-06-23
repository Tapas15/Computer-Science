#include<stdio.h>
#include<cs50.h>                  // likely we did not declard something very important here
int main(void)
{
    string name = get_string("What is your name :");
    printf("hello, %s\n", name);// printf("Hello, %s\n",name );
}