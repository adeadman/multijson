from datetime import date, datetime
from json import JSONEncoder
from uuid import UUID


class MultiJSONEncoder(JSONEncoder):
    """MultiJsonEncoder

    Extend the default JSONEncoder by adding support for UUID and DateTime
    """
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # Let the base class default raise the TypeError
        return JSONEncoder.default(self, obj)
