#!/usr/bin/env python

a = [5, 3, 6, 4, 1, 2, 0, 8, 9]


class Node(object):
    def __init__(self, value, left, right):
        self.value, self.left, self.right = value, left, right

    def __repr__(self):
        return str(self.value)


class BTree(object):
    def __init__(self, value):
        self.root_node = Node(value, None, None)

    def add_node(self, value):
        cur_node = self.root_node
        new_node = Node(value, None, None)
        while True:
            if cur_node.value > new_node.value:  # Insert left side
                if cur_node.left:
                    cur_node = cur_node.left
                    continue
                else:
                    cur_node.left = new_node
                    return
            elif cur_node.value < new_node.value:  # Insert right side
                if cur_node.right:
                    cur_node = cur_node.right
                    continue
                else:
                    cur_node.right = new_node
                    return
            break  # Same us current node do nothing

    def find_depth(self, cur_node=None, depth=0):
        if cur_node is None:
            cur_node = self.root_node
        depth1 = depth2 = depth
        if cur_node.left:
            depth1 = self.find_depth(cur_node.left, depth + 1)
        if cur_node.right:
            depth2 = self.find_depth(cur_node.right, depth + 1)
        depth = depth1
        if depth1 < depth2:
            depth = depth2
        return depth

    def print_nodes(self, cur_node=None, print_array=None, cur_depth=0):
        is_root_node = False
        if cur_depth == 0:
            is_root_node = True
            cur_node = cur_node if cur_node else self.root_node
            total_depth = self.find_depth(cur_node)
            print_array = [[] for i in range(total_depth + 2)]
        print_array[cur_depth].append(str(cur_node.value))
        if cur_node.left:
            self.print_nodes(cur_node.left, print_array, cur_depth + 1)
        else:
            print_array[cur_depth + 1].append(' ')
        if cur_node.right:
            self.print_nodes(cur_node.right, print_array, cur_depth + 1)
        else:
            print_array[cur_depth + 1].append(' ')
        if is_root_node:
            for i in range(len(print_array)):
                print '{}{}'.format(''.join(' ' * (total_depth - i + 1)),
                                    ' '.join(print_array[i]))

    def find_node(self, value, cur_node=None):
        if cur_node is None:
            cur_node = self.root_node
        if cur_node.value == value:
            return cur_node
        elif cur_node.value > value:
            return self.find_node(value, cur_node.left)
        else:
            return self.find_node(value, cur_node.right)

    def del_node(self, del_value, cur_node=None):
        # Find node and parent node
        if cur_node is None:
            cur_node = self.root_node
            parent_node = None
        while True:
            if cur_node.value == del_value:
                break
            elif cur_node.value > del_value and cur_node.left is not None:
                parent_node = cur_node
                cur_node = cur_node.left
                continue
            elif cur_node.value < del_value and cur_node.right is not None:
                parent_node = cur_node
                cur_node = cur_node.right
                continue
            return  # Did not find node
        if cur_node.left is None or cur_node.right is None:
            replacement_node = cur_node.left if cur_node.left else \
                cur_node.right
        else:
            replacement_node = cur_node.left
            replacement_node_parent = cur_node
            while replacement_node.right:
                replacement_node_parent = replacement_node
                replacement_node = replacement_node.right
            replacement_node_parent.right = None
            replacement_node.left = cur_node.left
            replacement_node.right = cur_node.right
        if parent_node:
            if parent_node.left == cur_node:
                parent_node.left = replacement_node
            else:
                parent_node.right = replacement_node
            return
        else:
            self.root_node = replacement_node


if __name__ == '__main__':
    btree = BTree(a[0])
    for i in a[1:]:
        btree.add_node(i)
    print a
    btree.print_nodes()
    found_node = btree.find_node(3)
    btree.print_nodes(cur_node=found_node)
    btree.del_node(5)
    btree.print_nodes()
