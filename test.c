#include <stdio.h>
#include "lib.h"

int main()
{
	SayHello();

	SayGoodbye();

	printf("Result of ReturnInt is %d\n", ReturnInt());

	printf("Result of ReturnFloat is %f\n", ReturnFloat());

	SetStatic(10);
	printf ("Static value is %d\n", GetStatic());
	SetStatic(20);
	printf ("Static value is %d\n", GetStatic());

	char testString[25];
	sprintf (testString, "Old Value");
	printf ("String is %s\n", testString);
	PointerReference(testString);
	printf ("String is now %s\n", testString);

	return 0;
}
