import unittest 
import day3_que
class check_palindrome(unittest.TestCase):
    def test_anagram(self):
        c=["eat", "tea", "far", "raf", "arf"]
        status =day3_que.groupAnagrams(c)
        self.assertEqual(status,[['eat', 'tea'], ['far', 'raf', 'arf']])
    def test_longalpha(self):
        m="abcaklmoeeffd"
        status =day3_que.alph(m)
        self.assertEqual(status,"Longest substring in alphabetical order is: aklmo")
    def test_binary(self):
        d=5
        status =day3_que.binary(d)
        self.assertEqual(status,'101 1')
    def test_vow1(self):
        c="I am reading a book"
        status =day3_que.vow(c)
        self.assertEqual(status,['reading', 'book', 'am', 'a', 'I'])
    def test_matrix(self):
        m=[[1,2],[3,4]]
        status =day3_que.mat(m)
        self.assertEqual(status,"1243")
    def test_longpalidrome(self):
        m="cabbage"
        status =day3_que.longpal(m)
        self.assertEqual(status,"abba")
    
        
if __name__ == '__main__': 
    unittest.main() 