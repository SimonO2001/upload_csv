from django.contrib import admin
from django.urls import path

from uploader.views import UploadView

from django.urls import path
from uploader import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', UploadView.as_view(), name='upload_data'),  # Update the name here
    path('display/', views.display_data, name='display_data'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add/', views.add_product, name='add_product'),
]
