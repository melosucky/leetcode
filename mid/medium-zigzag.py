# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this ...
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        righe=[""for r in range(numRows)]
        n_riga, step = 0,1
        for lettera in s:
            righe[n_riga]+=lettera

            if n_riga==0:
                step = 1
            elif n_riga==numRows-1:
                step=-1

            n_riga+=step
        return "".join(righe)    
            


stringa="PAYPALISHIRING" #14 ltrs
numrighe=3

