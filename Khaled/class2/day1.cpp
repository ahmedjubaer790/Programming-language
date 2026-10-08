#include <iostream>

using namespace std;

int sum(int a, int b){
	return (a+b);
}

int sub(int a, int b){
	return a-b;
}

int mul(int a, int b){
	return a*b;
}

float div1(int a, int b){
	return ((float) a)/b; // type casting
}

float div2(float a, int b){
	return a/b; // type casting
}

int main (void)
{
	//cout << "Test" << endl;
	/*Data Type*/
	char ch; //8 bit
	int i; //32 bit
	float f; //32 bit
	double d; //64 bit
	bool b; //0 or 1 => true or false

	
	/* value and address of a variable
	cin >> i;
	cout << i << endl; //prints the value
	cout << &i << endl; //prints the address
	//cout << *i << endl; ==> this cannot be done
	*/
	
	/* types of characters
	char ch1;
	signed char ch2;
	unsigned char ch3;
	cin >> ch3;
	cout << ch3 << endl;
	*/
	
	/* types of integer
	int i1;
	//signed int i2;  ==> same as int
	unsigned int i3;
	long int i4;
	//signed long int i5; ==> same as long int
	unsigned long int i6;
	cin >> i6;
	cout << i6 << endl;
	*/
	
	/* if-else if-else
	if(i>5) cout << i << endl;
	else if(i==5) cout << "five" << endl;
	else cout << "none" << endl;
	*/
	
	/* switch-case
	cin >> ch;
	switch (ch){
		case 'a': cout << "its a" << endl; break;
		case 'b': cout << "its b" << endl; break;
		case 'c': cout << "its c" << endl; break;
		default: cout << "its none" << endl;
	}
		
	cin >> i;
	switch (i){
		case 100: cout << "its 100" << endl; break;
		case 200: cout << "its 200" << endl; break;
		case 300: cout << "its 300" << endl; break;
		default: cout << "its none" << endl;
	}
	*/
	
	/* loops
	for(i=0;i<10;i++)
	{
		cout << i << endl;
	}
	
	i=20;
	while (i<30){
		cout << i << endl;
		i++;
	}
	
	i=40;
	do{
		cout << i << endl;
		i++;
	}while(i<50);
	*/
	
	/*arithmetic operations: + - * / %
	int x, y, result;
	cin >> x >> y;
	result = x/y;
	cout << result << " " << (x%y)<< endl;
	*/
	
	/*functions
	int x, y;
	cin >> x >> y;
	cout << sum(x,y) << endl;
	cout << sub(x,y) << endl;
	cout << mul(x,y) << endl;
	cout << div1(x,y) << endl;
	cout << div2(x,y) << endl;
	*/
	
	return 0;
}
