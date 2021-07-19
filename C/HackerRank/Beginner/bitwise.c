#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
// Complete the following function.

// For each number i from 1 through n, find the maximum value of the logical and, or and XOR
// when compared against all integers through n that are greater than i.
// Consider a value only if the comparison returns a result less than K$.
// Print the results of the and, or and XOR comparisons on separate lines, in that order.

// Test: For n = 3, k = 3
// S = {1,2,3}
// S = {1,2,3,4,5}

void calculate_the_maximum(int n, int k)
{
    //Write your code here.
    int current_pointer = 0;
    int comp_var = 0;
    int S[n];
    int and = 0, or = 0, xor = 0, print_and = 0, print_or = 0, print_xor = 0;
    int and_max = 0, or_max = 0, xor_max = 0;

    for (int i = 0; i < n; i++)
    {
        S[i] = i + 1;
    }

    while (current_pointer < n)
    {
        if (comp_var == n)
        {
            current_pointer++;
            comp_var = current_pointer;
        }

        if (current_pointer != comp_var)
        {
            and = S[current_pointer] & S[comp_var];
            or = S[current_pointer] | S[comp_var];
            xor = S[current_pointer] ^ S[comp_var];

            if (and_max < and)
            {
                and_max = and;
            }
            if (or_max < or)
            {
                or_max = and;
            }
            if (xor_max < xor)
            {
                xor_max = xor;
            }

            if (and < k && print_and < and)
            {
                print_and = and;
            }

            if (or < k && print_or < or)
            {
                print_or = or ;
            }

            if (xor < k && print_xor < xor)
            {
                print_xor = xor;
            }
        }
        comp_var++;
    }
    printf("%d\n%d\n%d\n", print_and, print_or, print_xor);
}

int main()
{
    int n, k;

    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    return 0;
}