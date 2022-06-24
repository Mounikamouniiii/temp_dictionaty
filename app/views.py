from django.shortcuts import render

# Create your views here.
def mouni(request):
    d={'name':'GULLAIAH GARI MOUNIKA','age':23,'phone':9381300431}
    return render(request,'chinni.html',context=d)
