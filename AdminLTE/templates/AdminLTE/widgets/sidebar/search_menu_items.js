<script>
function _search_menu_items(q, items, force_show) {
    // if one item matched the keywork, all children will show, too
    // if one item matched, it's parent will show, too
    //
    // force_show: if true, means it's parent is shown, thus all items should be shown
    //             if not specified, treat as false
    q = typeof q == 'undefined' ? '' : q;
    force_show = typeof force_show == 'undefined' ? false : force_show;
    var ret = false;
    for (var i=0; i<items.length; i++) {
        var item = items[i], show_me = false;
        if (force_show || q == '' || item.innerText.toLowerCase().match(q)) {
            show_me = true;
        }
        var show_children = _search_menu_items(q, $(item).find('ul > li'), show_me);
        if (show_me || show_children) {
            $(item).show();
            ret = true;
        } else {
            $(item).hide();
        }
    }
    return ret;
}
function search_menu_items() {
    return _search_menu_items($('#search-menu-text')[0].value.toLowerCase(), $('.sidebar-menu > li'));
}
</script>
