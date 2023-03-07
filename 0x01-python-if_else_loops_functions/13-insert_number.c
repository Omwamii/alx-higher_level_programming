#include "lists.h"

/**
 * insert_node - adds a new node in a sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *walk, *jump;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		walk = current;
		jump = current->next;
		while(jump)
		{
			if (number < walk->n  && number < jump->n) /* value is less than both */
			{
				current = new;
				new->next = walk;
				break;
			}
			if (number > walk->n && number < jump->n)/* insert in-between */
			{
				walk->next = new;
				new->next = jump;
				break;
			}

			walk = walk->next;
			jump = jump->next;
		}
	}
	*head = current;
	return (new);
}
