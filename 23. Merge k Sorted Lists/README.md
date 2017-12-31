## Merge k Sorted Lists

k个有序序列合并

#### Approach 1

同2个有序序列合并，每次对k个头部进行比较，复杂度O(kN)

#### Approach 2
对`Approach 1`的优化
k个头部比较时采用优先队列/小跟堆 的方式 复杂度O(Nlogk)