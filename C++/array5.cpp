#include <iostream>

using namespace std;

void funcTest(int *age, int noOfStudents)
{
	for (int i=0;i<noOfStudents;i++)
	{
		cout << age[i] << " ";
	}
	cout << endl;
}

int main (void)
{
	int noOfStudents;
	cout << "How many students? ";
	cin >> noOfStudents;
	
	int *age;
	age = new int[noOfStudents];
	
	cout << "Enter your ages: ";
	for (int i=0;i<noOfStudents;i++)
	{
		cin >> age[i];
	}
	
	funcTest(age, noOfStudents);
	
	delete [] age;

	return 0;
}
