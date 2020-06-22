import unittest 
import day1_que
class check_palindrome(unittest.TestCase):
    def test_palin(self):
        c="aBcDEFz"
        status = day1_que.strpalindrome(c)
        self.assertEqual(status,"AbCdefZ")
    def test_sumlist(self):
        c=[[1,2,3],4,[5,6]]
        status = day1_que.listsum(c)
        self.assertEqual(status,21) 
        
if __name__ == '__main__': 
    unittest.main() 
