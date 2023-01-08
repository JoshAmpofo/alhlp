#include "lists.h"

/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: pointer to beginning of node
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int i, length;
	int *array;
	listint_t *current;

	if (*head == NULL)
	{
		return (1);
	}

	current = *head;
	length = 0;

	while (current != NULL)
	{
		current = current->next;
		length++;
	}

	current = *head;

	array = malloc(sizeof(int) * length);

	for (i = 0; i < length; i++)
	{
		array[i] = current->n;
		current = current->next;
	}

	for (i = 0; i < length / 2; i++)
	{
		if (array[i] != array[length - i - 1])
		{
			return (0);
		}
	}

	return (1);
}
