from django.db import models

# Create your models here.


class Category(models.Model):
    #1. Property 
    category_name = models.CharField(max_length=255)
    category_desc = models.TextField(blank=True)

    #2. Constructor 

    #3. Methods
    def __str__(self): # Dunder/Magic Methods 
        return self.category_name

    #4. Nested Class
    class Meta:
        #1. Property
        verbose_name = 'Category' #Singular
        verbose_name_plural = 'Categories' #Plural

        #2. Constructor

        #3. Methods

        #4. Nested Class