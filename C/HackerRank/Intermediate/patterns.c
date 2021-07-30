#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Print a pattern of numbers from 1 to n as shown below. Each of the numbers is separated by a single space.

//                             4 4 4 4 4 4 4
//                             4 3 3 3 3 3 4
//                             4 3 2 2 2 3 4
//                             4 3 2 1 2 3 4
//                             4 3 2 2 2 3 4
//                             4 3 3 3 3 3 4
//                             4 4 4 4 4 4 4

//                             4 4 4 4
//                             4 3 3 3
//                             4 3 2 2
//                             4 3 2 1

void print_line(int array[], int line_size)
{
    for (int i = 0; i < line_size; i++)
    {
        printf("%d ", array[i]);
    }
}

int main()
{
    const int n = 4;

    int line[] = {[0 ... n-1] = n};
    int printing = n;
    // const int num_lines = (n * 2) - 1;
    // scanf("%d", &n);
    // Complete the code to print the pattern.

    for (int iline = 0; iline < n; iline++)
    {
        int num_print = (n - iline);

        printf("%d ", n);

        if (iline == n - 1)
        {
            printf("\n");
        }
    }
    return 0;
}