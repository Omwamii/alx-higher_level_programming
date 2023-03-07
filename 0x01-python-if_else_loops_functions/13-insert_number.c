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
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL && number > current->next->n)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
