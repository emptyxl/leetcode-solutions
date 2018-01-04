## Divide Two Integers

求两个数的整除结果 不能使用乘法、除法、和mod运算

#### Approach 
采用减法，但要注意一下 除数很小时会超时，所以采用**移位运算动态增加除数**

```python
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        coefficient = 1
        if dividend < 0 and divisor >= 0:
            coefficient = -1
            dividend = -dividend
        elif dividend >= 0 and divisor < 0:
            coefficient = -1
            divisor = -divisor
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend - temp >= divisor:
                dividend = dividend - temp
                result += i
                temp <<= 1
                i <<= 1
        if coefficient < 0 and result > 0:
            result = -result
        return min(max(-2147483648, result), 2147483647)
```
