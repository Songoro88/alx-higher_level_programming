#include "lists.h"

/**
 * insert_node - Inserts a num into a sorted singly linked list.
 * @head: list head
 * @number: num to store in the new Node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *runner;
        listint_t *new;

        Runner = *head;

        New = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        New->n = number;

        if (*head == NULL || (*head)->n > number)
        {
                new->next = *head;
                *head = new;
                return (new);
        }

        while (runner->next != NULL)
        {
                if ((runner->next)->n >= number)
                {
                        new->next = runner->next;
                        runner->next = new;
                        return (new);
                }
                Runner = runner->next;
        }

        new->next = NULL;
        runner->next = new;
        return (new);
}
