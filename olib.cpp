#include <stdio.h>
#include "lib.h"

static int staticVar;

class OLib
{
public:
	void SayHello()
	{
		printf ("Hello, world!\n");
	}

	void SayGoodbye()
	{
		printf ("Goodbye, cruel world!\n");
	}

	int GetStatic()
	{
		return staticVar;
	}

	void SetStatic (int newVal)
	{
		staticVar = newVal;
	}

	int ReturnInt()
	{
		return 10;
	}

	float ReturnFloat()
	{
		return 25.22343;
	}

	void PointerReference (char *inputString)
	{
		sprintf (inputString, "New Value");
	}
};


