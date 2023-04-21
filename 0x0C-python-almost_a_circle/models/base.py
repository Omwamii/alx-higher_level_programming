#!/usr/bin/python3
"""
base class module
"""
import json
import csv
import turtle


class Base:
    """ 'Base' class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string rep of a list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep to a file """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            data = "[]"
        else:
            obj_dicts = []
            for obj in list_objs:
                obj_dicts.append(obj.to_dictionary())  # store dict rep of objs
            data = cls.to_json_string(obj_dicts)  # convert list to json rep
        with open(filename, "w") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """ return list of the JSON string rep """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                attrs = cls.from_json_string(f.read())
                return [cls.create(**attr) for attr in attrs]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes an object in cvs """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                   fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes data from csv file returning list of instances
            created from the csv file or [] if file not found
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                attr_dicts = csv.DictReader(f, fieldnames=fieldnames)
                attr_dicts = [dict([i, int(j)] for i, j in k.items())
                              for k in attr_dicts]
                return [cls.create(**k) for k in attr_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
