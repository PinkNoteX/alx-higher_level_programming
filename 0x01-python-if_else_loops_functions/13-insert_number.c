#include "lists.h"
/**
 * insert_node - add a num to a sorted list
 * @head: head of the list
 * @number: int to insert to the list
 * Return: a new node or NULL
 */
istint_t *insert_node(listint_t **head, int number)
{
	listint_t *a = *head;
	listint_t *ne = malloc(sizeof(listint_t));

	if (!ne)
		return (NULL);

	ne->n = number;
	ne->next = NULL;

	if (!a || ne->n < a->n)
	{
		ne->next = a;
		return (*head = ne);
	}

	while (a)
	{
		if (!a->next || ne->n < a->next->n)
		{
			ne->next = a->next;
			a->next = ne;
			return (a);
		}
		a = a->next;
	}
	return (NULL);
}
