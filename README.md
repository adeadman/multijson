MultiJSON
=========

A modular extension to Python's JSONEncoder that allows UUID and date/datetime
objects to be serialised as JSON.

UUIDs are serialised as hyphen-separated hex representations by calling `str()`.

Dates and Datetimes are serialised in ISO8601 format using `strftime`.

Contributing
------------
Contributions welcome.
