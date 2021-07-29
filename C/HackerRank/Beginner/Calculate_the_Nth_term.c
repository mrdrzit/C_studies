#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

//Calcular a soma dos três números anteriores à enésima posição dada
int sum = 0;
int find_nth_term(int n, int a, int b, int c)
{
    int counter = 0;
    sum = a + b + c;

    if (counter == (n - 4))
    {
        return sum;
        
    }

    a = b;
    b = c;
    c = sum;
    n--;
    counter++;

    int actual = sum + find_nth_term(n, a, b, c);
    return sum;
}

int main()
{
    int n, a, b, c;
    scanf("%d\n %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);

    printf("%d", ans);
    return 0;
}