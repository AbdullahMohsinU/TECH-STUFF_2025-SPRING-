#include <iostream>
#include "my.h"
#include<string>
using namespace std;

int main()
{
	calculator calc;
	cout << "Hello World!\n";
	cout << calc.addition(4, 25) << endl;
	cout << calc.Subtract(60, 90) << endl;
	cout << calc.Multiply(20, 12) << endl;
	cout << calc.classify("aba");

}