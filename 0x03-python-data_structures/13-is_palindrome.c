#include "lists.h"
/**
 * is_palindrome_helper - compare value of current node with value of node
 * at end of linked list
 * @head: pointer to beginning of node
 * @length: size of node
 * @node: node
 * Return: 0.
 */
int is_palindrome_helper(listint_t *head, int length, listint_t **node)
{
	if (head == NULL || length <= 0)
	{
		return (1);
	}
	else if (length == 1)
	{
		*node = head->next;
		return (1);
	}

	if (!(is_palindrome_helper(head->next, length - 2, node)))
	{
		return (0);
	}
	if ((*node)->n == head->n)
	{
		*node = (*node)->next;
		return (1);
	}
	return (1);
}
/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: pointer to beginning of node
 *
 * Return: 0 if not palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *node;
	int length;

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
	node = *head;

	return (is_palindrome_helper(*head, length, &node));
}
