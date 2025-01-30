from django.db import models
from django.template.context_processors import media
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs = {"pk": self.pk})


class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


class Bike(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='bikes')
    supplier = models.ManyToManyField(Supplier, related_name='bikes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("bike_detail", kwargs = {"pk": self.pk})

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    feedback = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.feedback

    def get_absolute_url(self):
        return reverse("review_detail", kwargs = {"pk": self.pk})

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    bikes = models.ManyToManyField(Bike, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer}"

class Comment(models.Model):
    bike = models.ForeignKey("Bike", related_name="comments", on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.bike.name, self.username)

