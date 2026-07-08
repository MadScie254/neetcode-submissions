class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val)

        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)

        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        # Remove head
        if index == 0:
            self.head = self.head.next

            if not self.head:
                self.tail = None

            return True

        prev = self.head
        curr = self.head.next
        i = 1

        while curr:
            if i == index:
                prev.next = curr.next

                if curr == self.tail:
                    self.tail = prev

                return True

            prev = curr
            curr = curr.next
            i += 1

        return False

    def getValues(self) -> list[int]:
        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values

    def reverse(self) -> None:
        prev = None
        curr = self.head

        self.tail = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev