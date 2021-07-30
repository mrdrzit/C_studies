#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Print a pattern of numbers from 1 to n as shown below. Each of the numbers is separated by a single space.

//                             4 4 4 4
//                             4 3 3 3
//                             4 3 2 2
//                             4 3 2 1

void print_line(int array[], int line_size, int subtract, int which)
{

    for (int i = 0; i < line_size; i++)
    {
        if (i >= which)
        {
            array[i] = line_size - subtract;
        }
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main()
{
    int subtract = 0; //How much do i need to subtract
    int which = 0; //at which element do i need to start subtracting

    const int n = 9;

    int line[] = {[0 ... 8] = n};

    for (int iline = 0; iline < n; iline++)
    {
        print_line(line, n, subtract, iline);
        subtract++;
        which++;
        if (iline == n - 1)
        {
            printf("\n");
        }
    }
    return 0;
}