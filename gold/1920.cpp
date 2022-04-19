#include <iostream>
using namespace std;

int main(){
    int n = 0;
    int idx = 0;
    int arr[100001] = {0,};

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> idx;
        arr[idx] = 1;
    }

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> idx;
        if(arr[idx] == 0){
            cout<<"0\n";
        }
        else{
            cout<<"1\n";
        }
    }
}