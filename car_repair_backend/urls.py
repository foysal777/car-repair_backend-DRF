
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/' ,include('account.urls')),
    path('appoint/' ,include('appointment.urls')),
    path('blog/' ,include('blog.urls')),
    path('parts/' ,include('parts.urls')),
    path('payment/' ,include('payment.urls')),
    path('contact/' ,include('contact.urls')),
]
