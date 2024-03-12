from django.db import models
from datetime import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from account.models import CustomUser

class MemberProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

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



class Conference(models.Model):
    title = models.CharField(max_length=255)
    conf_date = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='conference_images/')

    def __str__(self):
        return self.title

class ConferenceRegistration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.conference.title + " - " + self.user.first_name + "  " + self.user.last_name
    
###############Defining SIGs Models#######################
class Sigs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='sig_images/')

    def __str__(self):
        return self.title

class SigsRegistration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sig = models.ForeignKey(Sigs, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)