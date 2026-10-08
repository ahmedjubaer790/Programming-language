#include <iostream>
using namespace std;

void FuncTest(int *age){
    for(int i=0;i<3;i++){
        cout<<age[i]<<" ";
    }
    cout<<endl;
}

int main (void){
    int age[3];
    cout<<"Enter Your name"<<endl;
    for(int i=0;i<3;i++){
        cin>>age[i];
    }
    FuncTest(age);
    return 0;
}