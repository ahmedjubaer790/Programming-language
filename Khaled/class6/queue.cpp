#include <iostream>
#include <queue>

using namespace std;

int main (void)
{
	queue <int> mQ;
	cout << "Initial Size: " << mQ.size() << endl;
	
	for (int i=0;i<5;i++){
		int input;
		cin >> input;
		mQ.push(input);
	}
	cout << "After 5 pushes Size: " << mQ.size() << endl;
	
	mQ.pop();
	mQ.pop();
	mQ.push(999);
	mQ.push(9999);
	
	while(!mQ.empty()){
		cout << mQ.front() << "\t" << mQ.back() << "\t Size: " << mQ.size()<< endl;
		mQ.pop();
	}
	
	return 0;
}
