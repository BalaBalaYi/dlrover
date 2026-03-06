
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_all(self):
        result = [self.val]
        iterator = self.next
        while iterator:
            result.append(iterator.val)
            iterator = iterator.next

        print(result)
