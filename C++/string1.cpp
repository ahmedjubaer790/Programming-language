#include <iostream>
#include <string>

using namespace std;

int main (void)
{
	string s = "mahTab";
	
	//cin >> s;
	//getline(cin, s);
	
	string s1 = "legend killer";
	
	//cout << s1.size() << endl;
	//cout << s1.length() << endl;
	
	for(int i=0;i<s1.length();i++){
		//cout << s1[i] << endl;
		//cout << s1.at(i) << endl;
	}
	
	//cout << s1.back() << endl << s1.front() << endl;
	
	//cout << s+ " the " + s1 << endl;
	s += "the legend killer";
	cout << s << endl;
	return 0;
}















