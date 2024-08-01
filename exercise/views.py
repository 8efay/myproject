from django.shortcuts import render,redirect,HttpResponse

def home(request):
    return render(request, 'layout.html')  # layout.html dosyasını render eder
    return HttpResponse("home")
def about (request):
    return render (request,"about.html")
# Create your views here.
def contact (request):
    return render(request,"contact.html")
def boyun(request):
    return render(request,"boyun.html")
def omuz(request):
    return render(request,"omuz.html")
def sırt(request):
    return render(request,"sırt.html")
def bel(request):
    return render(request,"bel.html")
def el_ve_el_bilegi(request):
    return render(request,"el_ve_el_bilegi.html")
def kalca(request):
    return render(request,"kalca.html")
def ayak(request):
    return render(request,"ayak.html")

