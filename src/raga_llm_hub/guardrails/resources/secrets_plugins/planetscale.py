"""
This plugin searches for PlanetScale API tokens.
"""

import re

from detect_secrets.plugins.base import RegexBasedDetector


class PlanetScaleDetector(RegexBasedDetector):
    """Scans for PlanetScale API Tokens."""

    secret_type = "PlanetScale API Token"

    denylist = [
        # the PlanetScale API token
        re.compile(
            r"""(?i)\b(pscale_tkn_[a-z0-9=\-_\.]{32,64})(?:['|\"|\n|\r|\s|\x60|;]|$)"""
        ),
        # the PlanetScale OAuth token
        re.compile(
            r"""(?i)\b(pscale_oauth_[a-z0-9=\-_\.]{32,64})(?:['|\"|\n|\r|\s|\x60|;]|$)"""
        ),
        # the PlanetScale password
        re.compile(
            r"""(?i)\b(pscale_pw_[a-z0-9=\-_\.]{32,64})(?:['|\"|\n|\r|\s|\x60|;]|$)"""
        ),
    ]
