class Alpha:
    def __init__(self):
        pass
        
    def maxPref(self):
        s  = 'abcdefghijklmnopqrstuvwxyz' #string 'S'
        lst1= list(s) #make the string a list
        lst2 = list(input("enter your string: ")) # take a string as list
        while len(lst2) != 26:
            lst2.append('0')
        #print the second list
        #print(lst2)
        count = 0
        for i in range(26):
            if lst1[i]==lst2[i]:
                count = count + 1
            else:
                break
        return count
    
a1 = Alpha()
print(a1.maxPref())
