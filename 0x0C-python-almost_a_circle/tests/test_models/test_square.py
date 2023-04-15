#!/usr/bin/python3
"""Unittest for square.py file
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class Test_square(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for square.py file
    """

    def test_instance_class(self):
        """Checks for a instance of the class
        """
        s1 = Square(10)
        self.assertIsInstance(s1, Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(id(Square) != id(Rectangle))
        self.assertTrue(id(Square) != id(Base))
        self.assertTrue(type(Square) == type(Rectangle))
        self.assertTrue(type(Square) == type(Base))
        s2 = Square(2)
        self.assertTrue(type(s1) == type(s2))
        self.assertFalse(id(s1) == id(s2))

    def test_init_attributes(self):
        """Checks when id is none
        """
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(20, 40)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 20)
        self.assertEqual(s2.x, 40)
        self.assertEqual(s2.y, 0)

        s3 = Square(10, 2, 4, 5)
        self.assertEqual(s3.id, 5)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 4)

        s4 = Square(10, 2, 6)
        self.assertEqual(s4.id, 3)
        self.assertEqual(s4.size, 10)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 6)

        s5 = Square(10, 2, 4, 50)
        self.assertEqual(s5.id, 50)
        self.assertEqual(s5.size, 10)
        self.assertEqual(s5.x, 2)
        self.assertEqual(s5.y, 4)

        s6 = Square(10, 2, 4, 180)
        s6.id = 50
        self.assertEqual(s6.id, 50)
        s6.size = 100
        self.assertEqual(s6.size, 100)
        s6.x = 40
        self.assertEqual(s6.x, 40)
        s6.y = 50
        self.assertEqual(s6.y, 50)

    def test_raise_errors(self):
        """Check for raises errors
        """
        # checks for instances
        with self.assertRaises(TypeError):
            s1 = Square()
        with self.assertRaises(NameError):
            s1 = Square_shape()
        with self.assertRaises(AttributeError):
            s1 = Square(10, 80)
            s1.to_json()
        with self.assertRaises(ValueError):
            s3 = Square(-4)
        with self.assertRaises(TypeError):
            s4 = Square("4")
        with self.assertRaises(TypeError):
            s6 = Square(10, 4, "9")
        with self.assertRaises(TypeError):
            s7 = Square(10, "4", 9)
        with self.assertRaises(ValueError):
            s8 = Square(10, 4, -5, 7)
        with self.assertRaises(ValueError):
            s9 = Square(10, -4, 5, 10)
        with self.assertRaises(TypeError):
            s10 = Square(10, 4, 5, 10, 100)
        with self.assertRaises(ValueError):
            s11 = Square(0)

        # Checks for setters
        with self.assertRaises(ValueError):
            s1.x = -4
        with self.assertRaises(TypeError):
            s1.x = "4"
        with self.assertRaises(ValueError):
            s1.size = -10
        with self.assertRaises(TypeError):
            s1.size = "10"
        with self.assertRaises(ValueError):
            s1.y = -4
        with self.assertRaises(TypeError):
            s1.y = "30"
        # checks to_dicitonary method
        with self.assertRaises(AttributeError):
            s2 = None
            s2.to_dictionary
        # Checks for update method
        with self.assertRaises(ValueError):
            s1.update(10, -10, 20, 40)
        with self.assertRaises(TypeError):
            s1.update(10, 10, "20", 40)
        with self.assertRaises(ValueError):
            s1.update(id=10, x=10, y=-20, size=40)
        with self.assertRaises(TypeError):
            s1.update(id=10, x=10, y=20, size="30")

    def test_area(self):
        """Check area method of square objects
        """
        s1 = Square(3, 2)
        area = s1.area()
        self.assertEqual(area, 9)

        s2 = Square(3, 2)
        area = Square.area(s2)
        self.assertEqual(area, 9)

        s3 = Square(50, 20, 4, 10)
        area = s3.area()
        self.assertEqual(area, 2500)

        s4 = Rectangle(5, 5, 4)
        area = s4.area()
        self.assertEqual(area, 25)

        s5 = Square(10)
        area = s5.area()
        self.assertEqual(area, 100)

    def test_display(self):
        """Checks display method for square
        """
        output_1 = "#\n"
        s1 = Square(1)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            s1.display()
            self.assertEqual(mock_out.getvalue(), output_1)

        output_2 = "##\n##\n"
        s2 = Square(2, 0)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            s2.display()
            self.assertEqual(mock_out.getvalue(), output_2)

        output_3 = "\n\n  ###\n  ###\n  ###\n"
        s3 = Square(3, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            s3.display()
            self.assertEqual(mock_out.getvalue(), output_3)

        output_4 = "  ##\n  ##\n"
        s4 = Square(2, 2, 0)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            s4.display()
            self.assertEqual(mock_out.getvalue(), output_4)

        output_5 = "\n\n  ##\n  ##\n"
        s5 = Square(2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            s5.display()
            self.assertEqual(mock_out.getvalue(), output_5)

        output_6 = "\n\n\n  ##\n  ##\n"
        s6 = Square(2, 2, 3, 100)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            s6.display()
            self.assertEqual(mock_out.getvalue(), output_6)

    def test_str(self):
        """Check str method
        """
        s1 = Square(4, 6, 2, 1)
        self.assertEqual(str(s1), "[Square] (1) 6/2 - 4")
        s2 = Square(5, 5, 1)
        self.assertEqual(str(s2), "[Square] (1) 5/1 - 5")
        s3 = Square(5, 5)
        self.assertEqual(str(s3), "[Square] (2) 5/0 - 5")
        s4 = Square(4, 6, 2, 50)
        self.assertEqual(s4.__str__(), "[Square] (50) 6/2 - 4")

    def test_update(self):
        """Check update method
        """
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        s1.update(10, 10, 10, 10, x=1, size=2, y=3, id=30)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")
        s1.update(73, id=30)
        self.assertEqual(s1.__str__(), "[Square] (73) 10/10 - 10")
        s1.update(50)
        self.assertEqual(s1.__str__(), "[Square] (50) 10/10 - 10")

    def test_dictionary_representation(self):
        """Check to_dictionary method
        """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10})

        s2 = Square(1, 1)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(s2_dictionary, {'x': 1, 'y': 0, 'id': 2, 'size': 1})

        s3 = Square(10, 0, 2)
        s3_dictionary = s3.to_dictionary()
        self.assertEqual(s3_dictionary, {'x': 0, 'y': 2, 'id': 3, 'size': 10})

        s4 = Square(10)
        s4_dictionary = s4.to_dictionary()
        self.assertEqual(s4_dictionary, {'x': 0, 'y': 0, 'id': 4, 'size': 10})

        s5 = Square(10, 2, 5, 6)
        s5_dictionary = s5.to_dictionary()
        self.assertEqual(s5_dictionary, {'x': 2, 'y': 5, 'id': 6, 'size': 10})

    def tearDown(self):
        """Tear down test method to reset class attribute
        """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
