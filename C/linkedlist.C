// Define the node structure
struct node
{
    int data;          // The data stored in the node
    struct node *next; // The pointer to the next node
};

// Create a new node with a given data value and return its pointer
struct node *create_node(int data)
{
    struct node *new_node = malloc(sizeof(struct node)); // Allocate memory for the node
    new_node->data = data;                               // Assign the data value
    new_node->next = NULL;                               // Initialize the next pointer to NULL
    return new_node;                                     // Return the node pointer
}

// Add a new node at the end of the list and return the head pointer
struct node *add_node(struct node *head, int data)
{
    struct node *new_node = create_node(data); // Create a new node
    if (head == NULL)
    {                    // If the list is empty
        head = new_node; // Make the new node the head
    }
    else
    {                                // If the list is not empty
        struct node *current = head; // Start from the head
        while (current->next != NULL)
        {                            // Traverse the list until the last node
            current = current->next; // Move to the next node
        }
        current->next = new_node; // Link the last node to the new node
    }
    return head; // Return the head pointer
}

// Delete a node with a given data value from the list and return the head pointer
struct node *delete_node(struct node *head, int data)
{
    if (head == NULL)
    {                // If the list is empty
        return NULL; // Return NULL
    }
    else if (head->data == data)
    {                             // If the head node matches the data value
        struct node *temp = head; // Store the head node in a temporary variable
        head = head->next;        // Move the head pointer to the next node
        free(temp);               // Free the memory of the deleted node
        return head;              // Return the head pointer
    }
    else
    {                                 // If the head node does not match the data value
        struct node *current = head;  // Start from the head
        struct node *previous = NULL; // Initialize the previous pointer to NULL
        while (current != NULL && current->data != data)
        {                            // Traverse the list until the node matches the data value or the end is reached
            previous = current;      // Store the current node in the previous pointer
            current = current->next; // Move to the next node
        }
        if (current != NULL)
        {                                   // If the node is found
            previous->next = current->next; // Link the previous node to the next node
            free(current);                  // Free the memory of the deleted node
        }
        return head; // Return the head pointer
    }
}

// Find a node with a given data value in the list and return its pointer
struct node *find_node(struct node *head, int data)
{
    struct node *current = head; // Start from the head
    while (current != NULL)
    { // Traverse the list until the end is reached
        if (current->data == data)
        {                   // If the node matches the data value
            return current; // Return the node pointer
        }
        current = current->next; // Move to the next node
    }
    return NULL; // Return NULL if the node is not found
}

// Print the data values of the nodes in the list
void print_list(struct node *head)
{
    struct node *current = head; // Start from the head
    while (current != NULL)
    {                                 // Traverse the list until the end is reached
        printf("%d ", current->data); // Print the data value of the node
        current = current->next;      // Move to the next node
    }
    printf("\n"); // Print a new line
}
