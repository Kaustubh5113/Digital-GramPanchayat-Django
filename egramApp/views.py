import datetime
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views import View
from egramApp.models import Aadhar
from egramApp.models import Birth
from egramApp.models import Death
from egramApp.models import Complaint
from egramApp.models import Contacts
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import UserModel
from .models import Transaction
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
import logging
from datetime import datetime 
from .models import HomeTax
from .forms import ScreenshotUploadForm
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os
import json
from .models import TransactionScreenshot
from .models import TaxTransaction
from .models import PanchayatMember
import openai
from .models import VillagePopulation

def Aadhar_val(request):
    if request.method=='POST':
        adh=request.POST.get('aadhar')
        try:
            ad=Aadhar.objects.get(aadhar=adh)
            return redirect('signin')
        except Aadhar.DoesNotExist:
            return HttpResponse("not matched!!! ")
        return JsonResponse(response_data)    
    return render(request,'aadhar.html')
def Home(request):
    return render(request,'home.html')

@login_required(login_url='signin')

def Logout(request):
    logout(request)
    return redirect('signin')

def Contact(request):
    if request.method=='POST':
        contact_name=request.POST.get('cont_name')
        contact_email=request.POST.get('cont_email')
        contact_message=request.POST.get('cont_message')
        contact_data=Contacts(user=request.user,c_name=contact_name,c_mail=contact_email,c_mssg=contact_message)
        contact_data.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    return render(request,'contact.html')

def Profile(request):
    return render(request,'profile.html')

def About(request):
    return render(request,'about.html')

def Birth_reg(request):
    if request.method=='POST':
        dob=request.POST.get('dob')
        name=request.POST.get('name')
        gen=request.POST.get('gender')
        f_name=request.POST.get('fname')
        m_name=request.POST.get('mname')
        dis_name=request.POST.get('dname')
        pob=request.POST.get('place')
        birth_add=request.POST.get('baddress')
        curr_add=request.POST.get('caddress')
        per_add=request.POST.get('paddress')
        email=request.POST.get('email')
        mob=request.POST.get('mobile')
        mot_edu=request.POST.get('motedu')
        mot_occ=request.POST.get('motocc')
        fat_edu=request.POST.get('fatedu')
        fat_occ=request.POST.get('fatocc')
        marr_age=request.POST.get('mar_age')
        deli_age=request.POST.get('del_age')
        date=request.POST.get('date')
        applicant=request.POST.get('app_name')
        birth=Birth(user=request.user,DOB=dob,name=name,gen=gen,f_name=f_name,m_name=m_name,dis_name=dis_name,place_of_bir=pob,bp_address=birth_add
                    ,c_address=curr_add, p_address=per_add,email=email,num=mob,m_edu=mot_edu,m_occ=mot_occ,f_edu=fat_edu,
                    f_occ=fat_occ,m_age_mar=marr_age,m_age_del=deli_age,date=date,appli_name=applicant)
    
        existing_data = Birth.objects.filter(
    DOB=dob, name=name, gen=gen, f_name=f_name, m_name=m_name, dis_name=dis_name,
    place_of_bir=pob, bp_address=birth_add, c_address=curr_add, p_address=per_add,
    email=email, num=mob, m_edu=mot_edu, m_occ=mot_occ, f_edu=fat_edu, f_occ=fat_occ,
    m_age_mar=marr_age, m_age_del=deli_age, date=date, appli_name=applicant
)       
        
        if existing_data.exists():
            messages.error(request, 'The Data Already Exists!!')
            return redirect('admin_menu')
            
        else:
            birth.save()
            messages.success(request, ' Birth Form Filled Successfully!!')
            return redirect('admin_menu')
        
   
    return render(request,'client/birth_form.html')

def Death_reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        relation=request.POST.get('dec_rel')
        mobile=request.POST.get('dec_mob')
        d_of_death=request.POST.get('dod')
        dname=request.POST.get('dec_name')
        gender=request.POST.get('gender')
        d_fat=request.POST.get('dec_fat')
        d_mot=request.POST.get('dec_mot')
        rel=request.POST.get('rel')
        age_death=request.POST.get('dec_death')
        cau=request.POST.get('dec_cause')
        add=request.POST.get('dec_add')
        death=Death(user=request.user,applicant_name=name,applicant_relation=relation,mobile=mobile,
                    date_of_death=d_of_death,deceased_name=dname,gender=gender,
                    deceased_fname=d_fat,deceased_mname=d_mot,religion=rel,
                    death_age=age_death,cause_of_death=cau, deceased_address=add)

        existing_data = Death.objects.filter(
            applicant_name=name, applicant_relation=relation, mobile=mobile,
            date_of_death=d_of_death, deceased_name=dname, gender=gender,
            deceased_fname=d_fat, deceased_mname=d_mot, religion=rel,
            death_age=age_death, cause_of_death=cau, deceased_address=add
        )
        if existing_data.exists():
            messages.error(request, 'The Data Already Exists!!')
            return redirect('admin_menu')
        else:
            death.save()
            messages.success(request, ' Death Form Filled Successfully!!')
            return redirect('admin_menu')
       
    
    return render(request,'client/death_form.html')

