ICONS = {
    "home": (
        '<svg viewBox="0 0 24 24"><path d="M3 11.5 12 4l9 7.5"/>'
        '<path d="M5.5 10.5V20h13v-9.5"/><path d="M9.5 20v-6h5v6"/></svg>'
    ),
    "grid": (
        '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="6" height="6" rx="1"/>'
        '<rect x="14" y="4" width="6" height="6" rx="1"/>'
        '<rect x="4" y="14" width="6" height="6" rx="1"/>'
        '<rect x="14" y="14" width="6" height="6" rx="1"/></svg>'
    ),
    "book": (
        '<svg viewBox="0 0 24 24"><path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 0-3 3Z"/>'
        '<path d="M5 4v16"/><path d="M9 8h6"/><path d="M9 12h6"/></svg>'
    ),
    "user": (
        '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.2"/>'
        '<path d="M5 20c1.4-4.2 4-6.2 7-6.2s5.6 2 7 6.2"/></svg>'
    ),
    "greenhouse": (
        '<svg viewBox="0 0 64 64"><path d="M8 29 32 10l24 19"/>'
        '<path d="M14 28v26h36V28"/><path d="M32 10v44"/>'
        '<path d="M21 23v31"/><path d="M43 23v31"/><path d="M14 39h36"/>'
        '<path d="M25 54c.5-7.6 4.2-13 7-13s6.5 5.4 7 13"/>'
        '<path d="M32 46c-3.7-4.7-9.3-3.8-12.3-1.9 2.1 4.8 7.5 6.4 12.3 1.9Z"/>'
        '<path d="M32 46c3.7-4.7 9.3-3.8 12.3-1.9-2.1 4.8-7.5 6.4-12.3 1.9Z"/></svg>'
    ),
    "bolt": '<svg viewBox="0 0 24 24"><path d="m13 2-8 12h6l-1 8 8-12h-6Z"/></svg>',
    "droplet": (
        '<svg viewBox="0 0 24 24"><path d="M12 3.5c3.8 4.2 6.2 7.7 6.2 10.6a6.2 6.2 0 0 1-12.4 0C5.8 11.2 8.2 7.7 12 3.5Z"/>'
        '<path d="M9.2 15.4c.6 1.2 1.6 1.8 2.8 1.8"/></svg>'
    ),
    "arrow-right": '<svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>',
    "book-open": (
        '<svg viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11v17H6.5A2.5 2.5 0 0 0 4 22Z"/>'
        '<path d="M20 5.5A2.5 2.5 0 0 0 17.5 3H13v17h4.5A2.5 2.5 0 0 1 20 22Z"/></svg>'
    ),
}


def icon(name: str) -> str:
    return ICONS.get(name, "")
