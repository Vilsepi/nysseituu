
sites_to_check = [
    {
        "name": "Lissu Monitor",
        "url": "http://lissu.tampere.fi/monitor.php?stop=0014",
        "acceptable_statuses": [200],
        "mandatory_strings": [
            "table2"
        ]
    },
    {
        "name": "Siri API",
        "url": "https://siri.ij2010.tampere.fi/ws",
        "acceptable_statuses": [401],
        "mandatory_strings": [
            "Full authentication is required to access this resource",
            "Apache Tomcat"
        ]
    }
    # TODO Next time when api is down, check below url:
    # http://lissu.tampere.fi/ajax_servers/busLocations.php
]
