#include <iostream>

using namespace std;

int factorial(int input){
	if(input == 1) return 1; 
	else return factorial(input-1)*input;
}

int main (void)
{
	int input;
	cin >> input;
	cout << factorial(input) << endl;
	
	/*
	int output=1;
	for (int i=1; i<=input; i++){
		output = output*i;
	}
	
	cout << output << endl;
	*/
	return 0;
}
