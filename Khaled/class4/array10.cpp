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

void copyArray(int *tempArr)
{
	for(int i=0;i<elementCount;i++)
	{
		tempArr[i] = myArray[i];
	}
}

int insertElementAtPosition(int input, int position)
{
	if(position > elementCount || position < 0)
	{
		cout << "invalid position, cannot insert" << endl;
		return 1;
	} 
	if(position == elementCount)
	{
		myArray[position] = input;
	}
	else
	{
		int *tempArr = new int [elementCount];
		copyArray(tempArr);

		for(int i=0;i<position;i++)
		{
			myArray[i] = tempArr[i];
		}
		
		myArray[position] = input;
		
		for(int i=position;i<elementCount;i++)
		{
			myArray[i+1] = tempArr[i];
		}
		
		delete [] tempArr;
		
	}
	return 0;
}

void insertElement()
{
	if(elementCount == currentSize)
	{
		resize(1);
	}
	
	cout << "Input the position?: " ;
	int position;
	cin >> position;
	
	cout << "Input the element?: " ;
	int input;
	cin >> input;

	int success = insertElementAtPosition(input, position);
	if (success == 0) elementCount++;
	printArray();
}

void deleteElement()
{
	if(elementCount == 0)
	{
		cout << "array empty, cannot delete" << endl;
		return;
	}
	
	cout << "Input the position?: " ;
	int position;
	cin >> position;
	
	if(position >= elementCount || position < 0)
	{
		cout << "invalid position, cannot delete" << endl;
	}
	else
	{
		for(int i=position;i<elementCount-1;i++)
		{
			myArray[i] = myArray[i+1];
		}
		elementCount--;
	}
	
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
		if (choice ==1) 
		{
			insertElement();
		}
		else if (choice == 2) 
		{
			deleteElement();
		}
		else if (choice == -1) break;
		else cout << "muri kha" << endl;
	}
	
	delete [] myArray;
	
	return 0;
}
