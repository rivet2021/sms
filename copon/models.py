from django.db import models


# Create your models here.

class coupons(models.Model):
      ID=models.CharField(max_length=100)
      code=models.CharField(max_length=100)
      url=models.URLField(max_length=100)
      subaccount=models.CharField(max_length=100)
      title=models.CharField(max_length=100)
      subtitle=models.CharField(max_length=100)

      def __str__(self):
        return self.url


