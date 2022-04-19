#include <iostream>
using namespace std;

int main(){
    int Y, X, B;
    cin >> Y >> X >> B;

    int **list2d;
    list2d = new int*[Y];

    for (int i = 0; i < Y; i++){
        list2d[i] = new int[X];
    }

    for (int i = 0; i < Y; i++){
        for (int j = 0; j < X; j++){
            cin >> list2d[i][j];
        }
    }

    for (int i = 0; i < Y; i++){
        for (int j = 0; j < X; j++){
            cout<<list2d[i][j]<<" ";
        }
        cout<<"\n";
    }
    for(int i = 0; i < Y; i++){
        delete [] list2d[i];
    }
    delete [] list2d;

}