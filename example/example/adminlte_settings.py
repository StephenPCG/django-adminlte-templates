# -*- coding: utf-8 -*-

from AdminLTE.sidebar import SimpleSidebarMenuItem as Item
from AdminLTE.sidebar import Sidebar, SidebarMenuItem, SidebarSearchForm, SidebarSearchMenuForm

menu_items = [
    Item(name='Main Navigation', is_header=True),
    Item(name='Dashboard', icon='dashboard', children=[
            Item(name='Dashboard v1', icon='circle-o', active=True),
            Item(name='Dashboard v2', icon='circle-o'),
        ]),
    Item(name='Layout Options', icon='files-o', label={"type":"primary", "data":4}),
    Item(name='Widgets', icon='th', label={"type":"success", "data":"hot"}),
    Item(name='Charts', icon='pie-chart'),
    Item(name='Multilevel', icon='share', children=[
            Item(name='Level One', icon="circle-o"),
            Item(name='Level One', icon="circle-o", children=[
                    Item(name='Level Two', icon="circle-o"),
                    Item(name='Level Two', icon="circle-o", children=[
                            Item(name='Level Three', icon='circle-o'),
                            Item(name='Level Three', icon='circle-o'),
                        ]),
                ]),
            Item(name='Level One', icon="circle-o"),
        ]),
    Item(name='中文菜单项',icon='language'),
    Item(name='Labels',is_header=True),
    Item(name='Important', icon='circle-o', icon_color='red'),
    Item(name='Warning', icon='circle-o', icon_color='yellow'),
    Item(name='Information', icon='circle-o', icon_color='aqua'),
    Item(name='Hidden Item', hidden=True),
]

#search_form = SidebarSearchForm(action=".", method="get", name="query", placeholder="Search Menu...")
search_form = SidebarSearchMenuForm()

right_item = SidebarMenuItem(name='Right Items')
right_item.icon = '<i class="fa text-green">✔</i>'
wrong_item = SidebarMenuItem(name='Wrong Items')
wrong_item.icon = '<i class="fa text-red">✘</i>'

def generate_sidebar(request):
    sidebar = Sidebar(request, menu_items=menu_items)
    sidebar.add_widget_before_menu(search_form)
    sidebar.add_menu_item(right_item)
    sidebar.add_menu_item(wrong_item)
    return sidebar

ADMINLTE_SETTINGS = {
    'SIDEBAR_GENERATOR': generate_sidebar,
    'LOGIN': {
        'LOGO': r'<b>Example</b> Site',
    },
    'REGISTER': {
        'LOGO': r'<b>Example</b> Site',
    },
}
