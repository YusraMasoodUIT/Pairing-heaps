# Pairing-heaps
Pairing heaps is a modified form of Fibonacci heaps. It consist of the properties of heap data structure along with self adjusting structure. Mostly they are used in shortest path algorithms

## Operations Of Pairing Heap:  

### Merge
Compare the root node of the two heaps to be merged, if the root node of the first heap is smaller than the root node of the second heap then root node of the second heap becomes a left child of the root node of the first heap otherwise vice-versa

### Insert
Insert a new item in heap by creating a new node and Merging it with existing heap

### Find Minimum
Find min just returns the top element(root node) of the heap.

### Delete
Delete operation is always performed on root node. To delete a node n, detach the sub tree that is rooted at node n. Then, delete n from the tree and merge its sub trees into one sub tree using a two-pass method. Merge the detached sub tree with the sub tree resulting from the two-pass


# Implementation

The complete code of pairing heaps is in the pairing_heaps.py file. To execute the code call the gui() function in that file.

The gui implementation of this code is in the gui.py file. Simply run this file to execute it.
