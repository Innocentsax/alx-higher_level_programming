#!/usr/bin/python3
"""Unittest for base.py file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class Test_Base(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for base.py file"""

    def test_instance_type_id_class(self):
        """Checks for a instance of the class
        """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b2 = Base()
        self.assertTrue(type(b1) == type(b2))
        self.assertFalse(id(b1) == id(b2))

    def test_none_id(self):
        """Checks when id is none
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 4)

    def test_id_value(self):
        """Checks when id has a integer value
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1.id = 4
        self.assertEqual(b1.id, 4)
        b2 = Base(50)
        self.assertEqual(b2.id, 50)
        b1 = Base(-4)
        self.assertEqual(b1.id, -4)
        b2 = Base(0)
        self.assertEqual(b2.id, 0)
        b1 = Base(100e+1000)
        self.assertEqual(b1.id, 100e+1000)
        b1.__init__(30)
        self.assertEqual(b1.id, 30)

    def test_object_attributtes(self):
        """Check for attributes dictionary of a object"""
        b1 = Base()
        self.assertEqual(b1.__dict__, {'id': 1})
        b2 = Base()
        self.assertEqual(b2.__dict__, {'id': 2})
        b3 = Base(100)
        self.assertEqual(b3.__dict__, {'id': 100})

    def test_raise_errors(self):
        """Check for raises errors
        """
        with self.assertRaises(AttributeError):
            b1 = Base()
            print(b1.x)
        with self.assertRaises(NameError):
            b1 = Base_geometry()
        with self.assertRaises(AttributeError):
            b1.to_dictionary()

    def test_JSON_string(self):
        """Check for JSON_string method
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = (r1.to_dictionary())
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 7], ["id", 1], '
                         '["width", 10], ["x", 2], ["y", 8]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        r2 = Rectangle(10, 7, 2, 8, 30)
        dictionary = r2.to_dictionary()
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 7], ["id", 30], '
                         '["width", 10], ["x", 2], ["y", 8]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        r3 = Rectangle(30, 50)
        dictionary = r3.to_dictionary()
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 50], ["id", 2], '
                         '["width", 30], ["x", 0], ["y", 0]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        r4 = Rectangle(30, 50, 0, 0)
        dictionary = r4.to_dictionary()
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 50], ["id", 3], '
                         '["width", 30], ["x", 0], ["y", 0]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        r5 = Rectangle(30, 50, 0, 0, 89)
        dictionary = r5.to_dictionary()
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 50], ["id", 89], '
                         '["width", 30], ["x", 0], ["y", 0]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        dictionary = None
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '[]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        dictionary = []
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '[]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

    def test_save_to_file(self):
        """Checks save_to_file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x), '[{"y": 8, "x": 2, '
                                        '"id": 1, "width": 10, "height": 7}, '
                                        '{"y": 0, "x": 0, "id": 2, '
                                        '"width": 2, "height": 4}]')))
            self.assertEqual(sum_read, sum_expected)

        r1 = Rectangle(10, 7)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x), '[{"y": 0, "x": 0, '
                                        '"id": 3, "width": 10, "height": 7}, '
                                        '{"y": 0, "x": 0, "id": 4, '
                                        '"width": 2, "height": 4}]')))
            self.assertEqual(sum_read, sum_expected)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')


    def test_rectangle_save_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            result = file.read()
            self.assertEqual(result, '[]')

        # check for square object
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x), '[{"y": 2, "x": 7, '
                                        '"id": 8, "size": 10}, '
                                        '{"y": 0, "x": 4, "id": 1, '
                                        '"size": 2}]')))
            self.assertEqual(sum_read, sum_expected)

        r1 = Square(10, 7)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x), '[{"y": 0, "x": 7, '
                                        '"id": 2, "size": 10}, '
                                        '{"y": 0, "x": 4, "id": 3, '
                                        '"size": 2}]')))
            self.assertEqual(sum_read, sum_expected)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_square_save_to_file(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            result = f.read()
            self.assertEqual(result, '[]')

    def test_from_json_string(self):
        """Checks from_json_string method
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},
                                       {'height': 7, 'width': 1, 'id': 7}])
        self.assertTrue(type(list_output) == list)

        list_input = [
                    {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2},
                    {'id': 7, 'width': 1, 'height': 7, 'x': 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89,
                                        'x': 3, 'y': 2},
                                       {'height': 7, 'width': 1, 'id': 7,
                                        'x': 3}])
        self.assertTrue(type(list_output) == list)

        list_input = [
                    {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2},
                    {'id': 7, 'width': 1, 'height': 7, 'x': 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89,
                                        'x': 3, 'y': 2},
                                       {'height': 7, 'width': 1,
                                        'id': 7, 'x': 3}])
        self.assertTrue(type(list_output) == list)

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

    def test_create(self):
        """Checks create method
        """
        # Checks create Rectangle
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Rectangle(3, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (3) 0/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Rectangle(3, 5, 3, 4, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (89) 3/4 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Rectangle(3, 5, 3, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (6) 3/4 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        # Checks for create square
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (8) 5/1 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (10) 5/0 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(3, 5, 3, 89)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (89) 5/3 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(50)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (13) 0/0 - 50")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """Checks for load_from_file
        """
        # Check for rectangle load from file
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output), "[]")

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        r1 = Rectangle(10, 50)
        r2 = Rectangle(2, 4, 0, 0, 89)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        r1 = Rectangle(10, 50)
        r2 = Rectangle(2, 4, 0, 0)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        # Check for square load from file
        list_square_output = Square.load_from_file()
        self.assertEqual(str(list_square_output), "[]")

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

        s1 = Square(10, 50)
        s2 = Square(2, 0, 0, 89)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

        s1 = Square(10, 50)
        s2 = Square(2, 4, 0, 0)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

    def test_save_csv(self):
        """Checks save_csv method
        """
        # Checks save to csv file
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), '[]')

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        sum_expected = sum(list(map(lambda x: ord(x), 'id,width,height,x,y\n'
                                    '1,10,7,2,8\n'
                                    '2,2,4,0,0\n')))
        with open("Rectangle.csv", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            self.assertEqual(sum_read, sum_expected)

        r1 = Rectangle(10, 7)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x),
                                        'id,width,height,x,y\n'
                                        '3,10,7,0,0\n'
                                        '4,2,4,0,0\n')))
            self.assertEqual(sum_read, sum_expected)

    def test_load_csv(self):
        """Checks load_csv method
        """
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output), "[]")

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        r1 = Rectangle(10, 50)
        r2 = Rectangle(2, 4, 0, 0, 89)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        r1 = Rectangle(10, 50)
        r2 = Rectangle(2, 4, 0, 0)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

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
