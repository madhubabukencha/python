"""
The first line of input contains an integer N, the number of mobile phone numbers.
N lines follow each containing a mobile number.

Output Format:
Print mobile numbers on separate lines in the required format.

Sample Input
3
07895462130
919875641230
9195969878

Sample Output
+91 78954 62130
+91 91959 69878
+91 98756 41230
"""


def wrapper(f):
    def fun(l):
        lst = []
        for j in l:
            nums = str(j)[-10:]
            lst.append(int(nums))
        *a,  = sorted(lst)
        for i in a:
            num = str(i)
            print("+91"+" "+num[:5]+" "+num[5:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
