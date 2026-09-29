#include <iostream>
using namespace std;
// int age[3];

void funcTest(int *age)
{
    for(int i=0; i<3; i++)
    {
        cout<<age[i]<<" ";
    }
    cout << endl;
}

int main (void)
{
    int age[3];
    cout <<"Enter Age: ";
    for (int i=0; i<3; i++)
    {
        cin>>age[i];
    }
    funcTest(age);

    return 0;
}