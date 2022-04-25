#include "lists.h"

/**
 * check_cycle - linked list cycle
 * @list: list
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *shorter = list;
	listint_t *longer = list;

	if (!list)
	{
		return (0);
	}
	while (1)
	{
		if (longer->next != NULL && longer->next->next != NULL)
		{
			longer = longer->next->next;
			shorter = shorter->next;
		if (longer == shorter)
		{
			return (1);
		}
		}
		else
		{
			return (0);
		}
	}
}
