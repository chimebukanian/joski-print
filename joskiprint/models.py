from django.db import models
from django.utils import timezone
from django.db import models
# Create your models here.


# Create your models here.
class PrintOptions(models.Model):
    startPage=models.IntegerField(null=True,)
    endpage=models.IntegerField(null=True,)
    frontAndBack=models.BooleanField(null=True,)
    coloured=models.BooleanField(null=True, default=False)

    class Meta:
        ordering=['endpage']

    def __str__(self):
        return "Print Options"

class UserDetails(models.Model):
    email=models.EmailField(help_text="Email", null=True,)
    phoneNumber=models.CharField(help_text="phone number", max_length=15, null=True,)
    name=models.CharField(help_text="Name", max_length=30, null=True,)
    address=models.CharField(max_length=30, help_text="Address", null=True,)
    date_created=models.DateField(auto_now_add=True, null=True)
    class Meta:
        ordering=['name']

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    file=models.FileField(null=True, help_text='select the file to upload')
    fileurl=models.CharField(null=True, help_text='url of file', blank=True, max_length=30)
    pages=models.IntegerField(null=True, help_text="how many copies")
    printOptions=models.ForeignKey(PrintOptions, null=True, on_delete=models.CASCADE, help_text="print options")
    price=models.DecimalField(help_text="price of order", decimal_places=2, max_digits=100, null=True,)
    notes=models.CharField(max_length=200, help_text="notes", null=True,)
    userDetails=models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True,)
    order_date=models.DateTimeField('order date', null=True, auto_now_add=True)
    
    class Meta:
        ordering=['-price']

    Status=(
        (0, "pending"),
        (1, 'processing'),
        (2, 'ready'),
        (3, 'delivered'),
    )
    status=models.IntegerField(null=True, choices=Status, blank=True, default=0, help_text="Order status")

    def __str__(self):
        return self.userDetails.name


class Pricing(models.Model):
    name=models.CharField(max_length=30, null=True,)
    cost=models.DecimalField(max_digits=5, decimal_places=2, help_text='cost', null=True,)
    description=models.CharField(max_length=252, null=True,)
    code=models.CharField(max_length=20, null=True,)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name