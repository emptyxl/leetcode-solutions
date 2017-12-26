## Longest Common Prefix

n个字符串求最长公共前缀



#### Approach 1 - 横向扫描



```
LCP(S1…Sn)=LCP(LCP(LCP(S1,S2),S3),…Sn)
```

#### Approach 2 - 纵向扫描



```
c = *strs.begin()[i]
```

比较每个str第i位是否为c



#### Approach 3 - 分治

![](https://github.com/emptyxl/leetcode-solutions/raw/master/14.Longest-Common-Prefix/14_lcp_diviso_et_lmpera.png)

#### Approach 4 - 二分搜索

![](https://github.com/emptyxl/leetcode-solutions/raw/master/14.Longest-Common-Prefix/14_lcp_binary_search.png)

二分搜索最长公共前缀可能的最大长度

### Further Thoughts

假设存在一个集合 S = [S<sub>1</sub>,S<sub>2</sub>...S<sub>n</sub>]  求一个字符串`q` 和集合`s` 的LCP，且此算法会频繁调用

首先`S` 的存储使用`Trie` 字典树结构：

![](https://github.com/emptyxl/leetcode-solutions/raw/master/14.Longest-Common-Prefix/Trie_example.png)



由于要求`q`和`S` 的最长公共前缀，即求**从根节点开始，最长的只有一个孩子的节点序列，且节点序列字母满足`q` **