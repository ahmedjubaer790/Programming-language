#include <iostream>

using namespace std;

int fibonacci(int input){
	if(input == 0) return 0;
	else if(input == 1)  return 1;
	else return fibonacci(input-1)+fibonacci(input-2);
}

int main (void)
{
	int input;
	cin >> input;
	cout << fibonacci(input) << endl;
	/*
	for (int i=0; i<=input; i++){
		cout << fibonacci(i) << "  ";
	}
	cout << endl;
	*/
	
	return 0;
}
