#include <iostream>

using namespace std;

int i;

void printI(){
	cout << i  << endl;
	cout << &i << endl;
}

int main (void)
{
	//int i;
	cin >> i;
	cout << i << endl; //prints the value
	cout << &i << endl; //prints the address
	//cout << *i << endl; ==> this cannot be done
	printI();
	
	return 0;
}
