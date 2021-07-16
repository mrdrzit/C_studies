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
    int a, b;
    printf("numeros ");
    scanf("%d\n%d", &a, &b);
    char *words[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        for (int i = a; i <= b; i++)
        {
            int currenti = i;
            if (i >= 1 && i <= 9)
            {
                printf("%s\n", words[i - 1]);
            }
            else if (i > 9 && (i % 2 == 0))
            {
                printf("even\n");
            }
            else if (i > 9 && (i % 2 != 0))
            {
                printf("odd\n");
            }
        }
        return 0;
    }
