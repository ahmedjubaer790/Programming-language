#include <iostream>
using namespace std;

//array declare
int age[3];

//function
void funcTest(){
    for (int i=0;i<3;i++) //loop
    {cout<<"The age are: "<<age[i]<< " " << endl;
    }
    cout <<endl;
}

int main (void){
    cout <<"Enter Your age: ";
    //loop for take input 3 
    for(int i=0; i<3; i++)
    {
        cin>>age[i];
    }
    funcTest();
    return 0;
}