//Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *dummy=new ListNode(0);
        ListNode *temp=dummy;
        ListNode *t1=l1;
        ListNode *t2=l2;
        while (t1!=NULL || t2!=NULL){
            if(t1 && t2)
            {
                if (t1->val<t2->val)
                {
                    dummy->next=new ListNode(t1->val);
                    t1=t1->next;
                }
                else
                {
                    dummy->next=new ListNode(t2->val);
                    t2=t2->next;
                }
            }
            else if (t1!=NULL && t2==NULL)
            {
                dummy->next=t1;
                return temp->next;
            }
            else if (t2!=NULL && t1==NULL){
                dummy->next=t2;
                return temp->next;
            }
            dummy=dummy->next;
        }
        return temp->next;
    } 
};
