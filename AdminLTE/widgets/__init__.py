# -*- coding: utf-8 -*-

class _ContainsMeta(type):
    def __contains__(self, item):
        return hasattr(self, item.upper())

class COLORS(object):
    AQUA = "aqua"
    BLACK = "black"
    BLUE = "blue"
    FUCHSIA = "fuchsia"
    GRAY = "gray"
    GREEN = "green"
    LIGHTbLUE = "lightBlue"
    LIME = "lime"
    MAROON = "maroon"
    NAVY = "navy"
    OLIVE = "olive"
    ORANGE = "orange"
    PURPLE = "purple"
    RED = "red"
    TEAL = "teal"
    YELLOW = "yellow"

    __metaclass__ = _ContainsMeta
    def __init__(self):
        raise ValueError('Bound is not allowed for this class.')

class WIDGET_TYPES(object):
    PRIMARY = "primary"
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"

    __metaclass__ = _ContainsMeta
    def __init__(self):
        raise ValueError('Bound is not allowed for this class.')

class WidgetBase(object):
    classes = None
    request = None

    def __init__(self, request=None, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        if request:
            self.set_request(request)
        if self.classes is None:
            self.classes = []

    def set_request(self, request):
        self.request = request
        if hasattr(self, 'children') and getattr(self, 'children'):
            for child in getattr(self, 'children'):
                child.set_request(request)

    def to_html(self):
        return ''

    def __str__(self):
        return self.to_html()

class FontAwesomeIcon(WidgetBase):
    def __init__(self, name, color=None, **kwargs):
        super(FontAwesomeIcon, self).__init__(**kwargs)

        self.name = name
        if color:
            self.classes.append("text-%s" % color)

    def to_html(self):
        return '<i class="fa fa-%s %s"></i>' % (self.name, " ".join(self.classes))

class Label(WidgetBase):
    def __init__(self, data, type=None, **kwargs):
        super(Label, self).__init__(**kwargs)

        self.data = data
        if type:
            self.classes.append("label-%s" % type)

    def to_html(self):
        return '<span class="label %s">%s</span>' % (" ".join(self.classes), self.data)
