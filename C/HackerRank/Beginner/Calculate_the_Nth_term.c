#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

//Calcular a soma dos três números anteriores à enésima posição dada

int find_nth_term(int n, int a, int b, int c)
{
    int sum = a + b + c;

    if ((n - 1) == 0)
    {
        return sum;
    }

    a = b;
    b = c;
    c = sum;
    n--;

    find_nth_term(n, a, b, c);
}

int main()
{
    int n, a, b, c;

    scanf("%d\n %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);

    printf("%d", ans);
    return 0;
}

// a + b + c = x
// b + c + x = y
// c + x + y = z

// for (int i = 0; i < n; i++)
// x_termo = a + b + c
// y_termo = x_termo + c + b
// z_termo = z_termo + y_termo + x_termo
// w_termo = w_termo + z_termo + y_termo

//   int sum = a + b + c;
//   a = 0;
//   b = a;
//   c = b;
//   next_term = sum

// int list[n];
// for (int i = 0; i < n; i++)
// {
//   list[i] = a
//   a++;
// }

// list[0]