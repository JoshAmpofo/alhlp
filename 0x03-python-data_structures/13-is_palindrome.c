#include "lists.h"

/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: pointer to beginning of node
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int i, length, top;
	int *stack;
	listint_t *current;

	if (*head == NULL)
		return (1);

	current = *head;
	length = 0;

	while (current != NULL)
	{
		current = current->next;
		length++;
	}

	current = *head;

	stack = malloc(sizeof(int) * length);
	top = -1;

	for (i = 0; i < length / 2; i++)
	{
		stack[++top] = current->n;
		current = current->next;
	}

	if (length % 2 != 0)
		current = current->next;
	for (i = 0; i < length / 2; i++)
	{
		if (stack[top--] != current->n)
			return (0);
		current = current->next;
	}
	return (1);
}
