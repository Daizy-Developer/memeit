from django.shortcuts import render
from meme.models import Meme,Categorie
# Create your views here.
def index(request):
    meme_category =  Categorie.objects.all()
    print(meme_category) 
    return render(request,"meme/index.html",{"meme_category":meme_category})

def Get_Category(request,Category):
   meme_category = Categorie.objects.filter(Category=Category).first()
   memes = Meme.objects.filter(Category=meme_category)
   print(memes)
   return render(request,"meme/meme.html" ,{"memes":memes})