#include <stdio.h>

int main () {
	FILE *fptr;

	fptr = fopen("hello.txt", "w");

	fprintf(fptr, "%s", "Hello World!");

	fclose(fptr);

	return 0;
}