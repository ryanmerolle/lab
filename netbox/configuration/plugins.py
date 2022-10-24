# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

PLUGINS = [
    "netbox_acls",
    "netbox_bgp",
    # "netbox_config_backup",
    "netbox_devicetype_importer",
    "netbox_initializers",
    "netbox_inventory",
    "netbox_lists",
    "netbox_prometheus_sd",
    # "netbox_static_routes",
    "netbox_topology_views",
    # "netbox_vrf_context",
]

PLUGINS_CONFIG = {
    "netbox_acls": {},
    "netbox_bgp": {},
    # "netbox_config_backup": {},
    "netbox_devicetype_importer": {
        "github_token": "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"
    },
    "netbox_initializers": {},
    "netbox_inventory": {},
    "netbox_lists": {},
    "netbox_prometheus_sd": {},
    # "netbox_static_routes": {},
    "netbox_topology_views": {},
    # "netbox_vrf_context": {},
}
