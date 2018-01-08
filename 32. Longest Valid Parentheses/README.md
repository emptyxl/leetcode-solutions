## Longest Valid Parentheses
寻找最长有效括号匹配子序列

#### Approach 1 DP

d[i] 表示 以`i`为末尾的最长有效匹配子序列长度,则初值为`0`，动归方程如下：

```
d[i] = d[i-2]+2     s[i]==')' and s[i-1]=='('
d[i] = d[i-1]+d[i-dp[i-1]-2]+2     s[i]==')' and s[i-1]==')' and s[i-dp[i-1]-1]=='('
```

#### Approach 2 stack
利用栈 从左到右扫描 记录整体最长和当前长度