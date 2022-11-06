//https://qiita.com/drken/items/97e37dd6143e33a64c8c

#include <iostream>
#include <vector>
using namespase std;

vector<int> a={1, 14, 32, 51, 51, 51, 243, 419, 750, 910}

//目的の値keyのindexを返す。ない場合は-1

//一般的な二分探索
int binary_search(int key){
    int left=0, right=(int)a.size()-1;
    while(right >=left){
        int mid = left+(right-left)/2;
        if (a[mid]==key) return mid;
        else if (a[mid]>key) right=mid-1;
        else if (a[mid]<key) left=mid+1;
    }
    return -1;
}


int main(){
    cout << binary_search(51) << endl; // a[4] = 51 (他に a[3], a[5] も)
    cout << binary_search(1) << endl; // a[0] = 1
    cout << binary_search(910) << endl; // a[9] = 910

    cout << binary_search(52) << endl; // -1
    cout << binary_search(0) << endl; // -1
    cout << binary_search(911) << endl; // -1
}



//汎用的な二分探索, lower_bound()は、配列aのindexのうちkey以上となる最小のindexを返す

//indexが条件を満たすかどうか
bool isOK(int index, int key){
    if (a[index] >=key) return true;
    else return false;
}

//汎用的な二分探索のテンプレ
int binary_search(int key){
    int left=-1;//「index = 0」が条件を満たすこともあるので、初期値は -1
    int right=(int)a.size(); //// 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    /* どんな二分探索でもここの書き方を変えずにできる！ */
    while (right - left > 1) {
        int mid = left + (right - left) / 2;

        if (isOK(mid, key)) right = mid;
        else left = mid;
    }

    /* left は条件を満たさない最大の値、right は条件を満たす最小の値になっている */
    return right;
}

//上のプロトコルは「ソート済配列の中での探索」に限らず様々な問題に活用することができる
//求めたい境目を境にして「左側はすべて偽で、右側はすべて真」である。


