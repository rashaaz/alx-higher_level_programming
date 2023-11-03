#include "lists.h"

/**
 * is_palindrome - checks if is a palindrome
 * @head: pointer
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (au_pal(head, *head));
}

/**
 * au_pal - Check if  a palindrome
 * @bign: A pointer
 * @last: A pointer
 *
 * Return: 1 or 0
 */

int au_pal(listint_t **bign, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (au_pal(bign, last->next) && (*bign)->n == last->n)
	{
		*bign = (*bign)->next;
		return (1);
	}
	return (0);
}
