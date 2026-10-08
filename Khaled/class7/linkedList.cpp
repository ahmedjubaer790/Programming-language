#include <iostream>

using namespace std;

struct Node{
	string name;
	int roll;
	Node *next;
	Node *previous; 
};

Node *head;
Node *tail;

void initNewLinkedList(void){
	head = NULL;
	tail = NULL;
}

bool isEmpty(void){
	if(head == NULL && tail ==NULL) return true;
	else return false;
}

Node* createNode(string name, int roll){
	Node  *firstNode = new Node[1];
	firstNode[0].name = name;
	firstNode[0].roll = roll;
	firstNode[0].next = NULL;
	firstNode[0].previous = NULL;
	
	return firstNode;
}

void insertNodeAtEndOfList(string name, int roll){
	Node *newNode = createNode(name, roll);
	//cout << newNode->name <<"\t" << newNode->roll << endl;
	if(head == NULL && tail ==NULL)
	{
		head = newNode;
		tail= newNode;
	}
	else{
		//cout << "###########" << endl;
		tail->next = newNode;
		newNode->previous = tail;
		tail = newNode;
	}
	//cout << "Head: " << head << "\tTail: " << tail << "\tCurrent: " << newNode << endl; 
}

void insertNodeAtStartOfList(string name, int roll){
	Node *newNode = createNode(name, roll);
	if(head == NULL && tail ==NULL)
	{
		head = newNode;
		tail= newNode;
	}
	else{
		//cout << "###########" << endl;
		//tail->next = newNode;
		//newNode->previous = tail;
		//tail = newNode;
		newNode->next = head;
		head->previous = newNode;
		head = newNode;
	}
}

void printNode(Node *current){
	cout << current->name << "\t" << current->roll << endl;
}

void traverseLinkedList(void){
	Node *current = head;
	while(current != tail){
		printNode(current);
		current = current->next;
	}
	printNode(current);
}

void destroyLinkedList(){
	if(head == NULL && tail ==NULL) {}
	else{
		Node *current = head;
		while(current != tail){
			Node *maiyat = current;
			current = current->next;
			delete [] maiyat;
		}
		delete [] current;
		head = NULL;
		tail = NULL;
	}
}

void traverseLinkedListReverse(void){
	Node *current = tail;
	while(current != head){
		printNode(current);
		current = current->previous;
	}
	printNode(current);
}

Node* searchByRoll(int key){
	Node *current = head;
	while(current != tail){
		if(current->roll == key) return current;
		current = current->next;
	}
	if(current->roll == key) return current;
	else return NULL;
}

void insertAfter(int key, string name, int roll){
	Node *temp = searchByRoll(key);
	if (temp == NULL) cout << "Does Not Exist on the List, Not inserting" << endl;
	else{
		Node *newNode = createNode(name, roll);
		if(temp == tail){
			tail->next = newNode;
			newNode->previous = tail;
			tail = newNode;
		}
		else{
			newNode->previous = temp;
			newNode->next = temp->next;
			temp->next = newNode;
			newNode->next->previous = newNode;
		}
	}
}

void insertBefore(int key, string name, int roll){
	Node *temp = searchByRoll(key);
	if (temp == NULL) cout << "Does Not Exist on the List, Not inserting" << endl;
	else{
		Node *newNode = createNode(name, roll);
		if(temp == head){
			newNode->next = head;
			head->previous = newNode;
			head = newNode;
		}
		else{
			newNode->previous = temp->previous;
			newNode->next = temp;
			temp->previous = newNode;
			newNode->previous->next = newNode;
		}
	}
}

void deleteElementByRoll(int key){
	Node *temp = searchByRoll(key);
	if (temp == NULL) cout << "Does Not Exist on the List, Not deleting" << endl;
	else {
		if(temp == head) {
			Node *maiyat = head;
			head = head->next;
			delete [] maiyat;
		}
		else if (temp == tail) {
			Node *maiyat = tail;
			tail = tail->previous;
			delete [] maiyat;
		}
		else {
			Node *maiyat = temp;
			temp->previous->next = temp->next;
			temp->next->previous = temp->previous;
			delete [] maiyat;
		}
	}
}

int main (void)
{
	initNewLinkedList();
	//cout << "Head: " << head << "\tTail: " << tail << endl; 
	
	insertNodeAtEndOfList("Arif",1);
	insertNodeAtEndOfList("Shafayat",2);
	insertNodeAtEndOfList("Jubaer",3);
	insertNodeAtEndOfList("Ahsan",4);
	
	insertNodeAtStartOfList("Khaled",0);
	insertNodeAtStartOfList("Sakib",-1);
	insertNodeAtStartOfList("Zerin",-2);
	
	//traverseLinkedList();
	
	Node *temp = searchByRoll(3);
	//if (temp == NULL) cout << "Does Not Exist on the List" << endl;
	//else cout << "Found "<< temp->name << "\t" << temp->roll <<endl;
	
	//insertAfter(4, "Apa", 6);
	//insertBefore(-2, "Apa", 6);
	//traverseLinkedListReverse();
	
	
	//?? searchByRollReverse(3);
	//?? searchByName("Ahsan");
	//?? searchByNameReverse("Ahsan");
	
	deleteElementByRoll(1);
	deleteElementByRoll(0);
	cout << "################" << endl;
	traverseLinkedList();
	
	destroyLinkedList();
	
	//?? deleteElementByName("Ahsan");
	
	return 0;
}
