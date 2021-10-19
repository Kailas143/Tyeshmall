from django.db import models


# Create your models here.
class store(models.Model) :
    tenant_id=models.PositiveIntegerField()
    store_name=models.CharField(max_length=50)
    product=models.PositiveIntegerField()
    quantity=models.FloatField()

    def __str__(self):
        return str(self.id)



class location(models.Model) :
    tenant_id=models.PositiveIntegerField()
    address=models.CharField(max_length=2054)
    store_id=models.ForeignKey(store,on_delete=models.CASCADE)
    qty_in_lct=models.FloatField()

    def __str__(self):
        return str(self.id)
    