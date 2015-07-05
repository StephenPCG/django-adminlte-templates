<script>
function _search_menu_items(q, items) {
    for (var i=0; i<items.length; i++) {
        var item = items[i];
        var show = _search_menu_items(q, $(item).find('ul > li'));
        var ret = false;
        if (show || typeof q == 'undefined' || q == '' || item.innerText.toLowerCase().match(q)) {
            $(item).show();
            ret = true;
        } else {
            $(item).hide();
            ret = false;
        }
    }
    return ret;
}
function search_menu_items() {
    return _search_menu_items($('#search-menu-text')[0].value.toLowerCase(), $('.sidebar-menu > li'));
}
</script>
