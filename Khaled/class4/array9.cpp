#include <iostream>

using namespace std;

int *myArray;
int elementCount=0;
int currentSize=5;

void resize(int flag)
{
	int *tempHandle = myArray;
	
	int newSize;
	if(flag == 1) 
	{
		newSize = currentSize*2;
	}
	else if (flag ==2) 
	{
		newSize = currentSize/2;
	}
	
	myArray = new int [newSize];
	
	for(int i=0;i<elementCount;i++)
	{
		myArray[i] = tempHandle[i];
	}
	
	delete [] tempHandle;
	
	currentSize = newSize;
}

void printArray()
{
	for(int i=0;i<elementCount;i++)
	{
		cout << myArray[i] << " ";
	}
	cout << endl << "array size: " << currentSize << " #elements: " << elementCount << endl;
}

void insertElement()
{
	if(elementCount == currentSize)
	{
		resize(1);
	}
	
	cout << "Input the element?: " ;
	int input;
	cin >> input;
	myArray[elementCount] = input;
	elementCount++;
	printArray();
}
void deleteElement()
{
	if(elementCount == 0)
	{
		cout << "array empty, cannot delete" << endl;
		return;
	}
	
	elementCount--;
	cout << "deleted last element" << endl;
	
	if(currentSize!=5 && elementCount <= currentSize/2)
	{
		resize(2);
	}
	
	printArray();
}

int main (void)
{	
	
	myArray = new int [currentSize];
	
	while(true){
		cout << "select choice: (1) insert (2) delete (-1) stop" << endl;
		int choice;
		cin >> choice;
		if (choice ==1 ) 
		{
			insertElement();
		}
		else if (choice == 2) 
		{
			deleteElement();
		}
		else break;
	}
	
	delete [] myArray;
	
	return 0;
}
