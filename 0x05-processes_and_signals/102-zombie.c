#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
* infinite_while - Creates an infinite loop
* Description: Creates an infinite loop
* that will put a sleep within the loop
* Return: number
*/
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
* main - Main Entry Point
* Description: Creates a Zombie process
* Return: Nothing
*/
int main(void)
{
pid_t pid;
int counter = 0;

while (counter < 5)
{
	pid = fork();
	if (pid > 0)
	{
		printf("Zombie process created, PID: %d\n", pid);
		sleep(1);
		counter++;

	}
	else
		exit(0);
}

infinite_while();
return (EXIT_SUCCESS);
}
