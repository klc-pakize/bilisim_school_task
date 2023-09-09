from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Problem

@receiver(pre_save, sender = Problem)

# Kullanıcının girdiği title bilgilerine göre expected_output hesaplanmasını sağlayan signals fon
def colcature_expected_output(sender, instance, **kwargs):
    
    # Eğer problem başlığı-title "Say hello with python" ise beklenen çıktıyı-expected_output ayarlar.
    if instance.title == "Say hello with python":
        instance.expected_output = "Hello World"

    # Eğer problem başlığı-title "Arithmetic Operators - Sum" ise girdiyi-input parçala ve toplamı hesapla.
    elif instance.title == "Arithmetic Operators - Sum":
        instance_input = instance.input
        instance_input_list = instance_input.split(",")
        sum = 0
        for input in instance_input_list:
            sum += int(input)   
        instance.expected_output = sum

    # Eğer problem başlığı-title "Loops" ise karelerini hesapla ve çıktıyı-expected_output ayarlar.
    elif instance.title == "Loops":
        list_numbers = []
        numbers = int(instance.input)
        for i in range(numbers):
            list_numbers.append(i ** 2)
            str_liste = str(list_numbers)
            
        instance.expected_output = str_liste[1:-1]
        
    # Eğer problem başlığı-title tanımlanmamışsa, kullanıcıya belirli sorunları seçmesi gerektiğini belirten bir uyarı verir.    
    else:
        instance.expected_output = "Please choose from defined problems"