#include <iostream>

int main()
{
    using namespace std;
    int    a;
    int    b;
    
    cin >> a >> b;
    if (a > b)
        cout << ">";
    else if (a < b)
        cout << "<";
    else
        cout << "==";
}