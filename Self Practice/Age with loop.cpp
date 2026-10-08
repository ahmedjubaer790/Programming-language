#include <iostream>
using namespace std;
int age[3];
void funcTest(){
    for(int i=0;i<3;i++){
        cout<<age[i]<<" ";
    }
    cout<<endl;
}

int main (void){
    cout<<"Enter Your age"<<endl;
    for(int i=0;i<3;i++){
        cin>>age[i];
    }
    funcTest();
    return 0;

}