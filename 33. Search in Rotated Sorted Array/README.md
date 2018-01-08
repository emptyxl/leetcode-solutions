## Search in Rotated Sorted Array
在有序循环队列中找到一个值

#### Approach
二分查找，首先二分找到最小值，此下标即为偏移量

```
    rot 为找到的最小值下标
    while(lo<=hi){
        int mid=(lo+hi)/2;
        int realmid=(mid+rot)%n;
        if(A[realmid]==target)return realmid;
        if(A[realmid]<target)lo=mid+1;
        else hi=mid-1;
    }
```

