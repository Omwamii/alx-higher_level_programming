#include "lists.h"

/**
  *check_cycle - checks if a singly linked list has a cycle
  *@list: list passed
  *
  *Return: 0 if no cycle, 1 if has cycle
  */

int check_cycle(listint_t *list)
{
	listint_t *current;

	current =  list;

	if (current == NULL)
		return (0);

	current = current->next;
	while (1)
	{
		if (current == list)
			return (1);
		if (current == NULL)
			return (0);

		current = current->next;
	}
}
