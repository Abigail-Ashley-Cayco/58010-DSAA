#include <iostream>
using namespace std;
int main() 
{
    int numbers[] = {5, 4, 3, 2, 1};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    cout << "Original Array: ";
    for (int i = 0; i < size; i++) 
	{
        cout << numbers[i] << " ";
    }
    for (int i = 0; i < size / 2; i++) 
	{
        int temp = numbers[i];
        numbers[i] = numbers[size - i - 1];
        numbers[size - i - 1] = temp;
    }
    cout << "\nReversed Array: ";
    for (int i = 0; i < size; i++) 
	{
        cout << numbers[i] << " ";
    }
    return 0;
}
