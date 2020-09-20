#binary search

int binary_search(int v){
    int left=0;
    int right =(int)a.size()-1;

    while(right -left>1){
        int mid =(left+right)/2;

        if(a[mid]>=v) right=mid;
        else left=mid;
    }

    return right;
}