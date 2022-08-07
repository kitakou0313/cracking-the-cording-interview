class LinkedListNode(object):
    """
    連結リストのノード
    """

    def __init__(self, val: int, nxt_node: LinkedListNode, prev_node: LinkedListNode):
        self.prev = prev_node
        self.nxt = nxt_node
        self.val = val
