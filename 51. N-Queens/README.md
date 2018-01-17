## N-Queens
N皇后问题


#### Approach  
八皇后的扩展

`dfs(x[i],level,res)`代表往第level行放时，`x[]`数组表示第level行哪个位置可以放，`res`为当前的放置结果