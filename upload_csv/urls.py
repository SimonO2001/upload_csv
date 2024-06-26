from django.contrib import admin
from django.urls import path
from uploader.views import UploadView
from uploader import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', UploadView.as_view(), name='upload'),
    path('', views.display_data, name='display_data'),
    path('edit/<int:company_id>/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:company_id>/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add/', views.add_product, name='add_product'),
    path('copy/<int:company_id>/<int:product_id>/', views.copy_and_edit_data, name='copy_and_edit_data'),
    # path('select_company/', views.select_company, name='select_company'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('fetch-products/', views.fetch_products, name='fetch_products'),
    path('company_fields/', views.fetch_company_fields, name='fetch_company_fields'),
    # path('update-columns/', views.update_columns, name='update_columns'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

