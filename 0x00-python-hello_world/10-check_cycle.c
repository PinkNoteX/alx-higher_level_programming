#include "lists.h"

/**
 * check_cycle - check if linked list has a cycle or not
 * @list: the linked list to check
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (list == NULL || list->next == NULL)
		return (0);
	s = list;
	f = list;

	while (f->next && f && s)
	{
		s = s->next;
		f = f->next->next;
		if (s == n)
			return (1);
	}
	return (0);
}
