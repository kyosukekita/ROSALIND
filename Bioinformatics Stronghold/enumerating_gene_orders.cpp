#include <bits/stdc++.h>
using namespace std;
 
int factorialMethod(int k){
  int sum=1;
  for(int i=1; i<=k;i++){
    sum*=i;
  }
  return sum;
}


int main() {
  int N;
  cin >> N;
  
  cout << factorialMethod(N) << endl;
  
  vector<int> vec(N);
  for(int i=0;i<N;i++){
    vec.at(i)=i+1;
  }
  
  sort(vec.begin(), vec.end());
  do {
    for (int x : vec) {
      cout << x << " ";
    }
    cout << endl;
  } while (next_permutation(vec.begin(), vec.end()));
}
