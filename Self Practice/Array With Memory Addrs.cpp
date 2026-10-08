#include <iostream>
using namespace std;

int main (void){
    int arr[5]={11,23,45,65,9};
    for(int i=0;i<5;i++)
    {
        cout<<*(arr+i)<<" ";
    }
    cout<<endl;

    for(int i=0;i<5;i++)
    {
        cout<<(arr+i)<<" ";
    }
    cout<<endl;

    for(int i=0;i<5;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;

}