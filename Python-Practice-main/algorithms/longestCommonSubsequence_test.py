# Wesley Murray
# 2/11/2021
# For testing the longest common subsequence

import unittest
import longestCommonSubsequence as lcs
import random
import string
import math

class TestLongestCommonSubsequence(unittest.TestCase):

    #This method is for testing my custom, memory efficient dynamic programming algorithm
    def test_LongestCommonSequenceEfficDynamic(self):
        #edge cases
        self.assertEqual(lcs.longestCommonSubsequenceBrute("",""),None)
        self.assertEqual(lcs.longestCommonSubsequenceBrute("abc","defgh"),None)
        self.assertEqual(lcs.longestCommonSubsequenceBrute("hfsdui","hfsdui"),["hfsdui"])
        
        #normal cases
        self.assertEqual(lcs.longestCommonSubsequenceBrute("hfsdui","hfsduiksae"),["hfsdui"])
        self.assertEqual(lcs.longestCommonSubsequenceBrute("kjsdhfse","jaukadfj").sort(),['jdf','kdf'].sort())

        #compare with brute force
        for i in range(1,4,100):
            str1=''
            str2=''
            for _ in range(i):
                str1+=random.choice(string.ascii_letters)
                str2+=random.choice(string.ascii_letters)
            
            commonStrsBrute=lcs.longestCommonSubsequenceBrute(str1,str2)
            commonStrsDynam=lcs.longestCommonSubsequenceDynamic(str1,str2)

            if commonStrsDynam==None or commonStrsBrute==None:
                self.assertEqual(commonStrsBrute,commonStrsDynam)
            else:
                self.assertEqual(commonStrsBrute.sort(),commonStrsDynam.sort())

    #This method is for testing longest common subsequence recursive algorithm
    def test_LongestCommonSequenceRecursion(self):
        #edge cases
        self.assertEqual(lcs.longestCommonSubsequenceRecursion("",""),0)
        self.assertEqual(lcs.longestCommonSubsequenceRecursion("ab","cd"),0)
        self.assertEqual(lcs.longestCommonSubsequenceRecursion("hfsdui","hfsdui"),6)

        #normal cases
        self.assertEqual(lcs.longestCommonSubsequenceRecursion("hfsdui","hfsduiksae"),6)
        self.assertEqual(lcs.longestCommonSubsequenceRecursion("kjsdhfse","jaukadfj"),3)

        #compare with brute force algorithm
        for i in range(1,4,100):
            str1=''
            str2=''
            for _ in range(i):
                str1+=random.choice(string.ascii_letters)
                str2+=random.choice(string.ascii_letters)
            commonStrLenDynamic=lcs.longestCommonSubsequenceRecursion(str1,str2)
            commonStrs=lcs.longestCommonSubsequenceBrute(str1,str2)
            commonStrLenBrute=len(commonStrs[0]) if commonStrs!=None else 0
            self.assertEqual(commonStrLenDynamic,commonStrLenBrute)


    #This method is for testing longest common subsequence brute force algorithm
    def test_LongestCommonSequenceBrute(self):
        #edge cases
        self.assertEqual(lcs.longestCommonSubsequenceBrute("",""),None)
        self.assertEqual(lcs.longestCommonSubsequenceBrute("abc","defgh"),None)
        self.assertEqual(lcs.longestCommonSubsequenceBrute("hfsdui","hfsdui"),["hfsdui"])
        
        #normal cases
        self.assertEqual(lcs.longestCommonSubsequenceBrute("hfsdui","hfsduiksae"),["hfsdui"])
        self.assertEqual(lcs.longestCommonSubsequenceBrute("kjsdhfse","jaukadfj").sort(),['jdf','kdf'].sort())

    #test method for listing all substrings
    def test_listAllSubstringsBruteForce(self):
        #edge cases
        self.assertEqual(lcs.listAllSubstringsBruteForce("A"),['A'])
        self.assertEqual(lcs.listAllSubstringsBruteForce(''),[])

        #normal cases
        for i in range(1,4,100):
            base=''
            for _ in range(i):
                base+=random.choice(string.ascii_letters)
            self.assertEqual(len(lcs.listAllSubstringsBruteForce(base)),math.pow(2,i)-1)
        self.assertEqual(lcs.listAllSubstringsBruteForce("CKBE"),['C', 'K', 'B', 'E', 'CK', 'CB', 'CE', 'KB', 'KE', 'BE', 'CKB', 'CKE', 'CBE', 'KBE', 'CKBE'])
        self.assertEqual(lcs.listAllSubstringsBruteForce("ABCD"),['A', 'B', 'C', 'D', 'AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'ABC', 'ABD', 'ACD', 'BCD', 'ABCD'])
        self.assertEqual(lcs.listAllSubstringsBruteForce("DAB"),['D', 'A', 'B','DA', 'DB', 'AB', 'DAB'])

    #test method for getting next substrings
    def test_getNextSubstring(self):
        base="CKBE"
        state=[-1]
        self.assertEqual(lcs.getNextSubstring(base,4,1,state),'C')
        self.assertEqual(lcs.getNextSubstring(base,4,1,state),'K')
        self.assertEqual(lcs.getNextSubstring(base,4,1,state),'B')
        self.assertEqual(lcs.getNextSubstring(base,4,1,state),'E')
        state=[0,0]
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'CK')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'CB')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'CE')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'KB')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'KE')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'BE')
        state=[0,1,1]
        self.assertEqual(lcs.getNextSubstring(base,4,3,state),'CKB')
        self.assertEqual(lcs.getNextSubstring(base,4,3,state),'CKE')
        self.assertEqual(lcs.getNextSubstring(base,4,3,state),'CBE')
        self.assertEqual(lcs.getNextSubstring(base,4,3,state),'KBE')
        state=[0,1,2,2]
        self.assertEqual(lcs.getNextSubstring(base,4,4,state),'CKBE')

if __name__ == '__main__':
    unittest.main()