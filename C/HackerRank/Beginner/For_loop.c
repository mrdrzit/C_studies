//Task For each integer n in the interval [a, b] (given as input) : 
// • If 1 < n < 9, then print the English representation of it in lowercase. That is "one" for 1, "two" for 2, and so on. 
// • Else if n > 9 and it is an even number, then print "even". 
// • Else if n > 9 and it is an odd number, then print "odd". 

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    char *words[9] = {"one","three", "four", "five", "six", "seven", "eight", "nine"};
    int a, b;
    scanf("%d\n%d", &a, &b);
  	
    for(int i = a; i < b; i++)
    {
    }

    return 0;
}
