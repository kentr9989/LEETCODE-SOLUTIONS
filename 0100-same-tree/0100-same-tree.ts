/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    // BASE CASE: if both tree are empty return true
    if (!p && !q) {
        return true;
    }
    // if one of the tree is empty return false
    if (!p || !q) {
        return false;
    }
    // if val at first tree not equal val of second tree return false
    if (p.val !== q.val) {
        return false;
    }
    // recurse the (left of first tree,left of second tree) AND
    //             (right of first tree, right of second tree) 
    return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
};