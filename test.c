#include <stdio.h>
#include "lib.h"

void HeaderMessage (char *message)
{
	printf ("\n__%s__\n", message);
}

int main()
{
	HeaderMessage("Simple Printing");
	SayHello();

	SayGoodbye();

	HeaderMessage("Returning Numbers");
	printf("Result of ReturnInt is %d\n", ReturnInt());

	printf("Result of ReturnFloat is %f\n", ReturnFloat());

	HeaderMessage("Statics");
	SetStatic(10);
	printf ("Static value is %d\n", GetStatic());
	SetStatic(20);
	printf ("Static value is %d\n", GetStatic());

	HeaderMessage("Pointer References");
	char testString[25];
	sprintf (testString, "Old Value");
	printf ("String is %s\n", testString);
	PointerReference(testString);
	printf ("String is now %s\n", testString);

	return 0;
}
