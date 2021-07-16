//Task
// Given a five digit integer, print the sum of its digits.

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int recursive(int number);

int main() {
	int sum = 0;
    int n;
    scanf("%d", &n);

    char result[6]; // Create an empty character array to store the number that was converted to an array
    sprintf(result, "%d", n); // Converts an input "n" into an array
    int tamanho = strlen(result); // Gets ths number of digits in the original number using the converted array

    //Complete the code to calculate the sum of the five digits on n.
    int current = n;
    for (int i = 0; i < tamanho; i++)
    {
        sum = sum + current % 10; // Only leaves the last number of an integer in base 10
        current = current/10; // Truncates the last digit of the number given
    }
    printf("%d", sum);

    return 0;
}