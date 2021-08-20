from django.forms import ModelForm
from ceevee.models import Customer

# Create the form class.
class CustomerForm(ModelForm):
     class Meta:
         model = Customer
         fields = '__all__'

#customer= Customer.objects.get(pk=1)
#form = CustomerForm(instance=customer)