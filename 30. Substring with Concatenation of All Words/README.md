## Substring with Concatenation of All Words
给一个字串S`barfoothefoobarman`，和一个字符串list words`[abc,def]`其中words中字符串长度均相同，求所有words拼接后在`S`中的下面

#### Approach 
由于字符串长度相同，那么可以采用滑动窗口的方式，设置一个窗口，符合的话进入，不符合的话往后移。每次下标i都增加`len(words[0])`。
>比如根据题目中的例子，字符串s的长度n为18，words数组中有两个单词(cnt=2)，每个单词的长度len均为3，那么遍历的顺序为0，3，6，8，12，15，然后偏移一个字符1，4，7，9，13，16，然后再偏移一个字符2，5，8，10，14，17，这样就可以把所有情况都遍历到。