def Death_cert(request):
    if request.method=='POST':
        b=request.POST.get('view-certificate')
        death_data=Death.objects.filter(id=b)
   
    data={
        'death_data':death_data,
    }

    return render(request,'client/death_certificate.html',data)

def Birth_cert(request):
    if request.method=='POST':
        a=request.POST.get('view-certificate')
        birth_data=Birth.objects.filter(id=a)
        data={
            'birth_data':birth_data,
        }

    return render(request,'client/birth_certificate.html',data)

def Showcertificate(request):
    if request.user.is_staff:
        my_death=Death.objects.all()
        my_birth=Birth.objects.all()
        
    else:

        my_death=Death.objects.filter(user=request.user)
        my_birth=Birth.objects.filter(user=request.user)
        
    
    data={
        'my_death':my_death,
        'my_birth':my_birth,
    }
    return render(request,'client/mycertificate.html',data)

def Complaint_reg(request):
    if request.method == "POST":
        complaint_type = request.POST.get('compl_type')
        complaint_location = request.POST.get('compl_loc')  
        description = request.POST.get('desc')  
        document = request.FILES.get('document')  

    
        complaint = Complaint(
            user=request.user,
            compl_type=complaint_type,
            compl_loc=complaint_location,
            desc=description,
            document=document
        )
        complaint.save()
        return redirect('some_success_page')

 
    return render(request,'client/complaint.html')

def Mycomplaint(request):
    if request.user.is_staff:
        compl_info=Complaint.objects.all()
        
    else:
        compl_info=Complaint.objects.filter(user=request.user)  
    data={
        'compl_info':compl_info,
    }
    return render(request,'client/my_complaint.html',data)

def my_complaint(request):
    compl_info = [
        {"id": 1, "compl_type": "Water Leakage", "date_time": "2024-11-01", "status": "Pending"},
        {"id": 2, "compl_type": "Power Outage", "date_time": "2024-11-02", "status": "Resolved"},
        {"id": 3, "compl_type": "Road Damage", "date_time": "2024-11-03", "status": "In Progress"},
    ]
    return render(request, 'egramApp/my_complaint.html', {'compl_info': compl_info})

def success_page(request):
    return render(request, 'client/success_page.html')


def tax(request):
    return render(request, 'admin/admin_tax.html')


def certificates(request):
    return render(request, 'client/certificates.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')  
        
        if role == "admin":
            if username == "Kaustubh Kshirsagar" and password == "Kaus@123":

                user = authenticate(request, username=username, password=password)
                if user is None:
                    user = User.objects.create_user(username=username, password=password)
                    user.is_staff = True  
                    user.save()
                login(request, user)
                return redirect('admin_menu')  
            else:
                messages.error(request, "Invalid admin credentials")
                return redirect('signin') 
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_menu')  
            else:
                messages.error(request, "Invalid username or password")
                return redirect('signin')  

    return render(request, 'login.html')  


def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if not pass1 or not pass2:
            messages.error(request, 'Password fields cannot be empty.')
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if len(pass1) < 8 or not any(char.isdigit() for char in pass1) or \
           not any(char.isupper() for char in pass1) or not any(char.islower() for char in pass1):
            messages.error(request, 'Password must be at least 8 characters long and contain an uppercase letter, a lowercase letter, and a number.')
            return redirect('signup')

        try:
            user = UserModel(username=username, email=email, password=pass1)
            user.save()
            messages.success(request, 'Signup successful! Please log in.')
            return redirect('signin')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('signup')

    return render(request, 'signup.html')

def admin_menu(request):
    return render(request, 'admin/admin_menu.html')

def user_menu(request):
    return render(request, 'client/user_menu.html')
    
def transaction_list(request):
    users = User.objects.all()  
    return render(request, 'admin/transaction_list.html', {'users': users})

