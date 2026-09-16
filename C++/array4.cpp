#include <iostream>

using namespace std;

void funcTest(int *age)
{
	for (int i=0;i<3;i++)
	{
		cout << age[i] << " ";
	}
	cout << endl;
}

int main (void)
{
	int age[3];
	cout << "Enter your ages: ";
	for (int i=0;i<3;i++)
	{
		cin >> age[i];
	}
	
	funcTest(age);
	
	//cout << age << endl;

	return 0;
}
