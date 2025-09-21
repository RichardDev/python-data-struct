def create_node(data, next=None):
    return {'data': data, 'next': next}

def insert_beginning(list, data):
    new_node = create_node(data, list)
    return new_node

def insert_end(list, data):
    if list is None:
        return create_node(data)
    current = list
    while current['next'] is not None:
        current = current['next']
    current['next'] = create_node(data)
    return list

def delete_node(list, key):
    if list is None:
        return None
    if list['data'] == key:
        return list['next']
    current = list
    while current['next'] is not None and current['next']['data'] != key:
        current = current['next']
    if current['next'] is not None:
        current['next'] = current['next']['next']
    return list

def show_list(list):
    elements = []
    current = list
    while current is not None:
        elements.append(current['data'])
        current = current['next']
    return elements

def search(list, key):
    current = list
    while(current is not None):
        if current(['data']) == key:
            return True
        


# Example usage


linked_list = None

linked_list = insert_end(linked_list, 1)
linked_list = insert_end(linked_list, 2)
linked_list = insert_beginning(linked_list, 0)
print("Linked List after insertions:", show_list(linked_list))
linked_list = delete_node(linked_list, 2)
print("Linked List after deleting 2:", show_list(linked_list))
