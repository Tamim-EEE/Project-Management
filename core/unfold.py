from django.urls import reverse_lazy
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _
UNFOLD = {
    "SITE_TITLE": ("Raktch Project Management Admin"),
    "SITE_HEADER": ("Raktch Project Management"),
    # "SITE_ICON": {
    #     "light": "/static/assets/logo/logo-light.png",  # light mode
    #     "dark": "/static/assets/logo/logo.webp",  # dark mode
    # },
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,  # show/hide "View on site" button, default: True
    # show/hide "Back" button on changeform in header, default: False
    "SHOW_BACK_BUTTON": True,
    "BORDER_RADIUS": "10px",

    "COLORS": {
        "base": {
            "50": "248, 250, 252",    # #F8FAFC
            "100": "241, 245, 249",   # #F1F5F9
            "200": "226, 232, 240",   # #E2E8F0
            "300": "203, 213, 225",   # #CBD5E1
            "400": "148, 163, 184",   # #94A3B8
            "500": "100, 116, 139",   # #64748B
            "600": "71, 85, 105",     # #475569
            "700": "51, 65, 85",      # #334155
            "800": "30, 41, 59",      # #1E293B
            "900": "15, 23, 42",      # #0F172A
            "950": "2, 6, 23",        # #020617
        },
        "primary": {
            "50": "245, 243, 255",    # #F5F3FF
            "100": "237, 233, 254",   # #EDE9FE
            "200": "221, 214, 254",   # #DDD6FE
            "300": "196, 181, 253",   # #C4B5FD
            "400": "167, 139, 250",   # #A78BFA
            "500": "139, 92, 246",    # #8B5CF6
            "600": "124, 58, 237",    # #7C3AED
            "700": "109, 40, 217",    # #6D28D9
            "800": "91, 33, 182",     # #5B21B6
            "900": "76, 29, 149",     # #4C1D95
            "950": "59, 7, 100",      # #3B0764
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
    },

    "COMMAND": {
        "search_models": True,
        "search_callback": "utils.search_callback",
        "show_history": True,
    },

}
