
Here is the expected output from running this program. Depending on the order
of redistributing or coalescing, your output may vary. However, the end result
in every case should be the insertion or deletion of the item from the BTree.

My/Our name(s) is/are
BTree(2,
 {1: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],1)
},1,2)
***Inserting 10
BTree(2,
 {1: BTreeNode(2,1,[10, None, None, None],[None, None, None, None, None],1)
},1,2)
***Inserting 8
BTree(2,
 {1: BTreeNode(2,2,[8, 10, None, None],[None, None, None, None, None],1)
},1,2)
***Inserting 22
BTree(2,
 {1: BTreeNode(2,3,[8, 10, 22, None],[None, None, None, None, None],1)
},1,2)
***Inserting 14
BTree(2,
 {1: BTreeNode(2,4,[8, 10, 14, 22],[None, None, None, None, None],1)
},1,2)
***Inserting 12
BTree(2,
 {1: BTreeNode(2,2,[8, 10, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,2,[14, 22, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,1,[12, None, None, None],[1, 2, None, None, None],3)
},3,4)
***Inserting 18
BTree(2,
 {1: BTreeNode(2,2,[8, 10, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,3,[14, 18, 22, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,1,[12, None, None, None],[1, 2, None, None, None],3)
},3,4)
***Inserting 2
BTree(2,
 {1: BTreeNode(2,3,[2, 8, 10, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,3,[14, 18, 22, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,1,[12, None, None, None],[1, 2, None, None, None],3)
},3,4)
***Inserting 50
BTree(2,
 {1: BTreeNode(2,3,[2, 8, 10, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,4,[14, 18, 22, 50],[None, None, None, None, None],2)
, 3: BTreeNode(2,1,[12, None, None, None],[1, 2, None, None, None],3)
},3,4)
***Inserting 15
BTree(2,
 {1: BTreeNode(2,3,[2, 8, 10, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,2,[14, 15, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,2,[12, 18, None, None],[1, 2, 4, None, None],3)
, 4: BTreeNode(2,2,[22, 50, None, None],[None, None, None, None, None],4)
},3,5)
***Deleting 14
BTree(2,
 {1: BTreeNode(2,3,[2, 8, 10, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,4,[15, 18, 22, 50],[None, None, None, None, None],2)
, 3: BTreeNode(2,1,[12, None, None, None],[1, 2, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},3,5)
***Deleting 50
BTree(2,
 {1: BTreeNode(2,3,[2, 8, 10, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,3,[15, 18, 22, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,1,[12, None, None, None],[1, 2, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},3,5)
***Deleting 8
BTree(2,
 {1: BTreeNode(2,2,[2, 10, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,3,[15, 18, 22, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,1,[12, None, None, None],[1, 2, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},3,5)
***Deleting 12
BTree(2,
 {1: BTreeNode(2,2,[2, 10, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,2,[18, 22, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,1,[15, None, None, None],[1, 2, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},3,5)
***Deleting 18
BTree(2,
 {1: BTreeNode(2,4,[2, 10, 15, 22],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Deleting 2
BTree(2,
 {1: BTreeNode(2,3,[10, 15, 22, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Deleting 10
BTree(2,
 {1: BTreeNode(2,2,[15, 22, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Deleting 22
BTree(2,
 {1: BTreeNode(2,1,[15, None, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Deleting 15
BTree(2,
 {1: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Deleting 54
BTree(2,
 {1: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Deleting 76
BTree(2,
 {1: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Inserting 14
BTree(2,
 {1: BTreeNode(2,1,[14, None, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Deleting 2
BTree(2,
 {1: BTreeNode(2,1,[14, None, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
***Deleting 84
BTree(2,
 {1: BTreeNode(2,1,[14, None, None, None],[None, None, None, None, None],1)
, 2: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],2)
, 3: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],3)
, 4: BTreeNode(2,0,[None, None, None, None],[None, None, None, None, None],4)
},1,5)
