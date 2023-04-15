#!/usr/bin/python3
"""Module base"""
import json
import csv
from collections import OrderedDict
import turtle


class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assign the public instance attribute id
        Args:
           id(int): integer value to manage id in this project
        Return:
           Always nothing.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON
           string representation
        Args:
           list_dictionaries(dict): List of dictionaries
        Return:
           JSON string
        """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that writes the JSON string representation
            of list_objs to a file
        Args:
            list_objs(list): List of objects
        Return:
            Always nothing
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_string = Base.to_json_string(list_dictionaries)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the
           JSON string representation
        Args:
           json_string: JSON string
        Return:
           Python object
        """
        if json_string is None or bool(json_string) is False:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update the class Base and returns a instance with all
           attributes already set
        Args:
           dictionary: Dictionary with all attributes of the object
        Return:
           A instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances
           - the type of these instances depends on cls
        """
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that serializes in CSV
        Args:
           list_objs(list): List of objects
        Return:
           Always nothing
        """
        filename = "{}.csv".format(cls.__name__)
        data = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                data.append(dictionary)
        rectangle_header = ['id', 'width', 'height', 'x', 'y']
        square_header = ['id', 'size', 'x', 'y']
        with open(filename, mode='w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    result = csv.DictWriter(f, fieldnames=rectangle_header)
                elif cls.__name__ == 'Square':
                    result = csv.DictWriter(f, fieldnames=square_header)
                result.writeheader()
                result.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """Method that deserializes in CSV
        """
        filename = "{}.csv".format(cls.__name__)
        instance_list = []
        try:
            with open(filename) as f:
                result = csv.DictReader(f)
                for row in result:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Method that draws the shape with turtle module
        Args:
           list_squares(list): List of square objects
           list_rectangles(list): List of rectangle objects
        Return:
           Always nothing
        """
        # Open screen and set the turtle in the center
        s = turtle.getscreen()
        t = turtle.Turtle()

        # Add a title to my screen
        turtle.title("My first draw with python and tutle module")

        # Customize turtle and screen background
        t.shape("turtle")
        turtle.bgcolor("black")

        # Customize pen for rectangle
        t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
        # Extract the data from the instance rectangle list
        for instance in list_rectangles:
            # Customize pen for rectangle
            t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
            data = instance.to_dictionary()
            # Set the position acording the rectangle object
            t.home()
            t.setpos(data['x'], data['y'])
            # Draw process
            t.pd()
            for i in range(2):
                t.forward(data['width'])
                t.left(90)
                t.forward(data['height'])
                t.left(90)
            t.pu()

        # Customize pen for square
        t.pen(pencolor="red", fillcolor="white", pensize=5, speed=0.5)
        # Extract the data from the instance square list
        for instance in list_squares:
            data = instance.to_dictionary()
            # Set the position acording the square object
            t.home()
            t.setpos(data['x'], data['y'])
            # Draw process
            t.pd()
            for i in range(4):
                t.forward(data['size'])
                t.left(90)
            t.pu()

        # Keeps window open
        turtle.getscreen()._root.mainloop()
