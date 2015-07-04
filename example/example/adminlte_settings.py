# -*- coding: utf-8 -*-

from AdminLTE.navigation_tree import NavTree as tree

navtree = [
    tree(name='Main Navigation', is_header=True),
    tree(name='Dashboard', icon='dashboard', children=[
            tree(name='Dashboard v1', icon='circle-o'),
            tree(name='Dashboard v2', icon='circle-o'),
        ]),
    tree(name='Layout Options', icon='files-o', label={"type":"primary", "data":4}),
    tree(name='Widgets', icon='th', label={"type":"success", "data":"hot"}),
    tree(name='Charts', icon='pie-chart'),
    tree(name='Multilevel', icon='share', children=[
            tree(name='Level One', icon="circle-o"),
            tree(name='Level One', icon="circle-o", children=[
                    tree(name='Level Two', icon="circle-o"),
                    tree(name='Level Two', icon="circle-o", children=[
                            tree(name='Level Three', icon='circle-o'),
                            tree(name='Level Three', icon='circle-o'),
                        ]),
                ]),
            tree(name='Level One', icon="circle-o"),
        ]),
    tree(name='Labels',is_header=True),
    tree(name='Important', icon='circle-o', icon_color='red'),
    tree(name='Warning', icon='circle-o', icon_color='yellow'),
    tree(name='Information', icon='circle-o', icon_color='aqua'),
]

ADMINLTE_SETTINGS = {
    'NAVTREE': navtree,
    'LOGIN': {
        'LOGO': r'<b>Example</b> Site',
    },
    'REGISTER': {
        'LOGO': r'<b>Example</b> Site',
    },
}
