from time import sleep
from django.http import HttpRequest
from ninja import Router

from async_test.models import MyModel
from async_test.schema import MySchema, MySchemaDetails


router = Router()


@router.post("/new", response=MySchemaDetails)
def create(request: HttpRequest, my_schema: MySchema):
    obj = MyModel.objects.create(**dict(my_schema))
    sleep(0.05)
    return obj
