#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number
 * @head: A pointer
 * @number: The number to insert.
 *
 * Return: The address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *c = malloc(sizeof(listint_t));

	if (!c)
		return (NULL);

	c->n = number;
	c->next = NULL;

	if (!nd || c->n < nd->n)
	{
		c->next = nd;
		return (*head = c);
	}

	while (nd)
	{
		if (!nd->next || c->n < nd->next->n)
		{
			c->next = nd->next;
			nd->next = c;
			return (nd);
		}
		nd = nd->next;
	}
	return (NULL);
}

