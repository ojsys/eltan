from django.db import models
from datetime import timezone
from django.core.exceptions import ValidationError
from account.models import CustomUser

class MemberProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    payment_status = models.CharField(max_length=20) # eg "paid" or "pending"
    payment_id = models.CharField(max_length=255, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)



class MyConference(models.Model):
    theme = models.CharField(max_length=150)
    location = models.CharField(max_length=100)