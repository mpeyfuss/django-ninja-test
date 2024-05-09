from asyncio import sleep
from django.http import HttpRequest
from ninja import Router

from async_test.models import MyModel
from async_test.schema import MySchema, MySchemaDetails


router = Router()


@router.post("/new", response=MySchemaDetails)
async def create(request: HttpRequest, my_schema: MySchema):
    obj = await MyModel.objects.acreate(**dict(my_schema))
    await sleep(0.05)
    return obj
