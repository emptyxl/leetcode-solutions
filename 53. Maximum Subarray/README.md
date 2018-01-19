## Maximum Subarray
求最大子序列


#### Approach  
扫一遍，维护一个`sum`，如果`当前值+sum>=0`就把当前值加入区间，如果小的话就把区间重置