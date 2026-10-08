#include <iostream>
using namespace std;
void PrintWithref(int &j){
    cout<<j<<endl;
}

int main (void){
    int i;
    cin>>i;
    PrintWithref(i);
    return 0;
}