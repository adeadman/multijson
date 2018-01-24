import json
import uuid
import datetime
import pytest
from decimal import Decimal
from multijson import MultiJSONEncoder


class Custom:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class TestMultiJSONEncoder:

    def test_dump_uuid(self):
        test_input = {
            "id": uuid.uuid4(),
        }

        output = json.dumps(test_input, cls=MultiJSONEncoder)
        result = json.loads(output)

        assert "id" in result
        assert result["id"] == str(test_input["id"])

    def test_dump_date(self):
        test_input = {
            "date": datetime.date(2017, 7, 1),
        }

        output = json.dumps(test_input, cls=MultiJSONEncoder)
        result = json.loads(output)

        assert "date" in result
        assert result["date"] == "2017-07-01"

    def test_dump_datetime(self):
        test_input = {
            "time": datetime.datetime(2017, 7, 1, 23, 11, 11),
        }

        output = json.dumps(test_input, cls=MultiJSONEncoder)
        result = json.loads(output)

        assert "time" in result
        assert result["time"] == "2017-07-01T23:11:11Z"

    def test_dump_decimal(self):
        test_input = {
            "a": Decimal('3.9'),
            "b": Decimal('0.0003'),
            "c": Decimal('1200000.0000021'),
        }

        output = json.dumps(test_input, cls=MultiJSONEncoder)
        assert output == '{"a": 3.9, "b": 0.0003, "c": 1200000.0000021}'

    def test_dump_custom_object(self):
        test_input = {
            "custom": Custom("Rincewind", 120),
        }

        with pytest.raises(TypeError):
            json.dumps(test_input, cls=MultiJSONEncoder)
