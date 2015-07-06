# -*- coding: utf-8 -*-

from django.template import loader, Context

import re

from . import WidgetBase
from . import FontAwesomeIcon as FAIcon
from . import Label

class SidebarItem(WidgetBase):
    def is_active(self):
        return False

    def is_hidden(self):
        return False

class SidebarMenuItem(SidebarItem):
    # the menu item text
    name = None
    # the menu item href
    href = '#'
    # the menu item icon, placed left side of text, in html
    icon = None
    # the menu item label, placed right side of text, in html
    label = None
    # if the menu item is active
    active = None
    # used in self.is_active()
    active_path_pattern = None
    # if this is a menu header, a header is not clickable
    is_header = False
    # sublevel menu items
    children = None
    # whether to hide this menu
    hidden = None
    # used in self.is_hidden()
    all_perms = None
    any_perms = None

    def __init__(self, request=None, **kwargs):
        self.children = []
        super(SidebarMenuItem, self).__init__(request, **kwargs)

    def is_active(self):
        if self.is_hidden():
            return False

        if self.active is not None:
            return self.active

        if not self.request:
            return False

        if any([child.is_active() for child in self.children]):
            return True

        if self.active_path_pattern is None:
            return self.href == self.request.path
        elif hasattr(self.active_path_pattern, 'match') and callable(self.active_path_pattern):
            return self.active_path_pattern.match(self.request.path)
        elif isinstance(self.active_path_pattern, str):
            pattern = re.compile(self.active_path_pattern)
            return pattern.match(self.request.path)

    def is_hidden(self):
        if self.hidden is not None:
            return self.hidden

        if not self.request:
            return False

        if self.all_perms and not all([self.request.user.has_perm(perm) for perm in self.all_perms]):
            return True
        if self.any_perms and not any([self.request.user.has_perm(perm) for perm in self.any_perms]):
            return True

    def get_children(self):
        for child in self.children:
            if not child.is_hidden():
                yield child

    def has_children(self):
        if not self.children:
            return False
        return any([not child.is_hidden() for child in self.children])

    def get_li_classes(self):
        classes = []
        if self.is_active():
            classes.append("active")
        if self.children:
            classes.append("treeview")
        return " ".join(classes)

    def get_icon(self):
        return self.icon if self.icon else ""

    def get_label(self):
        if self.label:
            return self.label
        elif self.children:
            return '<i class="fa fa-angle-left pull-right"></i>'
        else:
            return ""

    def get_name(self):
        return '<span>%s</span>' % self.name

    def to_html(self):
        if self.is_header:
            return '<li class="header">%s</li>' % self.name

        if self.has_children():
            children_html = "".join([
                '<ul class="treeview-menu">',
                ''.join(child.to_html() for child in self.children if not child.is_hidden()),
                '</ul>',
            ])
        else:
            children_html = ''

        return ''.join([
            '<li class="%s">' % self.get_li_classes(),
            '<a href="%s">%s%s%s</a>' % (self.href, self.get_icon(), self.get_name(), self.get_label()),
            children_html,
            '</li>',
        ])

class SimpleSidebarMenuItem(SidebarMenuItem):
    def __init__(self, icon=None, icon_color=None, label=None, **kwargs):
        super(SimpleSidebarMenuItem, self).__init__(**kwargs)
        self.icon = FAIcon(icon, color=icon_color)
        self.label = Label(label.get("data"), type=label.get("type"), classes=["pull-right"]) if label else None

class SidebarSearchForm(SidebarItem):
    action = '#'
    method = 'get'
    name = 'q'
    placeholder = 'Search...'

    def to_html(self):
        return ''.join([
            '<form action="%s" method="%s" class="sidebar-form">' % (self.action, self.method),
            '<div class="input-group">',
            '<input type="text" name="%s" class="form-control" placeholder="%s"/>' % (self.name, self.placeholder),
            '<span class="input-group-btn">',
            '<button type="submit" name="search" id="search-btn" class="btn btn-flat">%s</button>' % FAIcon('search'),
            '</span>',
            '</div>',
            '</form>',
        ])

class SidebarSearchMenuForm(SidebarItem):
    placeholder = 'Search Menu...'

    def to_html(self):
        html = ''.join([
            '<div class="sidebar-form">',
            '<div class="input-group">',
            '<input type="text" id="search-menu-text" class="form-control" placeholder="%s" onKeyUp="search_menu_items()"/>' \
                    % (self.placeholder),
            '<span class="input-group-btn">',
            '<button class="btn btn-flat" id="search-menu-button">%s</button>' % FAIcon('search'),
            '</span>',
            '</div>',
            '</div>',
        ])
        js_template = loader.get_template('AdminLTE/widgets/sidebar/search_menu_items.js')
        js = js_template.render()
        return html + str(js)

class Sidebar(object):
    request = None
    widgets_before_menu = None
    menu_items = None
    widgets_after_menu = None

    def __init__(self, request=None, widgets_before=None, menu_items=None, widgets_after=None):
        self.widgets_before_menu = []
        self.menu_items = []
        self.widgets_after_menu = []

        if widgets_before:
            self.add_items('widgets_before', *widgets_before)

        if menu_items:
            self.add_items('menu_items', *menu_items)

        if widgets_after:
            self.add_items('widgets_after', *widgets_after)

        if request:
            self.set_request(request)

    def add_items(self, type, *items):
        if type == 'widgets_before':
            container = self.widgets_before_menu
        elif type == 'widgets_after':
            container = self.widgets_after_menu
        elif type == 'menu_items':
            container = self.menu_items
        else:
            return

        container.extend(items)

    def add_menu_item(self, item):
        self.add_items('menu_items', item)

    def add_widget_before_menu(self, widget):
        self.add_items('widgets_before', widget)

    def add_widget_after_menu(self, widget):
        self.add_items('widgets_after', widget)

    def set_request(self, request):
        self.request = request

        for widget in self.widgets_before_menu:
            widget.set_request(request)

        for item in self.menu_items:
            item.set_request(request)

        for widget in self.widgets_after_menu:
            widget.set_request(request)

    def to_html(self):
        return ''.join([
            '<section class="sidebar">',

            ''.join(widget.to_html() for widget in self.widgets_before_menu if not widget.is_hidden()),

            '<ul class="sidebar-menu">',
            ''.join(item.to_html() for item in self.menu_items if not item.is_hidden()),
            '</ul>',

            ''.join(widget.to_html() for widget in self.widgets_after_menu if not widget.is_hidden()),

            '</section>',
        ])
