import csv

from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from rest_framework.views import APIView
from . serializers import ProductsModelSerializer, ClientsModelSerializer
from django.core import serializers
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.db import transaction, IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .serializers import FileUploadSerializer
from rest_framework import generics
import io

""" MODULE: USER """

"""
    Class to create user system
"""
class CreateUserAPIView(APIView):
    def post(self,request):
        """
            POST Method
        """
        try:
            user = User.objects.create_user(
                request.data['email'],
                request.data['email'],
                request.data['password']
            )
            return Response("User added successfully")
        except MultiValueDictKeyError:
            return Response("Error adding the user")
        except IntegrityError:
            return Response("Database error adding the user")

""" MODULE: PRODUCTS """

"""
    Class to update product record
"""
class UpdateProductAPIView(APIView):
    """
        POST Method
        Params:
            pk: product_id
            data: {
                name: Product name
                description: Product description
                attribute: Product attribute
            }
    """
    def post(self,request,pk):
        try:
            product = Products.objects.get(id=pk)
            product.name = request.data['name']
            product.description = request.data['description']
            product.attribute = request.data['attribute']
            product.save()
            return Response("Product updated successfully")
        except ObjectDoesNotExist:
            return Response("Product Does not exist")
        except MultiValueDictKeyError:
            return Response("Error updating the product")
        except IntegrityError:
            return Response("Database error updating the product")

"""
    Class to create product record
"""
class CreateProductAPIView(APIView):
    """
        POST Method
        Params:
            data: {
                name: Product name
                description: Product description
                attribute: Product attribute
            }
    """
    def post(self,request):
        try:
            product = Products(
                name = request.data['name'],
                description = request.data['description'],
                attribute = request.data['attribute'],
            )
            product.save()
            return Response("Product added successfully")
        except MultiValueDictKeyError:
            return Response("Error adding the product")
        except IntegrityError:
            return Response("Database error adding the product")

