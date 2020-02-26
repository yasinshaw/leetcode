from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ListNode):
            return False
        return self.val == o.val and self.next == o.next


def build_list(list: List[int]):
    head = ListNode(0)
    temp = head
    for x in list:
        temp.next = ListNode(x)
        temp = temp.next
    return head.next
