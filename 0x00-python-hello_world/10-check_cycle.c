#include "lists.h"

/**
 * check_cycle - checks if a singly linked list
 * @list: pointer
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *sl = list;
	listint_t *fa = list;

	while (fa && fa->next)
	{
		sl = sl->next;
		fa = fa->next->next;

		if (sl == fa)
		{
			return (1);
		}
	}

	return (0);
}
