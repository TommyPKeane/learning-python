"""Unit-Testing for the graphql_queries.github.security Module
"""
import logging

import pytest

from graphql_queries.github.security import *  # TODO (tommypkeane): Update to explicit imports


module_log = logging.getLogger(__name__)


def test_AriadneSecurityAdvisoryClassification() -> None:
    assert AriadneSecurityAdvisoryClassification.field("GENERAL") is not None
    assert AriadneSecurityAdvisoryClassification.field("MALWARE") is not None
    return None
