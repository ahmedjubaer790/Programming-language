#include <iostream>

using namespace std;

void printIwithRefrence(int &j){
	cout << *j  << endl;
	cout << j << endl;
}

int main (void)
{
	int i;
	cin >> i;
	cout << i << endl; //prints the value
	cout << &i << endl; //prints the address

	printIwithRefrence(&i);
	
	return 0;
}
