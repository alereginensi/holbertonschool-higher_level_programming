#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	while (*head != NULL)
	{
		if ((*head)->next != NULL)
		{
			return (0);
			*head = (*head)->next;
		}
		else
		{
			return (1);
			*head = (*head)->next;
		}
	}
	return(1);
}
