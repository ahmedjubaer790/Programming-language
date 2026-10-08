#include <iostream>
using namespace std;
void printIwithPointer(int *j){
    cout<<*j<<endl;
    cout<<j<<endl;
}

int main (void){
    int i;
    cin>>i;
    // cout<<i<<endl;
    printIwithPointer(&i);
    return 0;
}