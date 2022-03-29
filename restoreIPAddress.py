class Solution(object):
    def restoreIpAddresses(self, s):
        output = []
         
        def backtrack(str, result, stage): 
           
            if(stage > 4): 
                return
            if(stage == 4 and len(str) > 0):
                return
            if(stage == 4 and len(str) == 0):
                output.append(result)

  
                return

            for i in range(0,min(3,len(str))): 
                single_spot = str[0:i+1]
              
                if(int(single_spot) <= 255):

                    if(len(single_spot) >= 2 and single_spot[0] == "0"):
                        return
                    else:
                        if(stage == 3):
                            backtrack(str[i+1:], result + single_spot , stage+1)
                        else:
                            backtrack(str[i+1:], result + single_spot + ".", stage+1)
        backtrack(s, "", 0)
        return output

a = Solution()
print(a.restoreIpAddresses("25525511135"))
