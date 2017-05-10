from django.shortcuts import render


# Create your views here.
def pagina_principal_view(request):
	return render(request,'index.html',{})

def admin(request):
	return render(request,'admin.html',{})
