#include<iostream>
using namespace std;

void shellsort(int arr[]  int n){
    for (int gap /=2; gap>0; gap /=2){
        for (int i = gap; i<n; i++){
            int temp = arr[j];
            int j;
            for (j = i; j>= gap; && arr[j-gap] > temp; j -= gap){
            arr[j] = arr[j - gap];
        }
        arr[j] = temp;
    }
  }
}

int main() {
    int arr[] = {9, 5, 2, 7, 1, 8};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Array before sorting: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    shellSort(arr, n);

    cout << "Array after sorting: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}