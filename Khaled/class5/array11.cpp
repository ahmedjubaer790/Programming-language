#include <iostream>
#include <vector>

using namespace std;

int main (void)
{
	vector <int> inputs;
	for(int i=0;i<10;i++){
		int input;
		cin >> input;
		inputs.push_back(input);
	}
	
	cout << "Size: " << inputs.size() << endl;
	
	for(int i=0;i<3;i++){
		//inputs.pop_back();
	}
	
	vector<int>::iterator it = inputs.begin();
	inputs.insert (it+5,2,300);
	
	cout << "Size: " << inputs.size() << endl;
	
	//vector <int> inputs = {1,3,5,7,9};
	
	//inputs.push_back(100);
	//inputs.push_back(200);
	//inputs.pop_back();
	
	//vector<int>::iterator it = inputs.begin();
	//inputs.insert(it+2, 1000);
	//inputs.insert (it,5,300);
	
	//inputs.erase(it+3);
	
	//inputs.clear();
	
	for(int i=0;i<inputs.size();i++){
		cout << inputs[i] << endl;
	}
	
	//inputs.at(2) = 17;
	//cout << inputs.front() << " " << inputs.back() << endl;
	//cout << inputs.at(2) << endl;
	//cout << inputs[2] << endl;
	
	//cout << inputs.size() << endl;
	//inputs.resize(10);
	//cout << inputs.max_size() << endl;
	//cout << inputs.capacity() << endl;
	//if(inputs.empty()) cout << "maalta empty" << endl;
	//else cout << "maal ase" << endl;
	
	
	
	return 0;
}
