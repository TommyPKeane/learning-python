"""GitHub's GraphQL Base Object
"""

class Node:
    """GitHub's Base Class for GraphQL Objects

    References:
    - https://docs.github.com/en/graphql/reference/interfaces#node
    """
    id: str = None

    def __init__(self, id: str = None) -> None:
        self.id = id
        return None
