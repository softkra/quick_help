from django.db import models

""" DEFINITIONS OF MODELS PROYECT """

class Clients(models.Model):

    """Model for managing Clients

    Attributes:
        document: Client document
        first_name: Client first_name
        last_name: Client last_name
        email: Client email
        created: Created Date

    """

    document = models.CharField(max_length=100)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        default_permissions = ()

    def __str__(self):
        return '{} {} {} {}'.format(self.pk, self.document, self.first_name, self.last_name)

    def get_quantity_bills(self):
        bills = Bills.objects.filter(
            client_id=self.pk
        )

        return len(bills)


class Bills(models.Model):

    """Model for managing Bills

    Attributes:
        client_id: Foreignkey to Clients
        company_name: Bill company_name
        nit: Bill nit
        code: Bill code
        created: Created date

    """

    client_id = models.ForeignKey('Clients', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    nit = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'
        default_permissions = ()

    def __str__(self):
        return '{} {} {} {}'.format(self.client_id.document, self.company_name, self.nit, self.code)

class Products(models.Model):

    """Model for managing Products

    Attributes:
        name: Product name
        description: Product description
        attribute: Product attribute
        created: Created date

    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    attribute = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        default_permissions = ()

    def __str__(self):
        return '{} {} {}'.format(self.name, self.description, self.attribute)

class BillsProducts(models.Model):

    """Model for managing Relationship of Bills and Products

    Attributes:
        client_id: Foreignkey to Clients
        product_id: Foreignkey to Products
        created: Created date

    """

    bill_id = models.ForeignKey('Bills', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Bill-Product'
        verbose_name_plural = 'Bills-Products'
        default_permissions = ()

    def __str__(self):
        return '{} {}'.format(self.bill_id, self.product_id)

