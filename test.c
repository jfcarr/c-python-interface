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

	return 0;
}
