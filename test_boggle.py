import unittest
import boggle

class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """
    
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
        
    def test_grid_size_is_width_times_height(self):
        """
        Test it to ensure that the total sizeof the grid
        is equal to width * height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)

def test_grid_coordinates(self):
    """
    Test to ensure that all of the coordinates
    inside of the gird can be accessed
    """
    grid = boggle.make_grid(2, 2)
    self.assertIn((0, 0), grid)
    self.assertIn((0, 1), grid)
    self.assertIn((1, 0), grid)
    self.assertIn((1,1), grid)
    self.assertNotIn((2, 2), grid)










#==========================================

# boggle test
#class test_boggle(unittest.TestCase):
    #def test_is_this_thing_on(self):
        #self.assertEqual(1,1)