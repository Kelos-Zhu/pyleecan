# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Geometry/Arc.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Line import Line

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Geometry.Arc.draw_FEMM import draw_FEMM
except ImportError as error:
    draw_FEMM = error

try:
    from ..Methods.Geometry.Arc.intersect_line import intersect_line
except ImportError as error:
    intersect_line = error

try:
    from ..Methods.Geometry.Arc.is_on_arc import is_on_arc
except ImportError as error:
    is_on_arc = error

try:
    from ..Methods.Geometry.Arc.split_line import split_line
except ImportError as error:
    split_line = error


from ._check import InitUnKnowClassError


class Arc(Line):
    """Abstract class for arc"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.Arc.draw_FEMM
    if isinstance(draw_FEMM, ImportError):
        draw_FEMM = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc method draw_FEMM: " + str(draw_FEMM))
            )
        )
    else:
        draw_FEMM = draw_FEMM
    # cf Methods.Geometry.Arc.intersect_line
    if isinstance(intersect_line, ImportError):
        intersect_line = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Arc method intersect_line: " + str(intersect_line)
                )
            )
        )
    else:
        intersect_line = intersect_line
    # cf Methods.Geometry.Arc.is_on_arc
    if isinstance(is_on_arc, ImportError):
        is_on_arc = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc method is_on_arc: " + str(is_on_arc))
            )
        )
    else:
        is_on_arc = is_on_arc
    # cf Methods.Geometry.Arc.split_line
    if isinstance(split_line, ImportError):
        split_line = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc method split_line: " + str(split_line))
            )
        )
    else:
        split_line = split_line
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, label="", init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            label = obj.label
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        # Call Line init
        super(Arc, self).__init__(label=label)
        # The class is frozen (in Line init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Arc_str = ""
        # Get the properties inherited from Line
        Arc_str += super(Arc, self).__str__()
        return Arc_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Line
        if not super(Arc, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Line
        Arc_dict = super(Arc, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Arc_dict["__class__"] = "Arc"
        return Arc_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Line
        super(Arc, self)._set_None()
