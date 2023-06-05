#include "lists.h"
#include <stdbool.h>

/**
 * check_cycle - checks if a linked list has a cycle in it or not
 * @list: linked list to check
 *
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *main_pointer = list;
	listint_t *skip_pointer = list;
	bool exit = true;

	if (list == NULL)
		return (0);

	if (main_pointer == NULL || skip_pointer == NULL)
		exit = false;
	else if (skip_pointer->next == NULL)
		exit = false;

	while (exit)
	{
		main_pointer = main_pointer->next;
		skip_pointer = skip_pointer->next->next;
		if (main_pointer == skip_pointer)
			return (1);
		if (main_pointer == NULL || skip_pointer == NULL)
			exit = false;
		else if (skip_pointer->next == NULL)
			exit = false;
	}
	return (0);
}
