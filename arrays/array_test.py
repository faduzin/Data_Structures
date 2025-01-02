from array_from_scratch import array_from_scratch
import unittest

class TestArray(unittest.TestCase):
    def setUp(self):
        """
        Runs before each test method.
        Here we initialize a fresh Array for testing.
        """
        # Assuming the Array class is imported or defined above.
        self.arr = array_from_scratch() 

    def test_initialization(self):
        """
        Test that a newly created array has size=0 and default capacity.
        """
        self.assertEqual(len(self.arr), 0, "New array should have size 0.")
        # Depending on how you've implemented default capacity:
        self.assertEqual(self.arr.capacity, 10, "Default capacity should be 1.")

    def test_append_and_len(self):
        """
        Test appending elements increases size and stores elements correctly.
        """
        # Append first element
        self.arr.append(10)
        self.assertEqual(len(self.arr), 1)
        self.assertEqual(self.arr[0], 10)
        
        # Append second element
        self.arr.append(20)
        self.assertEqual(len(self.arr), 2)
        self.assertEqual(self.arr[1], 20)

    def test_pop(self):
        """
        Test popping elements from the array.
        """
        # Append some items first
        self.arr.append('a')
        self.arr.append('b')
        self.arr.append('c')

        popped = self.arr.pop()
        self.assertEqual(popped, 'c')
        self.assertEqual(len(self.arr), 2)

        popped = self.arr.pop()
        self.assertEqual(popped, 'b')
        self.assertEqual(len(self.arr), 1)

        popped = self.arr.pop()
        self.assertEqual(popped, 'a')
        self.assertEqual(len(self.arr), 0)

        # Popping from an empty array should raise IndexError
        with self.assertRaises(IndexError):
            self.arr.pop()

    def test_insert(self):
        """
        Test inserting elements at specific indices.
        """
        # Start with empty array
        # Insert at index 0 when array is empty
        self.arr.insert(0, 'x')
        self.assertEqual(len(self.arr), 1)
        self.assertEqual(self.arr[0], 'x')

        # Insert at the end (index == size)
        self.arr.insert(1, 'y')
        self.assertEqual(len(self.arr), 2)
        self.assertEqual(self.arr[1], 'y')

        # Insert at the front
        self.arr.insert(0, 'z')
        self.assertEqual(len(self.arr), 3)
        self.assertEqual(self.arr[0], 'z')
        self.assertEqual(self.arr[1], 'x')
        self.assertEqual(self.arr[2], 'y')

        # Insert in the middle
        self.arr.insert(1, 'm')
        self.assertEqual(len(self.arr), 4)
        self.assertEqual(self.arr[0], 'z')
        self.assertEqual(self.arr[1], 'm')
        self.assertEqual(self.arr[2], 'x')
        self.assertEqual(self.arr[3], 'y')

        # Inserting out of range should raise IndexError
        with self.assertRaises(IndexError):
            self.arr.insert(999, 'oops')

    def test_remove(self):
        """
        Test removing elements at a specific index.
        """
        # Fill the array
        self.arr.append('a')
        self.arr.append('b')
        self.arr.append('c')
        self.arr.append('d')

        # Remove middle element
        self.arr.remove(1)  # should remove 'b'
        self.assertEqual(len(self.arr), 3)
        self.assertEqual(self.arr[0], 'a')
        self.assertEqual(self.arr[1], 'c')
        self.assertEqual(self.arr[2], 'd')

        # Remove first element
        self.arr.remove(0)  # should remove 'a'
        self.assertEqual(len(self.arr), 2)
        self.assertEqual(self.arr[0], 'c')
        self.assertEqual(self.arr[1], 'd')

        # Remove last element
        self.arr.remove(1)  # should remove 'd'
        self.assertEqual(len(self.arr), 1)
        self.assertEqual(self.arr[0], 'c')

        # Attempting to remove out of range
        with self.assertRaises(IndexError):
            self.arr.remove(10)

        # Remove last remaining element
        self.arr.remove(0)  # should remove 'c'
        self.assertEqual(len(self.arr), 0)

    def test_get_item_and_set_item(self):
        """
        Test indexing (getitem) and assignment (setitem).
        """
        # Pre-populate
        for i in range(5):
            self.arr.append(i)
        
        # Test getitem
        self.assertEqual(self.arr[0], 0)
        self.assertEqual(self.arr[4], 4)
        
        # Test setitem
        self.arr[0] = 99
        self.assertEqual(self.arr[0], 99)

        # Index out of range for getitem should raise error
        with self.assertRaises(IndexError):
            _ = self.arr[999]

        # Index out of range for setitem should raise error
        with self.assertRaises(IndexError):
            self.arr[999] = 1000

    def test_resize(self):
        """
        Test that the array properly resizes when capacity is reached.
        """
        initialcapacity = self.arr.capacity  # likely 1
        # Appending until we exceed capacity
        for i in range(20):  # definitely goes beyond capacity=1
            self.arr.append(i)
        
        self.assertTrue(self.arr.capacity >= 20, 
                        "Array capacity should have expanded to fit 20 elements.")
        self.assertEqual(len(self.arr), 20)
        # Check that each appended element is still correct
        for i in range(20):
            self.assertEqual(self.arr[i], i)

if __name__ == '__main__':
    unittest.main()
