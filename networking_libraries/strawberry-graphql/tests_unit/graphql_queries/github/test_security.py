"""Unit-Testing for the graphql_queries.github.security Module
"""
import logging

import pytest

from graphql_queries.github.security import *  # TODO (tommypkeane): Update to explicit imports


module_log = logging.getLogger(__name__)


def test_SecurityAdvisoryClassification() -> None:
    module_log.info(SecurityAdvisoryClassification.__dict__)
    return None
