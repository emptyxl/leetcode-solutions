## Jump Game II
给一个array `A` 其中每个元素代表当前位置可以向后跳的最大步数，求跳到最后一个位置时，最小的次数是多少

#### Approach 1 DP

```
dp[i] 表示 到第i个位置 最小的次数 
初值：
dp[i] = -1 表示跳不到
dp[0] = 0


dp[i] = min{dp[k]+1 | 0<=k<i,k+a[k]>=i,dp[k]>=0}
```

#### Approach 2 BFS
>I try to change this problem to a BFS problem, where nodes in level i are all the nodes that can be reached in i-1th jump. for example. 2 3 1 1 4 , is  
>2||  
>3 1||  
>1 4 ||  