"""
    Class to show detail product record
"""
class DetailProductsAPIView(APIView):
    """
        GET Method
        Params:
            pk: product_id
    """
    def get(self, request, pk):
        try:
            result = Products.objects.get(id=pk)
            serializer = ProductsModelSerializer(result, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response("Product Does not Exist")

"""
    Class to delete product record
"""
class DeleteProductsAPIView(APIView):
    """
        GET Method
        Params:
            pk: product_id
    """
    def get(self, request, pk):
        try:
            result = Products.objects.get(id=pk)
            result.delete()
            return Response("Product deleted successfully")
        except ObjectDoesNotExist:
            return Response("Product Does not Exist")

""" MODULE: CLIENTS """

"""
    Class to create client record
"""
class CreateClientsAPIView(APIView):
    """
        POST Method
        Params:
            data: {
                document: Client document
                first_name: Client first_name
                last_name: Client last_name
                email: Client email
            }
    """
    def post(self,request):
        try:
            client = Clients(
                document = request.data['document'],
                first_name = request.data['first_name'],
                last_name = request.data['last_name'],
                email = request.data['email'],
            )
            client.save()
            return Response("Client added successfully")
        except MultiValueDictKeyError:
            return Response("Error adding the client")
        except IntegrityError:
            return Response("Database error adding the client")

"""
    Class to update client record
"""
class UpdateClientsAPIView(APIView):
    """
        POST Method
        Params:
            pk: client_id
            data: {
                document: Client document
                first_name: Client first_name
                last_name: Client last_name
                email: Client email
            }
    """
    def post(self,request,pk):
        client = Clients.objects.raw("SELECT * FROM api_clients WHERE id = {} LIMIT 1".format(pk))
        if len(client) > 0:
            try:
                client = Clients.objects.get(id=pk)
                client.document = request.data['document']
                client.first_name = request.data['first_name']
                client.last_name = request.data['last_name']
                client.email = request.data['email']
                client.save()
                return Response("Client updated successfully")
            except ObjectDoesNotExist:
                return Response("Client Does not exist")
            except MultiValueDictKeyError:
                return Response("Error updating the client")
            except IntegrityError:
                return Response("Database error updating the client")
        else:
            return Response("Client Does not exist")

"""
    Class to show details client record
"""
class DetailClientsAPIView(APIView):
    """
        GET Method
        Params:
            pk: client_id
    """
    def get(self, request, pk):
        result = Clients.objects.raw("SELECT * FROM api_clients WHERE id = {} LIMIT 1".format(pk))
        if len(result) > 0:
            result_json = {}
            result_json['document'] = result[0].document
            result_json['first_name'] = result[0].first_name
            result_json['last_name'] = result[0].last_name
            result_json['email'] = result[0].email
            return Response(result_json)
        else:
            return Response("Client Does not Exist")

"""
    Class to delete client record
"""
class DeleteClientsAPIView(APIView):
    """
        GET Method
        Params:
            pk: client_id
    """
    def get(self, request, pk):
        result = Clients.objects.raw("SELECT * FROM api_clients WHERE id = {} LIMIT 1".format(pk))
        if len(result) > 0:
            result = Clients.objects.get(id=pk)
            result.delete()
            return Response("Client deleted successfully")
        else:
            return Response("Client Does not Exist")

""" MODULE: BILLS """

"""
    Class to create bill record
"""
class CreateBillsAPIView(APIView):
    """
        POST Method
        Params:
            data: {
                client_id: ForeignKey client_id
                company_name: Bill company_name
                nit: Bill nit
                code: Bill code
            }
    """
    def post(self,request):
        try:
            client = Clients.objects.get(id=request.data['client_id'])
            bill = Bills(
                client_id = client,
                company_name = request.data['company_name'],
                nit = request.data['nit'],
                code = request.data['code'],
            )
            bill.save()
            return Response("Bill added successfully")
        except Clients.DoesNotExist:
            return Response("Client not found")
        except MultiValueDictKeyError:
            return Response("Error adding the bill")
        except IntegrityError:
            return Response("Database error adding the bill")

"""
    Class to update bill record
"""
class UpdateBillsAPIView(APIView):
    """
        POST Method
        Params:
            pk: bill_id
            data: {
                client_id: ForeignKey client_id
                company_name: Bill company_name
                nit: Bill nit
                code: Bill code
            }
    """
    def post(self,request,pk):
        bill = Bills.objects.raw("SELECT * FROM api_bills WHERE id = {} LIMIT 1".format(pk))
        if len(bill) > 0:
            try:
                bill = Bills.objects.get(id=pk)
                bill.client_id = Clients.objects.get(id=request.data['client_id'])
                bill.company_name = request.data['company_name']
                bill.nit = request.data['nit']
                bill.code = request.data['code']
                bill.save()
                return Response("Bill updated successfully")
            except Clients.DoesNotExist:
                return Response("Client Does not exist")
            except Bills.DoesNotExist:
                return Response("Bill Does not exist")
            except MultiValueDictKeyError:
                return Response("Error updating the bill")
            except IntegrityError:
                return Response("Database error updating the bill")
        else:
            return Response("Bill Does not exist")

"""
    Class to show detail bill record
"""
class DetailBillsAPIView(APIView):
    """
        GET Method
        Params:
            pk: bill_id
    """
    def get(self, request, pk):
        result = Bills.objects.raw("SELECT * FROM api_bills WHERE id = {} LIMIT 1".format(pk))
        if len(result) > 0:
            result_json = {}
            result_json['client_id'] = result[0].client_id.id
            result_json['company_name'] = result[0].company_name
            result_json['nit'] = result[0].nit
            result_json['code'] = result[0].code
            return Response(result_json)
        else:
            return Response("Bill Does not Exist")

"""
    Class to delete bill record
"""
class DeleteBillsAPIView(APIView):
    """
        GET Method
        Params:
            pk: bill_id
    """
    def get(self, request, pk):
        result = BillsProducts.objects.raw("SELECT * FROM api_bills WHERE id = {} LIMIT 1".format(pk))
        if len(result) > 0:
            result = BillsProducts.objects.get(id=pk)
            result.delete()
            return Response("Bill deleted successfully")
        else:
            return Response("Bill Does not Exist")

""" MODULE: BILLS-PRODUCTS """

"""
    Class to delete bill-product record
"""
class CreateBillsProductsAPIView(APIView):
    """
        POST Method
        Params:
            data: {
                bill_id: ForeignKey bill_id
                product_id: ForeignKey product_id
            }
    """
    def post(self,request):
        try:
            bill = Bills.objects.get(id=request.data['bill_id'])
            product = Products.objects.get(id=request.data['product_id'])
            billProduct = BillsProducts(
                bill_id = bill,
                product_id = product,
            )
            billProduct.save()
            return Response("BillProduct added successfully")
        except Bills.DoesNotExist:
            return Response("Bill not found")
        except Products.DoesNotExist:
            return Response("Product not found")
        except MultiValueDictKeyError:
            return Response("Error adding the billProduct")
        except IntegrityError:
            return Response("Database error adding the billProduct")

"""
    Class to update bill-product record
"""
class UpdateBillsProductsAPIView(APIView):
    """
        POST Method
        Params:
            pk: bill_product_id
            data: {
                bill_id: ForeignKey bill_id
                product_id: ForeignKey product_id
            }
    """
    def post(self,request,pk):
        billProduct = BillsProducts.objects.raw("SELECT * FROM api_billsproducts WHERE id = {} LIMIT 1".format(pk))
        if len(billProduct) > 0:
            try:
                billProduct = BillsProducts.objects.get(id=pk)
                billProduct.bill_id = Bills.objects.get(id=request.data['bill_id'])
                billProduct.product_id = Products.objects.get(id=request.data['product_id'])
                billProduct.save()
                return Response("BillProduct updated successfully")
            except Bills.DoesNotExist:
                return Response("Bill Does not exist")
            except Products.DoesNotExist:
                return Response("Product Does not exist")
            except BillsProducts.DoesNotExist:
                return Response("BillProduct Does not exist")
            except MultiValueDictKeyError:
                return Response("Error updating the billProduct")
            except IntegrityError:
                return Response("Database error updating the billProduct")
        else:
            return Response("BillProduct Does not exist")

"""
    Class to show detail bill-product record
"""
class DetailBillsProductsAPIView(APIView):
    """
        GET Method
        Params:
            pk: bill_product_id
    """
    def get(self, request, pk):
        result = BillsProducts.objects.raw("SELECT * FROM api_billsproducts WHERE id = {} LIMIT 1".format(pk))
        if len(result) > 0:
            result_json = {}
            result_json['bill_id'] = result[0].bill_id.id
            result_json['product_id'] = result[0].product_id.id
            return Response(result_json)
        else:
            return Response("BillProduct Does not Exist")

"""
    Class to delete bill-product record
"""
class DeleteBillsProductsAPIView(APIView):
    """
        GET Method
        Params:
            pk: bill_product_id
    """
    def get(self, request, pk):
        result = BillsProducts.objects.raw("SELECT * FROM api_billsproducts WHERE id = {} LIMIT 1".format(pk))
        if len(result) > 0:
            result = BillsProducts.objects.get(id=pk)
            result.delete()
            return Response("BillProduct deleted successfully")
        else:
            return Response("BillProduct Does not Exist")

"""
    Class to export CSV file from client records
"""
class ClientReportAPIView(APIView):
    """
        GET Method
    """
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="client_report.csv"'

        writer = csv.writer(response)

        header = [
            "Documento",
            "Nombre completo",
            "Facturas relacionadas"
        ]
        writer.writerow(header)

        clients = Clients.objects.all()
        for row in clients:
            data = [
                row.document,
                "{} {}".format(row.first_name, row.last_name),
                row.get_quantity_bills()
            ]
            writer.writerow(data)
        return response

"""
    Class to import CSV file from client records
"""
class ClientCsvUpload(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    """
        POST Method
        Params:
            file: CSV file
    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        counter = 0
        for row in reader:
            data = {}
            list_row = list(row)
            
            data['document'] = list_row[0]
            data['first_name'] = list_row[1]
            data['last_name'] = list_row[2]
            data['email'] = list_row[3]
            serializer_client = ClientsModelSerializer(data=data)
            if serializer_client.is_valid():
                serializer_client.save()
                counter += 1

        return Response("{} Clients created successfully".format(counter))