#include <iostream>
using namespace std;
void funcTest(int *age, int noOfstudens)
{
    for(int i=0;i<noOfstudens;i++)
    {
        cout<< age[i]<< " ";
    }
    cout << endl;
}

int main (void){
    int noOfstudens;
    cout<< "How Many Students? ";
    cin>> noOfstudens;

    int *age;
    age= new int[noOfstudens];

    cout <<"Enter Your age ";
    for(int i=0; i<noOfstudens; i++)
    {
        cin>>age[i];
    }
    funcTest(age, noOfstudens);
    delete[] age;

    return 0;
}