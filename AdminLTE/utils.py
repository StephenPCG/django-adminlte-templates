# -*- coding: utf-8 -*-

class ALTE_COLORS:
    LIGHTbLUE = "lightBlue"
    RED = "red"
    GREEN = "green"
    AQUA = "aqua"
    YELLOW = "yellow"
    BLUE = "blue"
    NAVY = "navy"
    TEAL = "teal"
    OLIVE = "olive"
    LIME = "lime"
    ORANGE = "orange"
    FUCHSIA = "fuchsia"
    PURPLE = "purple"
    MAROON = "maroon"
    BLACK = "black"
    GRAY = "gray"

class ALTE_ELEM_TYPES:
    PRIMARY = "primary"
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"

def faicon(name, color=None, classes=None):
    """Returns FontAwesome icon
    """
    if not classes:
        classes = []
    if color:
        classes.append("text-%s" % color)
    return '<i class="fa fa-%s %s"></i>' % (name, " ".join(classes))

def label(data, type=None, classes=None):
    if not classes:
        classes = []
    if type:
        classes.append("label-%s" % type)
    return '<span class="label %s">%s</span>' % (" ".join(classes), data)
