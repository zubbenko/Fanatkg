JAZZMIN_SETTINGS = {
    "site_title": "Fanat_kg",
    "site_header": "Fanat_kg",
    "site_brand": "Fanat_kg",
    "welcome_sign": "Welcome to Fanat_kg",
    "copyright": "Fanat_kg",
    "search_model": ["auth.User", "auth.Group", "main_app.Vacancy", "main_app.Service", "main_app.PriceListItem"],

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "Fanat_kg"},
        {"model": "auth.User"},
        {"name": "Support", "url": "https://t.me/elldiyar", "new_window": True},
    ],
    "show_sidebar": True,
    "default_icon_parents": "fas fa-circle",
    "default_icon_children": "fas fa-dot-circle",
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}









JAZZMIN_UI_TWEAKS = {
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "navbar_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-primary",
    },
}
