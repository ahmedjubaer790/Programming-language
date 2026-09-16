#include <iostream>

using namespace std;

int age[3];

void funcTest()
{
	for (int i=0;i<3;i++)
	{
		cout << age[i] << " ";
	}
	cout << endl;
}

int main (void)
{
	cout << "Enter your ages: ";
	for (int i=0;i<3;i++)
	{
		cin >> age[i];
	}
	
	funcTest();
	
	//cout << age << endl;

	return 0;
}
