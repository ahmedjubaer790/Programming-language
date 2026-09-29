#include <iostream>

using namespace std;

void PrintWithRef(int *j){
    cout <<"Value of j: "<< *j << endl;
    cout << "Memory address: "<< j << endl;
}

int main (void){
    int i;
    cout << "Enter The value: " << endl;
    cin >> i;
    cout << "The value is:  " << i << endl;
    cout << "The memory address is: "<< &i << endl;
    PrintWithRef(&i);
    return 0;
}