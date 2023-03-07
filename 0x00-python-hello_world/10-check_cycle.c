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
	listint_t *temp, *temp_cpy;

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

		temp = current;
		temp_cpy = temp;
		temp = temp->next;
		while (temp) /* check for cycle within list */
		{
			if (temp == temp_cpy)
				return (1);
			temp = temp->next;
		}
		current = current->next;
	}
}
