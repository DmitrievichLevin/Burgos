"""Pytest config."""

from typing import Any

import pytest

from burgos.fields import fields
from burgos.fields.interface import Field
from burgos.messages.message import Message
from burgos.serializers import serializers
from burgos.serializers.interface import MessageSerializer
from burgos.utils import modulesubclasses


@pytest.fixture(scope="session")
def field_classes() -> Any:
    """All Field Subclasses."""
    return modulesubclasses(fields, Field)


@pytest.fixture(scope="session")
def serializer_classes() -> Any:
    """All Field Subclasses."""
    return modulesubclasses(serializers, MessageSerializer)


class TestMessage(Message):
    """Test Message Subclass."""

    required = True
    BoolField = fields.BoolField()
    FloatField = fields.FloatField()
    IntField = fields.IntField()
    ListField = fields.ListField(
        fields.BoolField(),
        fields.FloatField(),
        fields.IntField(),
        fields.StringField(),
    )
    StringField = fields.StringField()


@pytest.fixture(scope="session")
def test_message_all_fields() -> type[TestMessage]:
    """Test Message Subclass.

    * contains all valid fields see fields.py
    * required=True(all field attributes are set to required).
    * Note: TypeField is not a valid field attribute(auto-added by base class).
    """
    return TestMessage


@pytest.fixture(scope="session")
def valid_dictionary_test_message_dict() -> dict:
    """Valid Test Message Dict.

    * Value representing every Field Subclass defined in fields.py
    * [classname]: valid_value
    """
    test_dict = {
        "IntField": 144,
        "BoolField": False,
        # List Values in alpha order(same as field_classes fixture)
        # [BoolField, FloatField, IntField, StringField, TypeField...]
        "ListField": [True, 3.14, 144, "Hello World"],
        "FloatField": 3.14,
        "StringField": "Hello World",
        "type": "TestMessage",
    }

    return test_dict


@pytest.fixture(scope="session")
def invalid_dictionary_test_message_dict() -> dict:
    """Invalid Test Message Dict.

    * Value representing every Field Subclass defined in fields.py
    * [classname]: invalid_value
    """
    test_dict = {
        "IntField": 3.14,
        "BoolField": "Hello World",
        # List Values in alpha ordersame as field_classes fixture
        # [BoolField, FloatField, IntField, StringField, TypeField...]
        "ListField": True,
        "FloatField": 144,
        "StringField": [],
        "type": 144,
    }

    return test_dict


@pytest.fixture(scope="session")
def valid_bytes_message() -> bytes:
    """Valid Bytes for TestMessage."""
    right_bytes = b"\x97\x88\x0bTestMessage\x1f\x98\x00\x89@\t\x1e\xb8Q\xeb\x85\x1f\x88\x90\x01\x8a\x88\x1c\x98\x01\x89@\t\x1e\xb8Q\xeb\x85\x1f\x88\x90\x01\x92\x88\x0bHello World\x92\x88\x0bHello World"  # noqa: B950
    return right_bytes


@pytest.fixture(scope="session")
def invalid_bytes_message() -> bytes:
    """Invalid Bytes for TestMessage."""
    wrong_bytes = b"\x97\x88\x0cWrongMessage\x1f\x98\x00\x89@\t\x1e\xb8Q\xeb\x85\x1f\x88\x90\x01\x8a\x88\x1c\x98\x01\x89@\t\x1e\xb8Q\xeb\x85\x1f\x88\x90\x01\x92\x88\x0bHello World\x92\x88\x0bHello World"  # noqa: B950
    return wrong_bytes
