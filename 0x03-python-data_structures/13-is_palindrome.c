#include "lists.h"
#include <string.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

int compare_int(int a[], int b[], size_t size);
/**
 * is_palindrome - checks if single list has palindrome
 * @head: pointer to pointer to first node
 *
 * Return: 0 if not, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *fwd, *rev;
	size_t i = 0;
	size_t size = sizeof(int);
	void *wd;
	int j, num;

	if (current == NULL) /* empty list */
		return (1);


	fwd = malloc(size);
	while (current->next != NULL)
	{
		size += sizeof(int);
		fwd[i++] = (current->n);
		current = current->next;
		wd = realloc(fwd, size);
		if (!wd)
			return (-1);
	}
	fwd[i] = current->n;
	j = i;
	i = 0;
	rev = malloc(size);
	for (; j >= 0; j--, i++)
		rev[i] = fwd[j];
	num = compare_int(fwd, rev, (size / sizeof(int)));
	free(fwd), free(rev);
	return (num);
}

/**
 * compare_int - compares integer to check equality
 * @a: first array
 * @b: reversed array
 * @size: array size
 *
 * Return: 0 if not equal, else 1
 */
int compare_int(int *a, int *b, size_t size)
{
	size_t i = 0;

	for (; i < size; i++)
	{
		if (a[i] != b[i])
			return (0);
	}

	return (1);
}
