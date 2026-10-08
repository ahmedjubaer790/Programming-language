#include <iostream>
using namespace std;

void funcTest(int *age, int NoOfstduents){

    for(int i=0;i<NoOfstduents;i++){
        
        cout<<age[i]<<" ";
    }
    cout<<endl;
}

int main (void){
    int NoOfstduents;
    cout<<"How many student"<<endl;
    cin>>NoOfstduents;

    int *age;
    age=new int[NoOfstduents];

    cout<<"Enter your ages: ";
    for(int i=0;i<NoOfstduents;i++){
        cin>>age[i];
    }
    funcTest(age,NoOfstduents);
    delete [] age;
    return 0;
}
