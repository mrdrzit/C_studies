#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Your task is to take two numbers of int data type, two numbers of float data type as input and output their sum:
// Declare 4 variables: two of type int and two of type float.
// Read 2 lines of input from stdin (according to the sequence given in the 'Input Format' section below) and initialize your  variables.
// Use the + and - operator to perform the following operations:
// Print the sum and difference of two int variable on a new line.
// Print the sum and difference of two float variable rounded to one decimal place on a new line.


int main(void)
{
    //Initialize values 
    int int1 = 0;
    int int2 = 0;
    float float1 = 0;
    float float2 = 0;

    // Prompt for two floats
    scanf("%d %d", &int1, &int2);
    scanf("%f %f", &float1, &float2);

    int isum = int1 + int2;
    int idiff = int1 - int2; 
    float fsum = float1 + float2;
    float fdiff = float1 - float2; 
    printf("%d %d\n%.1f %.1f\n", isum, idiff, fsum, fdiff);

    //TODO: #1 Create comments for these lines
}