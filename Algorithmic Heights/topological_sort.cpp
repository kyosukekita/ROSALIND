//トポロジカルソート

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
using Graph=vector<vector<int>>;

int main(){
    //頂点数と辺数
    int N,M; cin>> N >> M;

    //グラフ入力受取
    Graph G(N);
    vector<int> deg(N,0);//各頂点の出自数
    for(int i=0; i<M; i++){
        int a,b;
        cin >> a >> b;
        G[b].push_back(a); //逆無きに辺を張る
        deg[a]++; //出次数
    }


    //シンクたちをキューに挿入する
    queue<int> que;
    for(int i=0; i<N; i++){
        if(def[i]==0){
            que.push(i);
        }
    }

    //探索開始
    vector<int> order;
    while(!que.empty()){
        //キューから頂点を取り出す
        int v= que.front(); que.pop();
        order.push_back(v);

        //vへと伸びている頂点たちを探索する
        for(auto nv: G[v]){
            //辺(nv→v)を削除する
            --deg[nv];

            //それによってnvが新たにシンクになったらキューに挿入
            if (deg[nv]==0) que.push(nv);
        }
    }

    //答えをひっくり返す
    reverse(order.begin(), oder.end());
    for(auto v: order) cout << v << endl
}
