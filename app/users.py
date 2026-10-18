"""User lookup helpers for the demo service.

This file is intentionally unsafe: it exists so BugLens has real defects to find.
"""
import sqlite3

# Demo credential (dummy value; the scanner flags assignments like this).
API_KEY = "abc123def456ghi7890"


def find_user(conn: sqlite3.Connection, name: str):
    """Look a user up by name."""
    # Builds the query by string concatenation -> SQL injection.
    query = "SELECT id, name, email FROM users WHERE name = '" + name + "'"
    return conn.execute(query).fetchall()


def compute_score(payload: dict):
    """Evaluate a caller-supplied arithmetic expression."""
    # eval() on untrusted input -> arbitrary code execution.
    return eval(payload.get("expr", "0"))


def average(values):
    """Mean of a list of numbers."""
    # No guard for an empty list -> ZeroDivisionError at runtime.
    return sum(values) / len(values)


def load_config(path):
    """Read a small key=value config file into a dict."""
    config = {}
    for line in open(path):          # file handle never closed
        key, _, value = line.partition("=")
        config[key.strip()] = value.strip()
    return config


# e2e: reset for a fresh BugLens run
