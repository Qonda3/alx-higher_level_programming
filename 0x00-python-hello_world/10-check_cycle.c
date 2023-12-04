#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow != fast)
	{
		if (fast == NULL)
			return (0);
		if (fast->next == NULL)
			return (0);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (1);
}
