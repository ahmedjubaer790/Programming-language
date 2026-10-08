#include <iostream>
#include <stack>

using namespace std;

int main (void)
{
	stack <int> myStack;
	cout << "Initial Size: " << myStack.size() << endl;
	
	for (int i=0;i<5;i++){
		int input;
		cin >> input;
		myStack.push(input);
	}
	cout << "After 5 pushes Size: " << myStack.size() << endl;
	
	myStack.pop();
	myStack.pop();
	myStack.push(999);
	myStack.push(7);
	
	stack <int> myStack1;
	
	for (int i=0;i<3;i++){
		myStack1.push(i*10);
	}
	
	myStack.swap(myStack1);
	
	while(!myStack.empty()){
		cout << myStack.top() << endl;
		myStack.pop();
	}
	
	while(!myStack1.empty()){
		cout << "\t" << myStack1.top() << endl;
		myStack1.pop();
	}
	
	return 0;
}
