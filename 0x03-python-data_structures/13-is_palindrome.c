#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - check if the given list is a palindrome or not
 * @head: head of the linked list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *t;
	int array[7777], x = 0, length = 0;

	if (*head == NULL)
	{
		return (1);
	}
	t = *head;
	while (t != NULL)
	{
		length++;
		t = t->next;
	}
	if (length == 1)
	{
		return (1);
	}
	t = *head;
	while (t != NULL)
	{
		array[x] = t->n;
		t = t->next;
		x++;
	}
	x = 0;
	while (x <= length / 2)
	{
		if (array[x] != array[length - x - 1])
			return (0);
		x++;
	}
	return (1);
}
