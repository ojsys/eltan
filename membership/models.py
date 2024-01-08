from django.db import models

class User(models.Model):
    pass

class MembershipType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    payment_status = models.CharField(max_length=20) # eg "paid" or "pending"
    