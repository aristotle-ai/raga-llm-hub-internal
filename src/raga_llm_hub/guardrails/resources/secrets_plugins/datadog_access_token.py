"""
This plugin searches for Datadog Access Tokens.
"""

import re

from detect_secrets.plugins.base import RegexBasedDetector


class DatadogAccessTokenDetector(RegexBasedDetector):
    """Scans for Datadog Access Tokens."""

    secret_type = "Datadog Access Token"

    denylist = [
        re.compile(
            r"""(?i)(?:datadog)(?:[0-9a-z\-_\t .]{0,20})(?:[\s|']|[\s|"]){0,3}(?:=|>|:{1,3}=|\|\|:|<=|=>|:|\?=)(?:'|\"|\s|=|\x60){0,5}([a-z0-9]{40})(?:['|\"|\n|\r|\s|\x60|;]|$)"""
        ),
    ]
