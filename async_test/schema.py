from typing import Annotated
from ninja import ModelSchema
from pydantic import AfterValidator, AnyHttpUrl, Field, HttpUrl, field_validator
from async_test.models import MyModel

EthAddress = Annotated[
    str, Field(pattern=r"^0x[a-fA-F0-9]{40}$"), AfterValidator(lambda s: s.lower())
]


class MySchema(ModelSchema):
    eth_address: EthAddress

    class Meta:
        model = MyModel
        fields = ["text", "large_int", "eth_address"]


class MySchemaDetails(ModelSchema):
    class Meta:
        model = MyModel
        fields = "__all__"
