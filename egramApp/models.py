
from django.db import models
from django.conf import settings
from datetime import date, datetime
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.db import models
from django.db import migrations
from datetime import date
from django.utils import timezone
from django.utils.timezone import now

class Aadhar(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    aadhar=models.BigIntegerField()


class Birth(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    DOB=models.DateField()
    name=models.CharField(max_length=30)
    gen=models.CharField(max_length=30)
    f_name=models.CharField(max_length=30)
    m_name=models.CharField(max_length=30)
    dis_name=models.CharField(max_length=30)
    place_of_bir=models.CharField(max_length=30)
    bp_address=models.CharField(max_length=30)
    c_address=models.CharField(max_length=30)
    p_address=models.CharField(max_length=30)
    email=models.EmailField()
    num=models.IntegerField()
    m_edu=models.CharField(max_length=30)
    m_occ=models.CharField(max_length=30)
    f_edu=models.CharField(max_length=30)
    f_occ=models.CharField(max_length=30)
    m_age_mar=models.IntegerField()
    m_age_del=models.IntegerField()
    date=models.DateField()
    appli_name=models.CharField(max_length=30)

class Death(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    applicant_name=models.CharField(max_length=30)
    applicant_relation=models.CharField(max_length=30)
    mobile=models.IntegerField()
    date_of_death=models.DateField()
    deceased_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    deceased_fname=models.CharField(max_length=30)
    deceased_mname=models.CharField(max_length=30)
    religion=models.CharField(max_length=30)
    death_age=models.IntegerField()
    cause_of_death=models.CharField(max_length=100)
    deceased_address=models.CharField(max_length=50)
    date_of_issue=models.DateTimeField(default=datetime.now())
    
class Contacts(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    c_name=models.CharField(max_length=30)
    c_mail=models.EmailField()
    c_mssg=models.CharField(max_length=200)
    
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    compl_type = models.CharField(max_length=255)
    compl_loc = models.CharField(max_length=255)  # Ensure this field exists
    desc = models.TextField()  # Ensure this field exists
    document = models.FileField(upload_to='documents/')  # Ensure this field exists
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class UserModel(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.username


class Transaction(models.Model):
    user_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    last_date = models.DateField()
    transaction_image = models.ImageField(upload_to='qr_codes/', null=True, blank=True)
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)
    upload_date = models.DateField(default=timezone.now)  

    def __str__(self):
        return f"{self.user_name} - {self.amount}"
    
class HomeTax(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')])
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.status}"
    
    


class TransactionScreenshot(models.Model):
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='screenshots')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Screenshot for Transaction {self.transaction.id} by {self.uploaded_by.username}"
    


class TaxTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tax_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tax_type} - {self.status}"
    
class BirthCertificate(models.Model):
    image = models.ImageField(upload_to='certificates/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certificate {self.id}"
    
class PanchayatMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    image = models.ImageField(upload_to='panchayat_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class VillagePopulation(models.Model):
    total_population = models.IntegerField()
    male_population = models.IntegerField()
    female_population = models.IntegerField()

    def __str__(self):
        return f"Total: {self.total_population}"
    


