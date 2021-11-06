from django.db import models


class AccountsCreated(models.Model):
    acc_id = models.CharField(max_length=50, blank=False)
    acc_email = models.EmailField(max_length=254)
    acc_pass = models.CharField(max_length=20, blank=False)
