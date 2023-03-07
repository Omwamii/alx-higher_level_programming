#include "lists.h"

/**
  *check_cycle - checks if a singly linked list has a cycle
  *@list: list passed
  *
  *Return: 0 if no cycle, 1 if has cycle
  */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;
	while (fast != NULL && fast->next != NULL)
	{
		if (fast == slow || fast->next == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}

