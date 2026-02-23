a=[4,3,2,9]
b=1
for i in range(len(a)-1,-1,-1):
    a[i]+=b
    if a[i]>=10:
        a[i]=0
        b=1
    else:
        b=0
        break
print(a)

digits=[1,2,3]
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a=1
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=a
            if digits[i]>=10:
                digits[i]=0
                a=1
            else:
                a=0
                break
        
print(digits)
       
    
