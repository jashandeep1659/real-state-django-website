from django.db import models
from user.models import User


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="city")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)  # auto increment
    name = models.CharField(max_length=50)  # rent
    slug = models.SlugField(unique=True)  # rent
    goodname = models.CharField(max_length=50)  # rental
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TypeOf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    goodname = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    image = models.ImageField(upload_to="building")
    price = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    typeof = models.ForeignKey(TypeOf, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created"]


class Building_images(models.Model):
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="buildings")
    index = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class HandPick(models.Model):
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="property"
    )
    newchats = models.IntegerField(default=0)
    closed = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    reply_pending = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer"
    )
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agent")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="chat")
    message = models.TextField(
        null=True,
        blank=True,
    )
    image = models.ImageField(upload_to="message", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
