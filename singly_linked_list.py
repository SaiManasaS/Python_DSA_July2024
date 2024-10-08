class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 1
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return 

            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):

        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            
            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")

            prev = cur 
            cur = nxt 
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)


    # This is my definition! Bravo Girl! Your definition ran the first time..! 
    '''def merge_sorted(self, llist):
        prev1 = None
        prev2 = None
        cur1 = self.head
        cur2 = llist.head
        smaller_elem = None

        # Have included these 3 if blocks after looking at the provided solution
        if not cur1 and not cur2:
            return
        if not cur1:
            return cur2
        if not cur2:
            return cur1

        while cur1 and cur2:
            if cur1.data < cur2.data:
                smaller_elem = cur1
                prev1 = cur1
                cur1 = cur1.next
            else:
                newNode = Node(cur2.data)
                smaller_elem = cur2
                prev2 = cur2
                cur2 = cur2.next             
                newNode.next = cur1
                prev1.next = newNode
                prev1 = prev1.next
        cur1.next = None
        return self.head
    '''


    '''def merge_sorted(self, llist):
    
        p = self.head 
        q = llist.head
        s = None
    
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p
            
        self.head = new_head     
        return self.head
    '''

    def merge_sorted1(self, llist):
        p1 = None
        p2 = None
        q = self.head
        p = llist.head
        s = None

        if p.data <= q.data:
            s = p
            '''s.next = q'''
            '''p = p.next'''
        else:
            s = q
            '''s.next = p'''
            '''q = q.next'''
        new_head = s
        

        print("self.head", self.head)
        print("q", q)
        print("llist.head", llist.head)
        print("p", p)

        while q is not None and p is not None:
            print('In while(), p:', p.data)
            print('In while(), q:', q.data)
            if p.data <= q.data:
                s = p
                temp = p.next
                s.next = q
                p = temp
                '''print('p:', p.data)'''
            else:
                s = q
                temp = q.next
                s.next = p
                '''temp = q'''
                q = temp
                '''print('q:', q.data)'''
                '''q.print_list()'''
            
            
        '''if s == temp and q is None and p is not None:'''
        if q is None and p is not None:
            s.next = p

        if p is None and q is not None:
            s.next = q

        '''p.print_list()
        q.print_list()'''

        self.head = new_head     
        return self.head

    def merge_sorted_didnotwork_July2024(self, llist):
        p1 = None
        p2 = None
        q = self.head
        p = llist.head
        s = None

        if p.data <= q.data:
            s = p
            '''s.next = q'''
            '''p = p.next'''
        else:
            s = q
            '''s.next = p'''
            '''q = q.next'''
        new_head = s
        

        print("self.head", self.head)
        print("q", q)
        print("llist.head", llist.head)
        print("p", p)

        '''while q is not None and p is not None:
            print('In while(), p:', p.data)
            print('In while(), q:', q.data)
            if p.data <= q.data:
                s = p
                temp = p.next
                s.next = q
                p = temp
                #print('p:', p.data)
            else:
                s = q
                temp = q.next
                s.next = p
                temp = q
                q = temp
                print('q:', q.data)
                q.print_list()
        '''
            
            
        '''if s == temp and q is None and p is not None:'''
        if q is None and p is not None:
            s.next = p

        if p is None and q is not None:
            s.next = q

        '''p.print_list()
        q.print_list()'''

        self.head = new_head     
        return self.head

    def merge_sorted(self, llist):
        p1 = None
        p2 = None
        c1 = self.head
        c2 = llist.head
        s = None
        new_head = self.head

        while c1 is not None and c2 is not None:
            print('In while(), c1:', c1.data)
            print('In while(), c2:', c2.data)
            if c1.data <= c2.data:
                p1 = c1
                next_c1 = c1.next
                if p2 is not None:
                    p2.next = c1
                c1.next = c2
                c1 = next_c1
            else:
                p2 = c2
                c2 = c2.next
            
        if c1 is None and c2 is not None:
            p1.next = c2
        elif c1 is not None and c2 is None:
            p2.next = c1

        self.head = new_head

#Finally this is working on Aug 8th
    def remove_duplicates(self):
        
        num_rep_dict = {}
        cur = self.head
        prev = None

        while cur is not None:
            if cur.data in num_rep_dict:
                if num_rep_dict[cur.data] > 1:
                    temp_next = cur.next
                    if prev is not None:
                        prev.next = cur.next
                        cur = temp_next
                num_rep_dict[cur.data] = num_rep_dict[cur.data] + 1
            else:
                num_rep_dict[cur.data] = 1
            cur = cur.next

        print("num_rep_dict: ", num_rep_dict)

        cur = self.head
        print("cur.data self.head: ", cur.data)

        while cur is not None:
            print("cur.data: ", cur.data)
            if num_rep_dict[cur.data] > 1:
                if cur == self.head:
                    print("if Line 326, num_rep_dict[cur.data]:", num_rep_dict[cur.data])
                    num_rep_dict[cur.data] = num_rep_dict[cur.data] - 1
                    self.head = cur.next
                    prev = self.head
                    cur = cur.next
                else:
                    print("else Line 332")
                    num_rep_dict[cur.data] = num_rep_dict[cur.data] - 1
                    prev.next = cur.next
                    cur = cur.next
                    '''prev = cur'''
                print("num_rep_dict[cur.data]:", num_rep_dict[cur.data])
            else:
                print("else Line 339")
                prev = cur
                cur = cur.next
        
        print("2nd num_rep_dict: ", num_rep_dict)
       
        '''num_rep_hastab = [[]]
        
        cur = self.head

        while cur is not None:
            num_rep_hastab[cur.data] = 0

        while cur is not None:
            if num_rep_hastab[cur.data]:
                num_rep_hastab[cur.data] = num_rep_hastab[cur.data] + 1
            else:
                num_rep_hastab[cur.data] = 0
        
        cur = self.head
        prev = None
        while cur is not None:
            prev = cur
            self.head = prev
            if num_rep_dict[cur.data] > 1:
                prev = cur
                num_rep_dict[cur.data] = num_rep_dict[cur.data] - 1
                next_cur = cur.next
                cur.next = None
                prev.next = None
                cur = next_cur
                self.head = cur
                prev = cur
            else:
                self.head = cur
                self.head = prev
                cur = cur.next
        '''
            

        print("2nd num_rep_dict: ", num_rep_dict)

        return self.head

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()