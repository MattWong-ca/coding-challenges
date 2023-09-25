// 206. Reverse Linked List - Leetcode Easy

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    let current = head;
    let nextNode: ListNode | null;

    while ( current != null ) {
        nextNode = current.next;
        current.next = prev;
        prev = current;
        current = nextNode;
    }

    return prev;
};
