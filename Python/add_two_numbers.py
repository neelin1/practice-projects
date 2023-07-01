# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def linked_list_to_string (l: Optional[ListNode]) -> str:
        if (l.next == None):
            return str(l.val)
        else: 
          return str(l.val) + linked_list_to_string(l.next)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # convert list 1 into a string
        l1_string = linked_list_to_string(l1)
        
        # convert list 2 into a string
        l2_string = linked_list_to_string(l2)

        rev_l1_string = reversed_string = ''.join(reversed(l1_string))
        rev_l2_string = reversed_string = ''.join(reversed(l2_string))

        sum = int(rev_l1_string) + int(rev_l2_string)
        
        str_sum = str(sum)

        temp_node = ListNode(str_sum[0], None)
        for i in range(1, len(str_sum), 1):
            temp_node = ListNode(str_sum[i], temp_node)
      
        return(temp_node)

        # l3 = ListNode(str_sum[-1])


        # sum = int(str_list_1) + int (str_list_2)

        # print (sum)
        # # make new linked list
        # l3 = 
        # for i in range(str(sum)):
            
            
        
