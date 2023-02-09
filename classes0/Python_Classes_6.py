class Prime():
    def prime(self,nums):
        for num in nums:
            bool = True
            for x in range(2, num - 1):
                if num % x == 0:
                    bool = False
                    break
            if bool == True:
                p.append(num)
                

nums = input(int()).split()
    
p = []        
number = Prime()
number.prime(nums)
print(p)   