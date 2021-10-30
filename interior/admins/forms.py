from django import forms

from products.models import Product, ProductsCategory
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserAdminsCreateForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-label'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'image', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminsUpdateForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4',
                                                            'readonly': False}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'readonly': False}))

    class Meta:
        model = User
        fields = ('username', 'image', 'email', 'first_name', 'last_name')


choices1 = [('True', 'Да'), ('True', 'Нет')]
choices2 = [(c.id, '— ' + c.name.capitalize()) for c in ProductsCategory.objects.all()]


class ProductAdminsCreateForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-label'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    action = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-control py-4'}))
    descriptions = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    hover_icon_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    category = forms.ChoiceField(widget=forms.SelectMultiple(
            attrs={'class': 'form-control py-4'}),
        choices=choices2)

    class Meta:
        model = Product
        fields = ('image', 'title', 'action', 'descriptions', 'hover_icon_description', 'price', 'quantity',
                  'category')
