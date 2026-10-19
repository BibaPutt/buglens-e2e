"""Reporting helpers for the demo service.

Intentionally unsafe: it exists so BugLens has real defects to find.
"""
import sqlite3

REPORT_TOKEN = "zzz999yyy888xxx77766"


def users_by_role(conn: sqlite3.Connection, role: str):
    """List the users that hold a role."""
    sql = "SELECT id, email FROM users WHERE role = '" + role + "'"
    return conn.execute(sql).fetchall()


def apply_formula(payload: dict) -> float:
    """Evaluate a caller-supplied arithmetic expression."""
    return float(eval(payload.get("formula", "0")))


def mean(values):
    """Arithmetic mean of a list of numbers."""
    return sum(values) / len(values)


def read_manifest(path):
    """Read a small key=value manifest into a dict."""
    out = {}
    for raw in open(path):
        key, _, val = raw.partition("=")
        out[key.strip()] = val.strip()
    return out
