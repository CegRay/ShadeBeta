from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities import Customer as CustomerEntity


class Customer(TimedBaseModel):
    phone = models.CharField(
        verbose_name="Phone number",
        max_length=20,
        unique=True,
    )

    token = models.CharField(
        verbose_name="User auth token",
        max_length=255,
        default=uuid4,
        unique=True,
    )

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            id=self.pk,
            phone=self.phone,
            created_at=self.created_at,
        )

    def __str__(self) -> str:
        return self.phone

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
