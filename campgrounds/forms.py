from django.forms import ModelForm
from .models import Campground
class UpdateForm(ModelForm):
    class Meta:
        model = Campground
        fields = ['name','description','price']
    