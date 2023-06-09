import sys

class Solution:
    # Write your code here
    stack = ''
    queue = ''
    def pushCharacter(self,s):
        self.stack = self.stack + s
    def enqueueCharacter(self,s):
        self.queue = s + self.queue
    def popCharacter(self):
        a = self.stack[-1]
        self.stack = self.stack[0:len(self.stack)-2]
        return a
    def dequeueCharacter(self):
        a = self.queue[-1]
        self.queue = self.queue[0:len(self.queue)-2]
        return a
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
