"""Reporting helpers for the demo service.

Intentionally unsafe: it exists so BugLens has real defects to find.
"""
import sqlite3

REPORT_TOKEN = "zzz999yyy888xxx77766"


def users_by_role(conn: sqlite3.Connection, role: str):
    """List the users that hold a role."""
    sql = "SELECT id, email FROM users WHERE role = ?"
    return conn.execute(sql, (role,)).fetchall()


def apply_formula(payload: dict) -> float:
    """Evaluate a caller-supplied arithmetic expression."""
    import ast

    expr = payload.get("formula", "0")
    node = ast.parse(expr, mode="eval")
    allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
               ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub)
    if not all(isinstance(n, allowed) for n in ast.walk(node)):
        raise ValueError("unsupported formula")
    return float(eval(compile(node, "<formula>", "eval")))


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
