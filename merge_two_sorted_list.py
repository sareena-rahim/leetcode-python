class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def mergeTwoLists(self,l1,l2):
        dummy=Node()
        tail=dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        tail.next =l1 if l1 else l2
        return dummy.next


def list_to_linked(data_list):
    if not data_list:
        return None

    head=Node(data_list[0])
    current=head
    for val in data_list[1:]:
        current.next=Node(val)
        current=current.next
    return head
def print_list(head):
    while head:
        print(head.val,end=' ')
        head=head.next
    print()

list_1_values=[1,2,3,4]
list_2_values=[2,4,6,8]
l1=list_to_linked(list_1_values)
l2=list_to_linked(list_2_values)
sol=Solution()
merge=sol.mergeTwoLists(l1,l2)
print('Merged List')
print_list(merge)

