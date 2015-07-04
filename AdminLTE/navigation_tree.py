# -*- coding: utf-8 -*-

"""
AdminLTE template use NavTree() to build navigation menu.
"""

import re

class NavTree():
    def __init__(self,
            name,
            href='#',
            all_perms=None,
            any_perms=None,
            icon=None,
            icon_color=None,
            active_pattern=None,
            children=None,
            is_header=False,
            label=None):
        # the menu item text
        self.name = name
        # the menu item href target
        self.href = href
        # if not None, the menu item will only show if user has all perms listed
        self.all_perms = all_perms
        # if not None, the menu item will only show if user has any perm listed
        self.any_perms = any_perms
        # icon of menu item, placed in the left side, it will be rendered as "<i class="fa fa-{{icon}}></i>""
        self.icon = icon
        # if not None, will add class="text-{{ icon_color }}" to the icon
        self.icon_color = icon_color
        # the request.url will be matched against this pattern, if matched, will add "class=active" to the menu item
        self.active_pattern = active_pattern
        # sublevel menu items
        self.children = children
        # if True, will be rendered as "<li class='header'>{{ name }}</l>"
        self.is_header = is_header
        # label of menu item, placed in the right side, should be a dict: {"type": xx, "data": xx}
        # if not empty, will add: '<span class="label label-{{ type }} pull-right>{{ data }}</span>"'
        self.label = label

    def to_dict(self, request):
        result = {
            "name": self.name,
            "href": self.href,
            "icon": self.icon,
            "icon_color": self.icon_color,
            "is_header": self.is_header,
        }

        if self.all_perms:
            if not request.user.has_perms(self.all_perms):
                return None
        if self.any_perms:
            if not any([request.user.has_perm(perm) for perm in self.any_perms]):
                return None

        if self.active_pattern is None:
            result['is_active'] = (request.path == self.href)
        elif hasattr(self.active_pattern, 'match') and callable(self.active_pattern.match):
            if self.active_pattern.match(request.path):
                result['is_active'] = True
            else:
                result['is_active'] = False
        elif isinstance(self.active_pattern, str):
            pattern = re.compile(self.active_pattern)
            if pattern.match(request.path):
                result['is_active'] = True
            else:
                result['is_active'] = False


        if self.children:
            children = [child.to_dict(request) for child in self.children]
            result['children'] = [c for c in children if c]
        else:
            result['children'] = []

        if self.label is not None:
            if isinstance(self.label, dict):
                result['label'] = self.label
            elif callable(self.label):
                result['label'] = self.label(request)

        return result
