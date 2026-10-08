#include <iostream>
using namespace std;

void  printArray(int *myArray, int elementcount){
    for(int i=0;i<elementcount;i++)
    {
        cout<<myArray[i]<<" ";
    }
    cout<<endl;
}

void insertElement(int *myArray, int &elementcount, int currentsize){
    if (elementcount==currentsize){
        cout<<"array full"<<endl;
        return;
    }
    cout<<"input the insert element: ";
    int input;
    cin>>input;
    myArray[elementcount]=input;
    elementcount++;
    printArray(myArray,elementcount);
}

void deleteelemnt(int *myArray,int &elementcount, int currentsize){
    if(elementcount==0){
        cout<<"Array Is empty cant dlt"<<endl;
        return;
    }
    elementcount--;
    cout<<"delete last elemnt"<<endl;
    printArray(myArray,elementcount);
}

int main (void){
    int *myArray;
    int elementcount=0;
    int currentsize=5;
    myArray=new int [currentsize];

    while(true){
        cout<<"select choice: (1) insert (2) delete "<<endl;
        int choice;
        cin>>choice;
        if(choice==1){
            insertElement(myArray,elementcount,currentsize);
        }
        else if(choice=2){
            deleteelemnt(myArray,elementcount,currentsize);
        }
        else break;
    }
    delete[] myArray;
    return 0;
}