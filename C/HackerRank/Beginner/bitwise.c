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
    int current_pointer = 0; //This will be the index used to identify the first number in the comparison (aka "a")
    int comp_var = 0;        //This will be the index used to identify the second number in the comparison (aka "b")
    int S[n];                //The array of numbers used for the comparisons
    int and = 0, or = 0, xor = 0, print_and = 0, print_or = 0, print_xor = 0;
    // int and_max = 0, or_max = 0, xor_max = 0;

    for (int i = 0; i < n; i++) //Create the array
    {
        S[i] = i + 1;
    }

    //Loop that goes through the numbers comparing each individual case
    while (current_pointer < n)
    {
        //This updates the pointers.
        //Important to notice here that every time the current index changes, the comparison also does..
        //This is because we don't want to compare the numbers that passed already to shun redundancy
        if (comp_var == n)
        {
            current_pointer++;
            comp_var = current_pointer;
        }

        //Different because we don't want to compare the number with itself, only pairs of different ones
        if (current_pointer != comp_var)
        {
            //Saving the results in temporary values for each one
            and = S[current_pointer] & S[comp_var];
            or = S[current_pointer] | S[comp_var];
            xor = S[current_pointer] ^ S[comp_var];

            //These conditions verify that the results from the bitwise operation is actually in the parameters set in the task
            if (and < k && print_and < and)
            {
                print_and = and;
                int and_max = and;
            }

            if (or < k && print_or < or)
            {
                print_or = or ;
                int or_max = and;
            }

            if (xor < k && print_xor < xor)
            {
                print_xor = xor;
                int xor_max = xor;
            }
        }
        comp_var++;
    }
    //Actually printing the values needed for the task
    printf("%d\n%d\n%d\n", print_and, print_or, print_xor);
}

int main()
{
    int n, k;

    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    return 0;
}