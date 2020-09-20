#include <stdio.h>

void swap(int *p_from, int *p_to){
    int tmp;
    tmp=*p_from;
    *p_from =*p_to;
    *p_to = tmp;
}


void insertionSort (int array[], int array_size){
    int i,j;

    for (i=1; i < array_size; i++){
        j=i;

        while ((j>0) && (array[j-1]>array[j])){
            swap(&array[j-1], &array[j]);
            j--;
        }
    }
}

int main(void){
    int i;
    int array[10] ={3,6,1,7,2,0,4,5,9,8};

    insertionSort(array, sizeof(array) / sizeof(array[0]));

    printf("sorted array:");
    for (i=0; i<sizeof(array) / sizeof(array[0]); i++){
        printf("%d", array[i]);
    }
    print("\n");

    return 0;
}