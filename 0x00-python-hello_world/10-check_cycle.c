#include "lists.h"

/**
 * check_cycle - checks if a singly linked list
 * @mynot: pointer
 * Return: 1 or 0
 */
int check_cycle(listint_t *mynot)
{
	listint_t *sl = mynot;
	listint_t *fa = mynot;

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
