from multiprocessing import current_process


class LinkedListNode(object):
    """
    連結リストのノード
    """

    def __init__(self, val: int, nxt_node: "LinkedListNode" = None, prev_node: "LinkedListNode" = None):
        self.prev = prev_node
        self.nxt = nxt_node
        self.val = val


class SingleLinkedList(object):
    """
    単方向連結リスト
    """

    def __init__(self, vals: list):
        """
        コンストラクタ
        """
        self.head: LinkedListNode = None
        self.tail: LinkedListNode = None

        for val in vals:
            self.add(val)

    def add(self, val: int):
        """
        リスト末尾にNode追加
        """
        node_to_add = LinkedListNode(val)
        if self.head is None:
            self.head = self.tail = node_to_add
            return

        self.tail.nxt = node_to_add
        self.tail = node_to_add

    def __iter__(self) -> LinkedListNode:
        """
        イテレータ
        """
        current_node = self.head

        while not(current_node is None):
            yield current_node
            current_node = current_node.nxt

    def get_vals(self) -> list:
        """
        全Valを返却
        """
        val_list = []

        current_node = self.head
        while not(current_node is None):
            val_list.append(current_node.val)
            current_node = current_node.nxt

        return val_list

    def add_multi_node(self, vals: list):
        """
        複数Nodeを同時に追加
        """
        for val in vals:
            self.add(val)


class LinkedList(object):
    """
    双方向連結リスト
    """

    def add(self, val):
        """
        要素の追加
        """
        new_node = LinkedListNode(val)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.nxt = new_node
        new_node.prev = self.tail

        self.tail = new_node

    def __init__(self, vals: list):
        """
        コンストラクタ
        """
        self.head: LinkedListNode = None
        self.tail: LinkedListNode = None

        for val in vals:
            self.add(val)

    def get_vals(self) -> list:
        """
        全nodeのvalを取得
        """
        vals = []

        node = self.head
        while not(node is None):
            vals.append(node.val)

        return vals
