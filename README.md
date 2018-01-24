MultiJSON
=========

A modular extension to Python's JSONEncoder that allows UUID, date/datetime and
Decimal objects to be serialised as JSON.

UUIDs are serialised as hyphen-separated hex representations by calling `str()`.

Dates and Datetimes are serialised in ISO8601 format using `strftime`.

Decimals are serialised using their string representation with `str()`

Contributing
------------
Contributions welcome.
