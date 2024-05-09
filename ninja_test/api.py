from ninja import NinjaAPI, Schema
from async_test.router import router as async_router
from sync_test.router import router as sync_router

api = NinjaAPI()

api.add_router(prefix="async", router=async_router)
api.add_router(prefix="sync", router=sync_router)


class IndexResponse(Schema):
    message: str = "Hello World"


@api.get(path="/", response=IndexResponse)
async def index(request):
    return IndexResponse()
