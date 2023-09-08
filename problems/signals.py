from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Problem

@receiver(pre_save, sender = Problem)
def colcature_expected_output(sender, instance, **kwargs):
    
    if instance.title == "Say hello with python":
        instance.expected_output = "Hello World"

    elif instance.title == "Arithmetic Operators - Sum":
        a = instance.input
        b = a.split(",")
        sum = 0
        for i in b:
            sum += int(i)   
        instance.expected_output = sum

    elif instance.title == "Loops":
        liste = []
        numbers = int(instance.input)
        for i in range(numbers):
            liste.append(i ** 2)
            str_liste = str(liste)
            
        instance.expected_output = str_liste[1:-1]
        
    else:
        instance.expected_output = "Please choose from defined problems"