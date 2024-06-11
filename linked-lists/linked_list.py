# A basic implementation of a Linked list

# Class Node for creating nodes


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


# Example Usage:
node1 = Node("once")
node2 = Node("upon")
node3 = Node("a")
node4 = Node("time")

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

# First node(head of the linked list) - contains data and link to the second node
# print(node1.data)
# print(node1.next_node)

# Second node - contains data and link to the third node
# print(node2.data)
# print(node2.next_node)

# Third node - contains data and link to the fourth node
# print(node3.data)
# print(node3.next_node)

# Fourth node(tail of the linked list) - contains data and None
# print(node4.data)
# print(node4.next_node)


# Class LinkedList for creating an actual Linked List by telling the program the first node
class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    # Method to read a node in the linked list using its index
    def read(self, index):
        # We begin at the first node of the list:
        current_node = self.first_node
        current_index = 0

        # We keep following the links of each node until we get to the index we're looking for:
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1

            # If we're past the end of the list, that means the
            # value cannot be found in the list, so rise IndexError:
            if current_node is None:
                raise IndexError("Index out of range")

        return current_node.data

    # Method to search for a node in the linked list using its value returning its index
    def search(self, value):
        # We begin at the first node of the list:
        current_node = self.first_node
        current_index = 0

        while current_node:
            # If we find the data we're looking for, we return it:
            if current_node.data == value:
                return current_index

            # Otherwise, we move on the next node:
            current_node = current_node.next_node
            current_index += 1

        # If we get through the entire list without finding the data, we return None:
        return None

    # Method to insert a new node in the linked list returning the new node
    def insert(self, index, value):
        # We create the new node with the provided value:
        new_node = Node(value)

        # If we are inserting at the beginning of the list:
        if index == 0:
            # Have our new node link to what was the first node:
            new_node.next_node = self.first_node
            # Establish that our new node is now the list's first node:
            self.first_node = new_node
            return new_node

        # If we are inserting anywhere other than the beginning:
        current_node = self.first_node
        current_index = 0

        # First, we access the node immediately before where the new node will go and call it current_node:
        while current_index < (index-1):
            current_node = current_node.next_node
            current_index += 1

        # Have the new node link to the next node:
        new_node.next_node = current_node.next_node
        # Modify the link of the previous node to point to our new node:
        current_node.next_node = new_node
        return new_node

    # Method to delete a node from the linked list using its index
    def delete(self, index):
        # If we are deleting the first node:
        if index == 0:
            # Simply set the first node to be what is currently the second node:
            self.first_node = self.first_node.next_node
            return

         # If we are deleting anywhere other than the beginning:
        current_node = self.first_node
        current_index = 0

        # First, we find the node immediately before the one we want to delete and call it current_node:
        while current_index < (index-1):
            current_node = current_node.next_node
            current_index += 1

        # We find the node that comes after the one we're deleting:
        node_after_deleted_node = current_node.next_node.next_node

        # We change the link of the current_node to point to the node_after_deleted_node,
        # leaving the node we want to delete out of the list:
        current_node.next_node = node_after_deleted_node

    # Add a method to the classic LinkedList class that prints all the elements of the list.
    def print_elements(self):
        current_element = self.first_node

        while current_element:
            print(current_element.data)
            current_element = current_element.next_node

    # Add a method to the classic LinkedList class that returns the last element from the list.
    # Assume you don't know how many elements are in the list.
    def print_last_element(self):
        current_element = self.first_node

        while current_element.next_node:
            current_element = current_element.next_node

        return current_element.data

    # Add a method to the classic LinkedList class that reverses the list.
    # If the original list is A -> B -> C, all of the list’s links should change so that C -> B -> A.
    def reverse_list(self):
        current_node = self.first_node
        prev_node = None

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = prev_node

            prev_node = current_node
            current_node = next_node
        self.first_node = prev_node

        # Example Usage:
list = LinkedList(node1)
# print(list.first_node)

# print(list.read(3))

# print(list.search("aa"))

# node31 = list.insert(3, "happy")
# print(node3.next_node)
# print(node31)
# print(node31.data)
# print(node31.next_node)
# print(node4)
# print(list.read(3))

# node0 = list.insert(0, "STORY!")
# print(node0.next_node)
# print(node1)

# print(list.read(0))
# list.delete(0)
# print(list.read(0))

# print(list.read(2))
# list.delete(2)
# print(list.read(2))

list.print_elements()
# print(list.print_last_element())
list.reverse_list()
list.print_elements()
