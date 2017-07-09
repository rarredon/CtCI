# Chapter 2 of CtCI

class Node():
    """Node in a linked list; use append_to_tail to build up list"""
    def __init__(self, value):
        """Initialize node with a value"""
        self.value = value
        self.next = None

    def __str__(self):
        """Nicely prints the linked list"""
        strvalues = [str(self.value)]
        nextnode = self.next
        while nextnode:
            strvalues.append(str(nextnode.value))
            nextnode = nextnode.next
        return ' -> '.join(strvalues)

    def __repr__(self):
        """Representation of the object"""
        return '<Node object: (%s, %r)>' % (self.value, self.next)

    def append_to_tail(self, value):
        """Add new node to the tail of linked list headed by self"""
        to_append = Node(value)
        current_node = self
        while current_node.next:
            current_node = current_node.next
        current_node.next = to_append

def delete_node(linkedlist, node):
    """Deletes node -- a Node object -- from linked list"""
    n = head = linkedlist
    while n is not node:
        prev = n
        n = n.next
    if n is head: # node is head, delete head
        return head.next
    elif n is None:
        return head
    else:
        prev.next = n.next
        return head

def delete_node_by_val(linkedlist, value):
    """Deletes node from linked list whose value matches value parameter"""
    n = head = linkedlist
    while n and n.value != value:
        prev = n
        n = n.next
    if n is head: # node is head, delete head
        return head.next
    elif n is None:
        return head
    else:
        prev.next = n.next
        return head

def problem1_space(ll):
    """Remove duplicates from linked list - space is not a constraint"""
    seenvals = set()
    n = ll
    while n:
        if n.value in seenvals:
            prev.next = n.next
            n = prev
        else:
            seenvals.add(n.value)
        prev = n
        n = n.next

    return ll

def problem1_no_space(ll):
    """Remove duplicates from linked list - space is a constraint"""
    n = ll
    while n:
        m = n.next
        prev = n
        while m:
            if n.value == m.value:  # Delete m
                prev.next = m.next
                m = prev
            prev = m
            m = m.next
        n = n.next
    return ll

## Tests ## ------------------------------------------------------------------
import random

def gen_test_ll(n=50):
    """Generates random linked list of length n"""
    ll = Node(random.randint(1,round(0.8*n)))
    for _ in range(n-1):
        ll.append_to_tail(random.randint(1, round(0.8*n)))
    return ll

def problem1_space_test():
    """Tests problem 1 - no space constraints"""
    ll = gen_test_ll(10)
    print('Before: ' + str(ll))
    ll = problem1_space(ll)
    print('After: ' + str(ll))

def problem1_no_space_test():
    """Tests problem 1 - space constraints"""
    ll = gen_test_ll(10)
    print('Before: ' + str(ll))
    ll = problem1_no_space(ll)
    print('After: ' + str(ll))
