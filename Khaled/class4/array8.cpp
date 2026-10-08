#include <iostream>

using namespace std;

void printArray(int *myArray, int elementCount)
{
	for(int i=0;i<elementCount;i++)
	{
		cout << myArray[i] << " ";
	}
	cout << endl;
}

void insertElement(int *myArray, int &elementCount, int currentSize)
{
	if(elementCount == currentSize)
	{
		cout << "array full, cannot input more" << endl;
		return;
	}
	
	cout << "Input the element?: " ;
	int input;
	cin >> input;
	myArray[elementCount] = input;
	elementCount++;
	printArray(myArray, elementCount);
}
void deleteElement(int *myArray, int &elementCount, int currentSize)
{
	if(elementCount == 0)
	{
		cout << "array empty, cannot delete" << endl;
		return;
	}
	
	elementCount--;
	cout << "deleted last element" << endl;
	printArray(myArray, elementCount);
}

int main (void)
{	
	int *myArray;
	int elementCount=0;
	int currentSize=5;
	myArray = new int [currentSize];
	
	while(true){
		cout << "select choice: (1) insert (2) delete (-1) stop" << endl;
		int choice;
		cin >> choice;
		if (choice ==1 ) 
		{
			insertElement(myArray, elementCount, currentSize);
		}
		else if (choice == 2) 
		{
			deleteElement(myArray, elementCount, currentSize);
		}
		else break;
	}
	
	delete [] myArray;
	
	return 0;
}
