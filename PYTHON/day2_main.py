import unittest 
import day2_que
class check_palindrome(unittest.TestCase):
    def test_palin(self):
        c="abba"
        status = day2_que.str1(c)
        self.assertEqual(status,"palindrome")
   
    def test_palin(self):
        c=[[2,4],[6,2]]
        b=[[5,8],[1,2]]
        status = day2_que.mul(c,b)
        self.assertEqual(status,[[14,24],[32,52]])

    def test_palin(self):
        c=[[5,4],[6,10]] 
        m=[[3,8],[11,2]]
        status = day2_que.add1(c,m)
        self.assertEqual(status,[[8,12],[17,12]])
    
    def test_vowstr(self):
        c="string"
        status = day2_que.word(c)
        self.assertEqual(status,"ng")         
        
if __name__ == '__main__': 
    unittest.main() 