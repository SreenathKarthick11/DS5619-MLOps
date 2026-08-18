"""
A minimal, from-scratch expectations framework in the spirit of Great
Expectations / data contracts (this week's lecture). You are implementing
the checking logic yourself rather than importing a library — the goal is
to understand what these tools actually do under the hood.

Fill in the four functions marked # TODO. Do not change the Violation
dataclass or any function signature.
"""
from dataclasses import dataclass


@dataclass
class Violation:
    expectation: str      # name of the check, e.g. "expect_column_not_null"
    column: str            # which column it was checking
    row_index: int          # index into the rows list where it failed
    detail: str              # short human-readable reason


def _is_null(value):
    return value is None or (isinstance(value, str) and value.strip() == "")


def expect_column_not_null(rows, column):
    """Return a Violation for every row where rows[i][column] is null/empty."""
    vio_objs=[]
    for i in range(len(rows)):
        if _is_null(rows[i][column]):
            vio_objs.append(Violation("expect_column_not_null",str(column),i,f"The value present needs to be not null, at {i}th row and {column}th column"))

    return vio_objs

def try_cast_float(val):
    try:
        float(val)
        return True
    except (ValueError, TypeError):
        return False

def expect_column_positive(rows, column):
    """Return a Violation for every row where rows[i][column], cast to float,
    is not strictly greater than 0. If the value can't be cast to float at
    all, that also counts as a violation (detail should say so).
    """
    vio_objs=[]
    for i in range(len(rows)):
        if (not try_cast_float(rows[i][column])):
            vio_objs.append(Violation("expect_column_positive",str(column),i,f"The value present needs to be casted to float, at {i}th row and {column}th column"))
        elif (float(rows[i][column]) <= 0):
            vio_objs.append(Violation("expect_column_positive",str(column),i,f"The value present needs to be strictly positive, at {i}th row and {column}th column"))

    return vio_objs


def expect_column_in_set(rows, column, allowed_values):
    """Return a Violation for every row where rows[i][column] is not a member
    of allowed_values (a set or list you're given).
    """
    vio_objs=[]
    for i in range(len(rows)):
        if (rows[i][column] not in allowed_values):
            vio_objs.append(Violation("expect_column_in_set",str(column),i,f"The value present needs to be present in allowed set of values , at {i}th row and {column}th column"))

    return vio_objs

def expect_column_unique(rows, column):
    """Return a Violation for every row AFTER THE FIRST that repeats a value
    already seen in `column`. (i.e. if three rows share a value, rows 2 and 3
    are violations; row 1 is not.)
    """
    vio_objs=[]
    seen = set()
    for i in range(len(rows)):
        if (rows[i][column] in seen):
            vio_objs.append(Violation("expect_column_unique",str(column),i,f"The value present needs to be unique, at {i}th row and {column}th column"))
        else:
            seen.add(rows[i][column])

    return vio_objs
