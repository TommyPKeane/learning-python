"""GitHub's GraphQL Base Object
"""
import logging

import strawberry


module_log = logging.getLogger(__name__)


class Node:
    """GitHub's Base Class for GraphQL Objects

    References:
    - https://docs.github.com/en/graphql/reference/interfaces#node
    """
    id: str = None

    def __init__(self, id: str = None) -> None:
        self.id = id
        return None
