#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 *         1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1;
	listint_t *ptr2;

	ptr1 = list;
	ptr2 = list;
	while (list && ptr1 && ptr1->next)
	{
		list = list->next;
		ptr1 = ptr1->next->next;

		if (list == ptr1)
		{
			list = ptr2;
			ptr2 =  ptr1;
			while (1)
			{
				ptr1 = ptr2;
				while (ptr1->next != list && ptr1->next != ptr2)
				{
					ptr1 = ptr1->next;
				}
				if (ptr1->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
