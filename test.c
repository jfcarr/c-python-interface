#include <stdio.h>
#include "lib.h"

int main()
{
	SayHello();

	SayGoodbye();

	printf("Result of ReturnInt is %d\n", ReturnInt());

	printf("Result of ReturnFloat is %f\n", ReturnFloat());

	return 0;
}
