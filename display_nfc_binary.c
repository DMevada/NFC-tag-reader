#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	int sleep_time = 7;

	if (argc == 2)
	{
		printf("Argument from python is: %s\n", argv[1]);
		printf("Sleeping for %d seconds\n", sleep_time);

		sleep(sleep_time);
	}

	else if (argc > 2)
	{
		printf("Too many arguments supplied \n");
		return 0;
	}

	else
	{
		printf("One argument expected. \n");
	}	

	printf("\n");
	return 0;
}