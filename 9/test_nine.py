import unittest
import nine

class TestNine(unittest.TestCase):

    def test_tail_follows_straight_up(self):
        self.assertEqual(nine.tail_follows(3,3,3,1), (3,2))

    def test_tail_follows_straight_down(self):
        self.assertEqual(nine.tail_follows(1,1,3,1), (2,1))
    
    def test_tail_follows_straight_left(self):
        self.assertEqual(nine.tail_follows(2,6,2,4), (2,5))
    
    def test_tail_follows_straight_right(self):
        self.assertEqual(nine.tail_follows(5,9,5,11), (5,10))

    def test_tail_follows_diag_up_right(self):
        self.assertEqual(nine.tail_follows(4,4,3,2), (4,3))
    
    def test_tail_follows_diag_down_left(self):
        self.assertEqual(nine.tail_follows(0,0,1,2), (0,1))
    
    def test_tail_follows_diag_up_left(self):
        self.assertEqual(nine.tail_follows(4,4,5,2), (4,3))
    
    def test_tail_follows_diag_down_right(self):
        self.assertEqual(nine.tail_follows(4,0,3,2), (4,1))
    
    def test_tail_holds_diag_adjacent(self):
        self.assertEqual(nine.tail_follows(4,4,3,3), (3,3))
    
    def test_tail_holds_vertical_adjacent(self):
        self.assertEqual(nine.tail_follows(4,4,4,3), (4,3))

if __name__ == "__main__":
    unittest.main()
