from django.db import models
from datetime import timezone
from django.core.exceptions import ValidationError

class User(models.Model):
    pass

class MembershipType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Subscription(models.Model):
    def clean(self):
        active_subs = Subscription.objects.filter(
            user=self.user, 
            end_date__gte=timezone.now()
        ).exclude(id=self.id)
        
        if active_subs.exists():
            raise ValidationError("You already have an active subscription")
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    payment_status = models.CharField(max_length=20) # eg "paid" or "pending"
    payment_id = models.CharField(max_length=255, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    