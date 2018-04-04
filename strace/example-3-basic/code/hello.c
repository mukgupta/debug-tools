#include <stdio.h>

int main () {
	printf("Hello World!\n");

	FILE *fptr;
	fptr = fopen("hello.txt", "w");

	fprintf(fptr, "%s", "Writing to file!");

	fclose(fptr);

	fprintf(stderr, "%s", "Writing to stderr!");

	return 0;
}