# Trees
# -----------------------------------------------------------------------------
# Implements concepts from Chapter 4 in Cracking the Coding Interview by Gayle
# McDowell 
# -----------------------------------------------------------------------------


class TreeNode:
    """Implements a node in a tree"""
    def __init__(self, data, children=None):
        """Node has data and a list of children"""
        self.data = data
        self.children = children if children else []


    def __repr__(self):
        return '<TreeNode object: val=%s>' % self.data


    def add_child(self, child):
        if not isinstance(child, TreeNode):
            raise TypeError(
                'Expected TreeNode object for child, got %s' % type(child)
            )
        self.children.append(child)


    def add_children(self, children):
        notlist = not (type(children) is list)
        if notlist or not all(isinstance(c, TreeNode) for c in children):
            raise TypeError('Expected list of TreeNode objects for children')
        self.children.extend(children)


    def remove_child_by_val(self, val):
        for child in self.children:
            if child.data == val:
                self.children.remove(child)
                break


class BinaryTreeNode(TreeNode):
    def __init__(self, data, children=None):
        self.data = data
        if children and len(children) > 2:
            raise ValueError('BinaryTreeNode can not have more than 2 children')
        if children and len(children) == 1:
            children.append(None)
        self.children = children if children else [None, None]


    def __repr__(self):
        return '<BinaryTreeNode object: val=%s>' % self.data


    def add_child(self, child):
        if not isinstance(child, BinaryTreeNode):
            raise TypeError(
                'Expected BinaryTreeNode object for child, got %s' % type(child)
            )
        if not any(c is None for c in self.children):
            raise ValueError('BinaryTreeNode can not have more than 2 children')
        elif self.children[0] is None:
            self.children[0] = child
        else:
            self.children[1] = child


    def add_children(self, children):
        notlist = not (type(children) is list)
        if notlist or not all(isinstance(c, BinaryTreeNode) for c in children):
            raise TypeError('Expected list of TreeNode objects for children')

        if len(children) == 1:
            self.add_child(children[0])

        elif len(children) == 2 and all(c is None for c in self.children) :
            self.children = children
            
        else:
            raise ValueError('BinaryTreeNode can not have more than 2 children')
        

class Tree:
    def __init__(self, root):
        if isinstance(root, (TreeNode, BinaryTreeNode)):
            self.root = root
        else:
            self.root = TreeNode(root)
        self.data = self.root.data


    def __repr__(self):
        return '<Tree object: root=%r>' % self.root


    def traverse(self, method='in-order', level=False):
        """Methods of traversal are 'in-order', 'pre-order', or 'post-order'"""
        if method=='in-order':
            if level:
                return Tree.in_order_traversal(self.root, level=0)
            else:
                return Tree.in_order_traversal(self.root)                
        elif method=='pre-order':
            if level:
                return Tree.pre_order_traversal(self.root, level=0)
            else:
                return Tree.pre_order_traversal(self.root)                
        elif method=='post-oder':
            if level:
                return Tree.post_order_traversal(self.root, level=0)
            else:
                return Tree.post_order_traversal(self.root)                
        else:
            raise ValueError('Method of traversal not recognized.')     


    @staticmethod
    def in_order_traversal(node, level=None):
        if len(node.children) > 2:
            raise ValueError(
                'Tree is not binary.'
                'In-order traversal is only defined for binary trees.'
            )

        # Set up for subtree traversal
        nextlevel = level + 1 if level is not None else None            

        # Traverse left subtree
        if node.children[0] is not None:
            yield from \
                Tree.in_order_traversal(node.children[0], level=nextlevel)

        # Yield current node and level (if level is not None)
        if level is not None:
            yield node, level
        else:
            yield node

        # Traverse right subtree
        if node.children[1] is not None:
            yield from \
                Tree.in_order_traversal(node.children[1], level=nextlevel)


    @staticmethod
    def pre_order_traversal(node, level=None):
        # Yield current node and level (if level is not None)
        if level is not None:
            yield node, level
        else:
            yield node

        # Set up for subtree traversal
        nextlevel = level + 1 if level is not None else None            

        # Traverse the subtrees
        for i in range(len(node.children)):
            if node.children[i] is not None:
                pre_order_traversal(node.children[i], level=nextlevel)
        

    @staticmethod
    def post_order_traversal(node, level=None):
        # Set up for subtree traversal
        nextlevel = level + 1 if level is not None else None            

        # Traverse the subtrees
        for i in range(len(node.children)):
            if node.children[i] is not None:
                post_order_traversal(node.children[i], level=nextlevel)

        # Yield current node and level (if level is not None)
        if level is not None:
            yield node, level
        else:
            yield node


    def convert_binary(self):
        root = BinaryTreeNode(self.root.data)
        queue = [(self.root, root)]
        while len(queue) > 0:
            oldnode, newnode = queue.pop()
            for child in oldnode.children:
                newchild = BinaryTreeNode(child.data)
                newnode.add_child(newchild)
                queue.append((child, newchild))
        return BinaryTree(root)


class BinaryTree(Tree):
    """Implements a binary tree"""
    def __init__(self, root):
        if isinstance(root, BinaryTreeNode):
            self.root = root
        else:
            self.root = BinaryTreeNode(root)
        self.data = self.root.data
        self.__depth = None  # Will get updated
        

    def __str__(self):
        """Pretty print a binary tree"""
        lines = []
        lines.append(str(self.root.data))
        if self.depth:
            lines.append('/ \\')
            lines.append(' %s   %s ' %
                tuple(
                    map(lambda c: str(c.data) if c else 'N', self.root.children)
                )
            )
        if self.depth > 1:
            lines.append('/|   |\\')
            lines.append(
                (' %s %s' % tuple(
                    (str(c.data) if c is not None else 'N'
                     for c in self.root.children[0].children)
                ))
                + '   '
                + ('%s %s ' % tuple(
                    (str(c.data) if c is not None else 'N'
                     for c in self.root.children[1].children)
                ))
            )
        if self.depth > 2:
            lines.append('...')
            lines.append('depth=%d: %s' %
                (self.depth,
                   ' '.join(
                       str(n.data) if n else 'N'
                       for n, level in self.traverse(level=True)
                       if level == self.depth
                   )
                )
            )
        maxlength = max(map(len, lines))
        if any('N' in line for line in lines):
            lines.append('\n... where N is None.')
        lines = ['{0:^{width}}'.format(s, width=maxlength)
                 if '...' not in s and 'depth=' not in s else s for s in lines]
        return '\n'.join(lines)
        


    def insert_node(self, insert):
        depth = self.depth
        if isinstance(insert, TreeNode):
            insert = BinaryTreeNode(insert.data, insert.children)
        elif not isinstance(insert, BinaryTreeNode):
            insert = BinaryTreeNode(insert)
        traversal = self.traverse(level=True)
        leftmost, _ = next(traversal)
        openspot = None
        for node, level in traversal:
            hasopening = any(c is None for c in node.children)
            # Priority given to leftmost open node above the bottom level
            if level < depth and hasopening: 
                node.add_child(insert)
                break
        else:
            # No open spots; start a new level at leftmost node
            leftmost.add_child(insert)
            self.__increment_depth()


    @property
    def depth(self):
        return self.get_depth()

    def get_depth(self):
        if self.__depth:
            return self.__depth
        depth = 0
        for _, level in self.traverse(method='in-order', level=True):
            depth = max(depth, level)
        self.__depth = depth
        return depth

    def __increment_depth(self):
        if self.__depth is None:
            self.get_depth()
        self.__depth += 1
