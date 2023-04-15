#!/usr/bin/python3
"""Unittest for rectangle.py file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class Test_rectangle(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for rectangle.py file
    """

    def test_instance_class(self):
        """Checks for a instance of the class
        """
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))
        r2 = Rectangle(2, 5)
        self.assertTrue(type(r1) == type(r2))
        self.assertFalse(id(r1) == id(r2))

    def test_init_attributes(self):
        """Checks when id is none
        """
        r1 = Rectangle(10, 60)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 60)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(20, 40)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 40)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 4, 5)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 5)

        r4 = Rectangle(10, 2, 6)
        self.assertEqual(r4.id, 4)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 6)
        self.assertEqual(r4.y, 0)

        r5 = Rectangle(10, 2, 4, 5, 50)
        self.assertEqual(r5.id, 50)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 4)
        self.assertEqual(r5.y, 5)

        r6 = Rectangle(10, 2, 4, 5, 180)
        r6.id = 50
        self.assertEqual(r6.id, 50)
        r6.width = 100
        self.assertEqual(r6.width, 100)
        r6.height = 200
        self.assertEqual(r6.height, 200)
        r6.x = 40
        self.assertEqual(r6.x, 40)
        r6.y = 50
        self.assertEqual(r6.y, 50)

    def test_raise_errors(self):
        """Check for raises errors
        """
        # Checks for diferents instances
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(NameError):
            r1 = Rectangle_shape()
        with self.assertRaises(AttributeError):
            r1 = Rectangle(10, 80)
            r1.to_json()
        with self.assertRaises(TypeError):
            r2 = Rectangle(10)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -4)
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 4)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, "4")
        with self.assertRaises(TypeError):
            r6 = Rectangle("10", 4)
        with self.assertRaises(TypeError):
            r7 = Rectangle(10, 4, "9")
        with self.assertRaises(TypeError):
            r8 = Rectangle(10, 4, 9, "20")
        with self.assertRaises(ValueError):
            r9 = Rectangle(10, 4, -5, 7)
        with self.assertRaises(ValueError):
            r10 = Rectangle(10, 4, 5, -10)
        with self.assertRaises(TypeError):
            r11 = Rectangle(10, 4, 5, 10, 30, 60)
        with self.assertRaises(ValueError):
            r12 = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            r13 = Rectangle(15, 0)

        # Checks for setters
        with self.assertRaises(TypeError):
            r1.x = "4"
        with self.assertRaises(ValueError):
            r1.x = -4
        with self.assertRaises(ValueError):
            r1.width = -10
        with self.assertRaises(TypeError):
            r1.width = "10"
        with self.assertRaises(TypeError):
            r1.height = "30"
        with self.assertRaises(ValueError):
            r1.height = -10
        with self.assertRaises(TypeError):
            r1.y = "10"
        with self.assertRaises(ValueError):
            r1.y = -10
        # Checks for update method
        with self.assertRaises(ValueError):
            r1.update(10, -10, 20, 40)
        with self.assertRaises(TypeError):
            r1.update(10, 10, "20", 40)
        with self.assertRaises(ValueError):
            r1.update(id=10, x=10, y=20, width=40, height=-60)
        with self.assertRaises(TypeError):
            r1.update(id=10, x=10, y=20, width="30", height=40)
        with self.assertRaises(AttributeError):
            r2 = None
            r2.to_dictionary

    def test_area(self):
        """Check area method of rectangle objects
        """
        r1 = Rectangle(3, 2)
        area = r1.area()
        self.assertEqual(area, 6)

        r2 = Rectangle(3, 2)
        area = Rectangle.area(r2)
        self.assertEqual(area, 6)

        r3 = Rectangle(30, 20, 4, 5, 10)
        area = r3.area()
        self.assertEqual(area, 600)

        r4 = Rectangle(5, 5, 4)
        area = r4.area()
        self.assertEqual(area, 25)

    def test_display(self):
        """Checks display method
        """
        output_1 = "#\n"
        r1 = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r1.display()
            self.assertEqual(mock_out.getvalue(), output_1)

        output_2 = "#####\n#####\n"
        r2 = Rectangle(5, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r2.display()
            self.assertEqual(mock_out.getvalue(), output_2)

        output_3 = "\n\n##\n##\n"
        r3 = Rectangle(2, 2, 0, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r3.display()
            self.assertEqual(mock_out.getvalue(), output_3)

        output_4 = "  ##\n  ##\n"
        r4 = Rectangle(2, 2, 2, 0)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r4.display()
            self.assertEqual(mock_out.getvalue(), output_4)

        output_5 = "\n\n  ##\n  ##\n"
        r5 = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r5.display()
            self.assertEqual(mock_out.getvalue(), output_5)

    def test_str(self):
        """Checks str method
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")
        r3 = Rectangle(5, 5)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 5/5")
        r4 = Rectangle(4, 6, 2, 1, 50)
        self.assertEqual(r4.__str__(), "[Rectangle] (50) 2/1 - 4/6")

    def test_update(self):
        """Checks update method
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        r1.update(x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(r1.__str__(), "[Rectangle] (30) 1/3 - 4/2")
        r1.update(id=67)
        self.assertEqual(r1.__str__(), "[Rectangle] (67) 1/3 - 4/2")
        r1.update(10, 10, 10, 10, 10, x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 10/10 - 10/10")
        r1.update(45, x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(r1.__str__(), "[Rectangle] (45) 10/10 - 10/10")
        r1.update(73, id=30)
        self.assertEqual(r1.__str__(), "[Rectangle] (73) 10/10 - 10/10")
        r1.update(50)
        self.assertEqual(r1.__str__(), "[Rectangle] (50) 10/10 - 10/10")
        r1.update()
        self.assertEqual(r1.__str__(), "[Rectangle] (50) 10/10 - 10/10")

    def test_dictionary_representation(self):
        """Checks to_dictionary method
        """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2,
                                         'width': 10})

        r2 = Rectangle(10, 2, 1, 9, 30)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r2_dictionary, {'x': 1, 'y': 9, 'id': 30, 'height': 2,
                                         'width': 10})

        r3 = Rectangle(10, 2)
        r3_dictionary = r3.to_dictionary()
        self.assertEqual(r3_dictionary, {'x': 0, 'y': 0, 'id': 2, 'height': 2,
                                         'width': 10})

        r4 = Rectangle(10, 2)
        r4_dictionary = r4.to_dictionary()
        self.assertEqual(r4_dictionary, {'x': 0, 'y': 0, 'id': 3, 'height': 2,
                                         'width': 10})

        r5 = Rectangle(10, 2, 5, 6)
        r5_dictionary = r5.to_dictionary()
        self.assertEqual(r5_dictionary, {'x': 5, 'y': 6, 'id': 4, 'height': 2,
                                         'width': 10})

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
