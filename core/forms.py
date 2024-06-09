from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

# class logout(logout):
#     pass





























# from django import forms
# from django_countries.fields import CountryField
# from django_countries.widgets import CountrySelectWidget


# PAYMENT_CHOICES = (
#     ('S', 'Stripe'),
#     ('P', 'PayPal')
# )


# class CheckoutForm(forms.Form):
#     shipping_address = forms.CharField(required=False)
#     shipping_address2 = forms.CharField(required=False)
#     shipping_country = CountryField(blank_label='(select country)').formfield(
#         required=False,
#         widget=CountrySelectWidget(attrs={
#             'class': 'custom-select d-block w-100',
#         }))
#     shipping_zip = forms.CharField(required=False)

#     billing_address = forms.CharField(required=False)
#     billing_address2 = forms.CharField(required=False)
#     billing_country = CountryField(blank_label='(select country)').formfield(
#         required=False,
#         widget=CountrySelectWidget(attrs={
#             'class': 'custom-select d-block w-100',
#         }))
#     billing_zip = forms.CharField(required=False)

#     same_billing_address = forms.BooleanField(required=False)
#     set_default_shipping = forms.BooleanField(required=False)
#     use_default_shipping = forms.BooleanField(required=False)
#     set_default_billing = forms.BooleanField(required=False)
#     use_default_billing = forms.BooleanField(required=False)

#     payment_option = forms.ChoiceField(
#         widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


# class CouponForm(forms.Form):
#     code = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Promo code',
#         'aria-label': 'Recipient\'s username',
#         'aria-describedby': 'basic-addon2'
#     }))


# class RefundForm(forms.Form):
#     ref_code = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea(attrs={
#         'rows': 4
#     }))
#     email = forms.EmailField()


# class PaymentForm(forms.Form):
#     stripeToken = forms.CharField(required=False)
#     save = forms.BooleanField(required=False)
#     use_default = forms.BooleanField(required=False)

