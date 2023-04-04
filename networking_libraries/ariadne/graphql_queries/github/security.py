"""Utilities for GraphQL Queries to GitHub's Security-related Information

References:
- https://docs.github.com/en/graphql/reference/queries#securityadvisories
-
"""
import datetime
import enum

from graphql_queries.query import GraphQLQuery
from graphql_queries.github.node import Node


class SecurityAdvisoryClassification(str, enum.Enum):
    """
    References:
    - https://docs.github.com/en/graphql/reference/enums#securityadvisoryclassification
    """
    GENERAL: str = "GENERAL"
    MALWARE: str = "MALWARE"


class SecurityAdvisoryEcosystem(str, enum.Enum):
    """
    References:
    - https://docs.github.com/en/graphql/reference/enums#securityadvisoryecosystem
    """
    ACTIONS: str = "ACTIONS"
    COMPOSER: str = "COMPOSER"
    ERLANG: str = "ERLANG"
    GO: str = "GO"
    MAVEN: str = "MAVEN"
    NPM: str = "NPM"
    NUGET: str = "NUGET"
    PIP: str = "PIP"
    PUB: str = "PUB"
    RUBYGEMS: str = "RUBYGEMS"
    RUST: str = "RUST"


class SecurityAdvisoryIdentifierType(str, enum.Enum):
    """
    References:
    - https://docs.github.com/en/graphql/reference/enums#securityadvisoryidentifiertype
    """
    CVE: str = "CVE"
    GHSA: str = "GHSA"


class SecurityAdvisoryOrderField(str, enum.Enum):
    """
    References:
    - https://docs.github.com/en/graphql/reference/enums#securityadvisoryorderfield
    """
    PUBLISHED_AT: str = "PUBLISHED_AT"
    UPDATED_AT: str = "UPDATED_AT"


class SecurityAdvisorySeverity(str, enum.Enum):
    """
    References:
    - https://docs.github.com/en/graphql/reference/enums#securityadvisoryseverity
    """
    CRITICAL: str = "CRITICAL"
    HIGH: str = "HIGH"
    MODERATE: str = "MODERATE"
    LOW: str = "LOW"


class SecurityVulnerabilityOrderField(str, enum.Enum):
    """
    References:
    - https://docs.github.com/en/graphql/reference/enums#securityvulnerabilityorderfield
    """
    UPDATED_AT: str = "UPDATED_AT"


class GitHubSecurityAdvisory(Node):
    classification: object = None
    cvss: object = None
    cwes: object = None
    databaseId: object = None
    description: object = None
    ghsaId: object = None
    identifiers: object = None
    notificationsPermalink: object = None
    origin: object = None
    permalink: object = None
    publishedAt: object = None
    references: object = None
    severity: object = None
    summary: object = None
    updatedAt: object = None
    vulnerabilities: object = None
    withdrawnAt: object = None

    def __init__(self) -> None:
        return None


class QueryGitHubSecurityAdvisories(GraphQLQuery):
    """
    """
    after: str = None
    before: str = None
    classifications: list[SecurityAdvisoryClassification]: None
    first: int = None
    identifier: str = None
    last: int = None
    orderBy: str = None
    publishedSince: datetime.datetime = None
    updatedSince: datetime.datetime = None

    def __init__(
        self,
        after: str = None,
        before: str = None,
        classifications: list: None,
        first: int = None,
        identifier: str = None,
        last: int = None,
        orderBy: str = None,
        publishedSince: datetime.datetime = None,
        updatedSince: datetime.datetime = None,
    ) -> None:
        self.after = after
        self.before = before
        self.classifications = classifications
        self.first = first
        self.identifier = identifier
        self.last = last
        self.orderBy = orderBy
        self.publishedSince = publishedSince
        self.updatedSince = updatedSince
        return None
