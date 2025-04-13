from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    home_tax_view, upload_screenshot, tax,
    user_transactions, upload_payment_screenshot,
    transaction_screenshot, home_taxsection,
    delete_transaction, panchayat_info
)

urlpatterns = [
    path('', views.Home, name='home'),
    path('logout/', views.Logout, name='logout'),
    path('aadhar/', views.Aadhar_val, name='aadhar'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.About, name='about'),
    path('profile/', views.Profile, name='profile'),
    path('birth_form/', views.Birth_reg, name='birth_form'),
    path('death_form/', views.Death_reg, name='death_form'),
    path('death_cert/', views.Death_cert, name='death_cert'),
    path('birth_cert/', views.Birth_cert, name='birth_cert'),
    path('my_cert/', views.Showcertificate, name='my_cert'),
    path('complaint/', views.Complaint_reg, name='complaint'),
    path('my_complaint/', views.Mycomplaint, name='my_complaint'),
    path('delete_complaint/', views.delete_complaint, name='delete_complaint'),
    path('success/', views.success_page, name='some_success_page'),
    path('tax/', views.tax, name='tax'),
    path('certificates/', views.certificates, name='certificates'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.Signup, name='signup'),
    path('admin_menu/', views.admin_menu, name='admin_menu'),
    path('user_menu/', views.user_menu, name='user_menu'),
    path('transactions/', views.transaction_list, name='transactions'),
    path('save_transaction/', views.save_transaction, name='save_transaction'),
    path('upload_screenshot/<int:transaction_id>/', upload_screenshot, name='upload_screenshot'),
    path('user-transactions/', user_transactions, name='user_transactions'),
    path('user_tax/', views.tax_client, name='user_tax'),
    path('TransactionScreenshot/', transaction_screenshot, name='transcation_screenshot'),
    path('home-tax/', home_taxsection, name='home_taxsection'),
    path('delete-transaction/<int:transaction_id>/', delete_transaction, name='delete_transaction'),
    path('panchinfo/', panchayat_info, name='panchinfo'),
    path('chatbot/', views.chatbot_response, name='chatbot'),
    path('chat/', views.chat_page, name='chat_page'),
    path('get_population_data/', views.get_population_data, name='get_population_data'),
    path('update_population_data/', views.update_population_data, name='update_population_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
