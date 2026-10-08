#include <iostream>
using namespace std;

int sum(int a,int b){
    return(a+b);
}

int sub(int a, int b) {
    return(a-b);
}

int mul(int a ,int b){
    return(a*b);
}

int div(float a,int b){
    return(a/b);
}

float div2(int a, int b){
    return (float(a)/b);
}

int main (void){
    char ch;
    int i;
    float f;
    double d;
    bool b;

    // funtions
            // int x,y;
            // cout << "Type the x value: ";
            // cin >> x;
            // cout << "Type the y value: ";
            // cin >> y;
            // cout<< "The sum value is "<<sum(x,y)<<endl;

            cin>>ch;
            switch (ch)
            {
            case 'a':cout<<"its a"<<endl; break;
            case 'b':cout<<"its b"<<endl; break;  
            
            
            default:cout<<"Its none"<<endl;
              
            }
    cin >>i;
    switch (i)
    {
    case 100: cout<< "its 100"<<endl; break;
       
        
    
    default:cout<<"its nothing"<< endl; break;
        
    } 
return 0;           
}