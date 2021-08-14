#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

//Calcular a soma dos três números anteriores à enésima posição dada
int sum = 0;
int find_nth_term(int n, int a, int b, int c)
{
    int array[3]; array[0] = a; array[1] = b; array[2] = c;
    if (n <= 3) //condição pra checar se tão pedindo algum número que não precisa somar (i.e. um dos 3 primeiros)
    {
        return array[n-1];
    }

    sum = a + b + c;

    if (0 >= (n - 3)) // Se menor do que n-3 pra excluir os valores que não foram somados (i.e. um dos 3 primeiros)
    {
        return sum;
        
    }
    n--; // usa o alvo como um índice máximo de iteração, diminuindo a cada chamada recursiva

    int actual = sum + find_nth_term(n, b, c, sum);
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