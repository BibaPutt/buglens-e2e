"""Minimal demo service used as a BugLens end-to-end fixture."""


def health() -> dict:
    return {"status": "ok"}
