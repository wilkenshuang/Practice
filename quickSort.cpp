// C++版本的快速排序算法

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<stack>

using namespace std;
void quickSort(int a[], int, int);
void insertSort(int arr[],int n);

int main() {
	int arr[] = { 34,65,12,43,67,5,78,10,3,70 };
	int len = sizeof(arr) / sizeof(int);
	quickSort(arr, 0, len - 1);
	for (int k=0;k<len;k++){
		cout << arr[k] << " ";
	}
	cout << endl;
	return 0;
}

void quickSort(int a[],int l, int r){
	if (l<r){
		int i = l, j = r, v = a[l];
		while (i<j&&a[j]>v)
			j--;
		if (i < j)
			a[i++] = a[j];
		while (i < j&&a[i] < v)
			i++;
		if (i < j)
			a[j--] = a[i];
		a[i] = v;
		quickSort(a, 0, i - 1);
		quickSort(a, i + 1, r);
	}
}
void insertSort(int arr[],int n){
	for (int i=1;i<n;i++){
		int j=i;
		while (j>=1&&arr[j-1] > arr[j]){
			int tmp = arr[j-1];
			arr[j-1] = arr[j];
			arr[j] = tmp;
			j--;
		}
	}
}
