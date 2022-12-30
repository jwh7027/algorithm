#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void PrintArray(int* arr, int size);
void Swap(int* xp, int* yp);
void SelectionSort(int* arr, int size);

int main()
{
	int arr[] = { 66,25,12,22,11,35 };
	int n = sizeof(arr) / sizeof(arr[0]);

	PrintArray(arr, n);
	SelectionSort(arr, n);
	PrintArray(arr, n);

	return 0;
}

void PrintArray(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d ", arr[i]);
	}
	printf("\n");
}

void Swap(int* xp, int* yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

void SelectionSort(int arr[], int n)
{
	int i, j, min_idx;
	for (i = 0; i < n - 1; i++)
	{
		int min_idx = i;
		for (j = i + 1; j < n; j++)
		{
			if (arr[j] < arr[min_idx])
				min_idx = j;
		}
		Swap(&arr[min_idx], &arr[i]);
	}
}