#include <iostream>
using namespace std;

int i;
void printI(){
    cout <<"Enter The value of I is: " << i << endl;
    cout <<"The memory address is: " << &i << endl;
}

int main (void)
{
    cin >> i;
    cout << i << endl;
    cout << &i << endl;
    printI();
    return 0;

}