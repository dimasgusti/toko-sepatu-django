from django import forms

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'address', 'telephone']
        
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400'}))
#     address = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400'}))
#     telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400'}))