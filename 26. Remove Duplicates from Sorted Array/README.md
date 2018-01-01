## Remove Duplicates from Sorted Array

求有序的序列的不同值个数，要求使用O(1)空间

#### Approach 

思路有点类似于给成绩排名，相同分数排名一致。  

* 设置两个下标`sum`和`value`,`sum`代表不同值总个数，`value`表示标记的当前值。  
* 对整理序列S进行搜索，当前值与`value`不同时`sum`+1 `value = 当前值`
