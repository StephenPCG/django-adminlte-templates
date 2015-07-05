# -*- coding: utf-8 -*-

from AdminLTE.widgets.sidebar import SimpleSidebarMenuItem as Item
from AdminLTE.widgets.sidebar import Sidebar, SidebarMenuItem, SidebarSearchForm, SidebarSearchMenuForm
from AdminLTE.settings import Settings

menu_items = [
    Item(name='Documentation', is_header=True),
    Item(name='Installation', icon='download'),
    Item(name='Configuration', icon='gears', children=[
            Item(name='Sidebar', icon='list'),
            Item(name='Template Options', icon='file-o'),
        ]),
    Item(name='Examples', is_header=True),
    Item(name='Dashboard', icon='dashboard', children=[
            Item(name='Dashboard v1', icon='circle-o', active=True),
            Item(name='Dashboard v2', icon='circle-o'),
        ]),
    Item(name='Layout Options', icon='files-o', label={"type":"primary", "data":4}),
    Item(name='Widgets', icon='th', label={"type":"success", "data":"hot"}),
    Item(name='Charts', icon='pie-chart', children=[
            Item(name='ChartJS', icon='circle-o'),
            Item(name='Morris', icon='circle-o'),
            Item(name='Flot', icon='circle-o'),
            Item(name='Inline charts', icon='circle-o'),
        ]),
    Item(name='UI Elements', icon='laptop', children=[
            Item(name='General', icon='circle-o'),
            Item(name='Icons', icon='circle-o'),
            Item(name='Buttons', icon='circle-o'),
            Item(name='Sliders', icon='circle-o'),
            Item(name='Timeline', icon='circle-o'),
            Item(name='Models', icon='circle-o'),
        ]),
    Item(name='Forms', icon='edit', children=[
            Item(name='General Elements', icon='circle-o'),
            Item(name='Advanced Elements', icon='circle-o'),
            Item(name='Editors', icon='circle-o'),
        ]),
    Item(name='Tables', icon='table', children=[
            Item(name='Simple Tables', icon='circle-o'),
            Item(name='Data Tables', icon='circle-o'),
        ]),
    Item(name='Calendar', icon='calendar', label={"type":"danger", "data":3}),
    Item(name='Mailbox', icon='calendar', label={"type":"warning", "data":12}),
    Item(name='Examples', icon='folder', children=[
            Item(name='Invoice', icon='circle-o'),
            Item(name='Login', icon='circle-o'),
            Item(name='Register', icon='circle-o'),
            Item(name='Lockscreen', icon='circle-o'),
            Item(name='404 Error', icon='circle-o'),
            Item(name='500 Error', icon='circle-o'),
            Item(name='Blank Page', icon='circle-o'),
        ]),
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
    Item(name='Labels',is_header=True),
    Item(name='Important', icon='circle-o', icon_color='red'),
    Item(name='Warning', icon='circle-o', icon_color='yellow'),
    Item(name='Information', icon='circle-o', icon_color='aqua'),
    Item(name='中文菜单项',icon='language'),
    Item(name='Hidden Menu Item', hidden=True),
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

Settings.load({
    'SIDEBAR_GENERATOR': generate_sidebar,
    'LOGIN': {
        'LOGO': r'<b>Example</b> Site',
    },
    'REGISTER': {
        'LOGO': r'<b>Example</b> Site',
    },
})
