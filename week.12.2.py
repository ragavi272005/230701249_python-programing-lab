def countKDiff (nums, k):
        count=0
        from collections import Counter
        mydict=Counter(nums)   
        for i in mydict:
            if i+k in mydict:
                count=count+
mydict[i]*mydict[i+k]  
        return count