@csrf_exempt  
def save_transaction(request):
    if request.method == "POST":
        try:
            transactions_data = json.loads(request.POST.get("transactions", "[]"))

            for transaction in transactions_data:
                Transaction.objects.create(
                    user_name=transaction["user_name"],
                    amount=transaction["amount"],
                    status=transaction["status"],
                    last_date=transaction["last_date"]
                )

            return JsonResponse({"success": True, "message": "Transactions saved successfully."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return JsonResponse({"success": False, "message": "Invalid request method."})

def upload_payment_screenshot(request):
    if request.method == "POST":
        transaction_id = request.POST.get("transaction_id")
        screenshot = request.FILES.get("screenshot")

        if not screenshot:
            return JsonResponse({'success': False, 'message': 'Screenshot is required'})

        transaction = get_object_or_404(Transaction, id=transaction_id)
        transaction.payment_screenshot = screenshot
        transaction.save()

        return JsonResponse({'success': True, 'message': 'Payment screenshot uploaded successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def user_transactions(request):
    user_name = request.user.username  
    transactions = Transaction.objects.filter(user_name=user_name).order_by('-id') 

    return render(request, 'client/user_transactions.html', {'transactions': transactions})

def delete_complaint(request):
    if request.method == 'POST':
        complaint_id = request.POST.get('id')  
        try:

            complaint = Complaint.objects.get(id=complaint_id)
            complaint.delete()
            return JsonResponse({'success': True, 'message': 'Complaint deleted successfully.'})
        except Complaint.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Complaint not found.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def home_tax_view(request):
    transactions = HomeTax.objects.all()
    return render(request, 'hometax.html', {'transactions': transactions})

def upload_screenshot(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)

    if request.method == 'POST':
        screenshot = request.FILES.get('screenshot')
        if screenshot:
            transaction.screenshot = screenshot
            transaction.save()
        return JsonResponse({'message': 'Screenshot uploaded successfully!'})

    return render(request, 'upload_screenshot.html', {'transaction': transaction})

@login_required
def upload_payment_screenshot(request):
    if request.method == "POST":
        transaction_id = request.POST.get("transaction_id")
        payment_screenshot = request.FILES.get("payment_screenshot")

        if not transaction_id or not payment_screenshot:
            return JsonResponse({'success': False, 'message': 'Please upload a screenshot.'})

        try:
            transaction = Transaction.objects.get(id=transaction_id, user=request.user)
            transaction.payment_screenshot = payment_screenshot
            transaction.save()

            return JsonResponse({'success': True, 'message': 'Payment screenshot uploaded successfully!'})

        except Transaction.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Transaction not found.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def tax_client(request):
    return render(request, 'client/user_tax.html')


def transaction_screenshot(request):
    transactions = Transaction.objects.all()
    return render(request, 'admin/transcation_screenshot.html', {'transactions': transactions})
    

def home_taxsection(request):
    transactions = TaxTransaction.objects.all()
    return render(request, 'admin/home_taxsection.html', {'transactions': transactions})


@csrf_exempt
def delete_transaction(request, transaction_id):
    if request.method == "DELETE":
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            transaction.delete()
            return JsonResponse({"message": "Transaction deleted successfully"}, status=200)
        except Transaction.DoesNotExist:
            return JsonResponse({"error": "Transaction not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)

def transaction_view(request):
    transactions = Transaction.objects.select_related('uploaded_by').all()  
    return render(request, 'your_template.html', {'transactions': transactions})

def panchayat_info(request):
    members = PanchayatMember.objects.all()  
    return render(request, 'admin/Panchinfo.html', {"members": members})



openai.api_key = "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"
@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message', '').lower()

        response = {"text": "Sorry, I didn't understand that.", "options": []}

        if user_input in ['hi', 'hello', 'help', 'start']:
            response = {
                "text": "Please choose one of the services below:",
                "options": ["Birth Certificate", "Property Tax", "Complaints", "Website Overview"]
            }

        elif user_input == 'birth certificate':
            response = {
                "text": "What would you like to know about Birth Certificate?",
                "options": ["How to apply", "Required documents", "Check status"]
            }
        elif user_input == 'how to apply':
            response["text"] = "To apply for a Birth Certificate, go to 'Birth Form' in the main menu and fill out the required details."
        elif user_input == 'required documents':
            response["text"] = "You will need: Aadhar Card, Hospital Letter, and Parent's ID Proof."
        elif user_input == 'check status':
            response["text"] = "Visit the 'My Certificate' section to track your application."

        elif user_input == 'property tax':
            response = {
                "text": "Choose what you'd like to know about Property Tax:",
                "options": ["How to pay", "View Transactions", "Required details"]
            }
        elif user_input == 'how to pay':
            response["text"] = "Go to the 'User Tax' section and submit your property details with payment screenshot."
        elif user_input == 'view transactions':
            response["text"] = "Visit the 'User Transactions' section to see your history."
        elif user_input == 'required details':
            response["text"] = "You’ll need your property ID, name, and address to proceed."

        elif user_input == 'complaints':
            response = {
                "text": "Need help with complaints? Choose an option below:",
                "options": ["How to file", "Check status", "Required information"]
            }
        elif user_input == 'how to file':
            response["text"] = "Go to the 'Complaint' section and fill out the complaint form."
        elif user_input == 'required information':
            response["text"] = "Include your name, problem description, and any reference number if available."
        elif user_input == 'check status':
            response["text"] = "Use the 'My Complaint' section to track your complaint status."
        elif user_input == 'website overview':
            response["text"] = "Digital Grampanchayat offers services like Certificate Registration, Tax Payment, Complaints, Event Listings, and Real-Time Chat Support."

        return JsonResponse({"reply": response})

    
def chat_page(request):
  return render(request, 'admin/chatbot.html')

def get_population_data(request):
    data = VillagePopulation.objects.first()
    return render(request, 'population_modal_content.html', {'data': data})

def update_population_data(request):
    if request.method == 'POST':
        data = VillagePopulation.objects.first()
        data.total_population = request.POST.get('total_population')
        data.male_population = request.POST.get('male_population')
        data.female_population = request.POST.get('female_population')
        data.save()
        return JsonResponse({'status': 'success'})
    
