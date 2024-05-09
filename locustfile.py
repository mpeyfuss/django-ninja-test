from locust import HttpUser, task


class TestAsync(HttpUser):
    @task
    def post_new(self):
        self.client.post(
            "/async/new",
            json={
                "text": "hello!",
                "eth_address": "0xF4DB918906946B53C8db2292239aC1c8B94145f6",
                "large_int": 100,
            },
        )


# class TestSync(HttpUser):
#     @task
#     def post_new(self):
#         self.client.post(
#             "/sync/new",
#             json={
#                 "text": "hello!",
#                 "eth_address": "0xF4DB918906946B53C8db2292239aC1c8B94145f6",
#                 "large_int": 100,
#             },
#         )
