#include <iostream>
using namespace std;

//値を交換する関数
void swap(int *a, int *b){
  int temp=*a;
  *a=*b;
  *b=temp;
}

//クイックソート
void QuickSort(int A[], int left, int right){
  int Left, Right;
  int pivot;
  
  //初期化
  Left=left; Right=right;
  
  //基準は真ん中
  pivot=A[(left+right)/2];
  
  while (1){
    //基準より小さい値を左から見つける
    while (A[Left]<pivot) Left++;
    
    //基準より大きい値を右から見つける
    while (pivot < A[Right]) Right--;
    
    //見つかった値の順序が逆になったら終了
    if (Left>=Right) break;
    
    //値を交換
    swap(&A[Left],&A[Right]);
    
    Left++;Right--;
  }
  
  //左のデータ群を対象としてクイックソートを再帰
  if (left < Left - 1) QuickSort(A, left, Left - 1);

  //右のデータ群を対象としてクイックソートを再帰
  if (Right + 1 < right) QuickSort(A, Right + 1, right);

}

int main() {
  int N;
  cin >> N;
  
  int arr[50];//作業用スペース
  for(int i=0; i<N;i++){
    cin >> arr[i];
  }
  
  QuickSort(arr,0,N-1);
  
  for(int i=0; i<N;i++){
    cout << arr[i] << " ";
  }
}
