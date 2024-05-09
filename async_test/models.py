from django.db import models


class MyModel(models.Model):
    text = models.TextField()
    large_int = models.DecimalField(max_digits=100, decimal_places=0)
    eth_address = models.TextField()

    def save(self, *args, **kwargs):
        self.eth_address = self.eth_address.lower()
        super().save(*args, **kwargs)
