from django.shortcuts import render
from . import forms 

def form_name_view(request):
    form = forms.FormName()
# check to see if we are getting a POST request back    
    if request.method == 'POST':
        form = forms.FormName(request.POST)       
        if form.is_valid():       
         print("Form validation successful! See console for information:")
         print("Name : "+form.cleaned_data['name'])
         print("Email : "+form.cleaned_data['email'])
         print("Message : "+form.cleaned_data['text'])
    return render(request,'home.html',{'form':form})

# from django.shortcuts import render
# from . import forms

# def form_name_view(request):
#     form = forms.FormName()
# #Check to see if we are getting a POST request back
#     if request.method == "POST":
#         form = forms.FormName(request.POST)
#         if form.is_valid():
#          print("Form validation successful! See console for information:")
#          print("Name: "+form.cleaned_data['name'])
#          print("email: "+form.cleaned_data['email'])
#          print("message: "+form.cleaned_data['text'])
#     return render(request, 'home.html', {'form': form})