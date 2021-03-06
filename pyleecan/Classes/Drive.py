# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/Drive.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError


class Drive(FrozenClass):
    """Abstract Drive class"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, Umax=800, Imax=800, is_current=False, init_dict=None, init_str=None
    ):
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
            Umax = obj.Umax
            Imax = obj.Imax
            is_current = obj.is_current
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Umax" in list(init_dict.keys()):
                Umax = init_dict["Umax"]
            if "Imax" in list(init_dict.keys()):
                Imax = init_dict["Imax"]
            if "is_current" in list(init_dict.keys()):
                is_current = init_dict["is_current"]
        # Initialisation by argument
        self.parent = None
        self.Umax = Umax
        self.Imax = Imax
        self.is_current = is_current

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Drive_str = ""
        if self.parent is None:
            Drive_str += "parent = None " + linesep
        else:
            Drive_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Drive_str += "Umax = " + str(self.Umax) + linesep
        Drive_str += "Imax = " + str(self.Imax) + linesep
        Drive_str += "is_current = " + str(self.is_current) + linesep
        return Drive_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Umax != self.Umax:
            return False
        if other.Imax != self.Imax:
            return False
        if other.is_current != self.is_current:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Drive_dict = dict()
        Drive_dict["Umax"] = self.Umax
        Drive_dict["Imax"] = self.Imax
        Drive_dict["is_current"] = self.is_current
        # The class name is added to the dict fordeserialisation purpose
        Drive_dict["__class__"] = "Drive"
        return Drive_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Umax = None
        self.Imax = None
        self.is_current = None

    def _get_Umax(self):
        """getter of Umax"""
        return self._Umax

    def _set_Umax(self, value):
        """setter of Umax"""
        check_var("Umax", value, "float", Vmin=0)
        self._Umax = value

    # Maximum RMS voltage of the Drive
    # Type : float, min = 0
    Umax = property(
        fget=_get_Umax, fset=_set_Umax, doc=u"""Maximum RMS voltage of the Drive"""
    )

    def _get_Imax(self):
        """getter of Imax"""
        return self._Imax

    def _set_Imax(self, value):
        """setter of Imax"""
        check_var("Imax", value, "float", Vmin=0)
        self._Imax = value

    # Maximum RMS current of the Drive
    # Type : float, min = 0
    Imax = property(
        fget=_get_Imax, fset=_set_Imax, doc=u"""Maximum RMS current of the Drive"""
    )

    def _get_is_current(self):
        """getter of is_current"""
        return self._is_current

    def _set_is_current(self, value):
        """setter of is_current"""
        check_var("is_current", value, "bool")
        self._is_current = value

    # True to generate current waveform, False for voltage
    # Type : bool
    is_current = property(
        fget=_get_is_current,
        fset=_set_is_current,
        doc=u"""True to generate current waveform, False for voltage""",
    )
