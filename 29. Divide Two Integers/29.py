class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        coefficient = 1
        if dividend<0 and divisor>=0:
            coefficient = -1
            dividend = -dividend
        elif dividend>=0 and divisor<0:
            coefficient = -1
            divisor = -divisor
        elif dividend<0 and divisor<0:
            dividend = -dividend
            divisor = -divisor
        result = 0
        while dividend>=divisor:
            temp,i = divisor,1
            while dividend-temp>=divisor:
                dividend = dividend - temp
                result += i
                temp <<= 1
                i <<= 1
        if coefficient<0 and result>0:
            result = -result
        return min(max(-2147483648, result), 2147483647)


def main():
    so = Solution()
    print(so.divide(1, 1))

if __name__ == '__main__':
    main()
