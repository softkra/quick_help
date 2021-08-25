from django.urls import path
from . views import *

urlpatterns = [
	path('add-user',CreateUserAPIView.as_view(),name='add-user'),

	path('add-product/',CreateProductAPIView.as_view(),name='add-product'),
    path('detail-product/<int:pk>/',DetailProductsAPIView.as_view(),name='detail-product'),
    path('delete-product/<int:pk>/',DeleteProductsAPIView.as_view(),name='delete-product'),
    path('update-product/<int:pk>/',UpdateProductAPIView.as_view(),name='update-product'),

    path('add-client/',CreateClientsAPIView.as_view(),name='add-client'),
    path('detail-client/<int:pk>/',DetailClientsAPIView.as_view(),name='detail-client'),
    path('delete-client/<int:pk>/',DeleteClientsAPIView.as_view(),name='delete-client'),
    path('update-client/<int:pk>/',UpdateClientsAPIView.as_view(),name='update-client'),

    path('add-bill/',CreateBillsAPIView.as_view(),name='add-bill'),
    path('detail-bill/<int:pk>/',DetailBillsAPIView.as_view(),name='detail-bill'),
    path('delete-bill/<int:pk>/',DeleteBillsAPIView.as_view(),name='delete-bill'),
    path('update-bill/<int:pk>/',UpdateBillsAPIView.as_view(),name='update-bill'),

    path('add-bill-product/',CreateBillsProductsAPIView.as_view(),name='add-bill-product'),
    path('detail-bill-product/<int:pk>/',DetailBillsProductsAPIView.as_view(),name='detail-bill-product'),
    path('delete-bill-product/<int:pk>/',DeleteBillsProductsAPIView.as_view(),name='delete-bill-product'),
    path('update-bill-product/<int:pk>/',UpdateBillsProductsAPIView.as_view(),name='update-bill-product'),

	path('client-report/',ClientReportAPIView.as_view(),name='client-report'),
	path('csv-clients/',ClientCsvUpload.as_view(),name='csv-clients'),
    
]