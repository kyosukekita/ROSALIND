#include <iostream>
#include <vector>
using namespace std;
vector<long long> memo(50,-1); /*-1で初期化*/

int cnt=0;
long long fibonacci(int n){
    cnt++;
    if (memo[n] != -1) return memo[n];
    return memo[n]= fibonacci(n-1)+ fibonacci(n-2);
}

int main(){
    int n; cin >> n;
    memo[0]=0;
    memo[1]=1;
    cout << fibonacci(n);
    cout << "\n" << cnt;
    return 0;
}