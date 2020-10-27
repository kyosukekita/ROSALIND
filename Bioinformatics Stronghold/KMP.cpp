//https://algoful.com/Archive/Algorithm/KMPSearch
//ずらし表の作成は、パターン文字列に対してパターン文字列自身を比較することで求まる
//一致しない時点で何文字一致していたかが、ずらし位置です。


public int KMSearch(string target, string pattern){

    var table = CreateTable(pattern);

    //文字列探索
    int i=0, p=0;
    while (i< target.Length && p < pattern.length()){
        if(target[i]==pattern[p]){
            //文字が一致していれば次の文字にすすむ
            i++; p++;
        }else if (p==0){
            //パターン先頭文字が不一致の場合、次の文字
            i++;
        }else{
            //不一致の場合、パターンのどの位置から再開するか設定
            p=table[p]
        }
    }
    if(p==pattern.length()){
        return i-p;
    }
    return -1;
}





//ずらし表の作成
public int[] createTable(string pattern){
    var table= new int[pattern.length()];
    table[0]=0;

    var j=0;//直前までに何文字一致していたか
    for (int i=1; i< pattern.length();i++){
        if(pattern[i]==pattern[j]){
            table[i]=j++
        }else{
            table[i]=j;
            j=0;
        }
    }

    return table;
}
