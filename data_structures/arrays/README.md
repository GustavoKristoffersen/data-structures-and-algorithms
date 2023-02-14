# Arrays

Arrays are one of the most basic data structures in computer science. An array is essentially a list of data elements stored in sequential memory slots, i.e., one after another.
The element position in the array is called index. Indexes go from 0 to as many elements as the array has, so the last index will always be the total number of elements minus one.

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20220721080308/array.png)

### :bookmark_tabs: Reading - O(1)

A computer can read a value from an array in a single step. This is because each value is in a separate memory address, and computers can access any data in any memory address directly without performing any search.
When allocating an array, the computer makes note of the memory address at which the array starts, so this way the computer can find values at any index by just performing simple additions to the first index’s memory address.

```
array[9]
```

### :bookmark_tabs: Insertion - O(N)
The time complexity of inserting new elements in an array depends on where they're going to be placed. If the value is being added at the end of the array, then a single step is performed because the computer only needs to place the element in the next memory slot after the last array element. However, if the value is going to be placed anywhere else in the array, it will need to reallocate all the right values to its next memory cell to create space for the new element. So we say that an insertion takes the maximum of N + 1 steps, where N is the number of values that will need to be shifted to make space for the new value and 1 is the insertion itself. In Big O notation, this is represented as just O(N).

Example: if we had an array of five integers ```[2, 2, 3, 0, 0, 1]``` and we wanted to insert the value of 5 at position 3, this is what would happend.

![alt text](https://www.codesdope.com/staticroot/images/ds/intro5.gif)

### :bookmark_tabs: Deletion - O(N)
The time complexity of deletion also depends on the position of the element. If the element to be deleted is at the end of the array, it can be deleted in a single step. However, if the element is anywhere else, we must shift the remaining right elements to the left in order to fill the empty space in memory left by the deletion. For this reason, we say that a deletion can take a maximum of N steps, where N is the number of elements that will need to be shifted. The worst case is when we want to delete the very first element of the array, meaning that all elements of the array will need to be shifted to the left.

Example: if we have the array ```[1, 20, 5, 78, 30]``` and we want to delete the number 20, at position 1.

![alt text](https://www.log2base2.com/images/ds/remove-an-element-from-array.png)


### :bookmark_tabs: Searching O(N)
Actually, searching for an element in an array depends on the type of the array and also the algorithm used to perform the search. If the array is ordered, we can use [Bubble Sort](https://github.com/GustavoKristoffersen/data-structures-and-algorithms/tree/main/algorithms/searching/binary_search) algorithm which has an efficiency of O(log N). If the array is unordered we can use a [Linear Search](https://github.com/GustavoKristoffersen/data-structures-and-algorithms/tree/main/algorithms/searching/linear_search) which has an efficiency of O(N). Since the arrays here are all unordered, the search efficiency will be O(N).


## Static Arrays vs Dynamic Arrays
There are two main types of arrays: static arrays and dynamic arrays. In a static array, you always have to declare the size of it in advance. This might be a problem if you don’t know how many items you will be storing in that array. However, static arrays are usually faster once the memory space is already predefined and will not change over time, not performing any additional allocations. It is also more efficient when it comes to memory usage, since it only allocates as much space as the array needs.

With dynamic arrays, however, you have the advantage of not having to worry about manually defining size of it. Although you can also end up having O(n) efficiency for operations like insertion at the end (which is O(1) by default). This happens because the array can not keep growing linearly forever. When you create a dynamic array, the size of it is determined by default by the number of elements that are there at the time. When trying to add a new element, if the allocated memory for the arary is already full, the computer has to take all elements and move them to another space in memory. Once this happens, the allocated memory for the array will now be the double of what it was previously. For this reason, sometimes an insertion can take many more steps than usual because of the moving step. [Read more about this here](https://en.wikipedia.org/wiki/Amortized_analysis#Dynamic_Array)

