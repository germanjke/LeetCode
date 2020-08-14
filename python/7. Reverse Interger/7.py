class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        minus = ''
        if strx[0] == '-':
            minus = '-'
            strx = strx[1:len(strx)]
        strx = strx[::-1]
        i = 0
        while strx[0] == '0' and len(strx) != 1:
            strx = strx[1::]
            i += 1
        if int(strx) > 2**31 or int(strx) <= (-1)*(2**31):
            return 0
        else:
            return minus+strx
