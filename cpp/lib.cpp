#include <iostream>
#include "lib.h"

using namespace std;

void CGreeter::SayHello()
{
	cout << "Hello!" << endl;
}

void CGreeter::SayGoodbye()
{
	cout << "Goodbye!" << endl;
}

extern "C" {
	CGreeter* CGreeter_new()
	{
		return new CGreeter() ;
	}
	void CGreeter_Hello(CGreeter * greeter )
	{
		greeter->SayHello();
	}
	void CGreeter_Goodbye(CGreeter * greeter )
	{
		greeter->SayGoodbye();
	}
}
