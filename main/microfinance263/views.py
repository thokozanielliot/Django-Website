from django.shortcuts import render,redirect
from .models import Blacklist
from .forms import BlacklistForm

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')

def create(request):  
    if (request.method == "POST"):  
        form = BlacklistForm(request.POST)  
        if (form.is_valid()):  
            try:  
                form.save()  
                return redirect('show')  
            except:  
                pass  
    else:  
        form = BlacklistForm()  
    return render(request,'create.html', {'form':form}) 

def show(request):  
    searchTerm = request.GET.get('searchName')
    no_records =Blacklist.objects.count()
    if (searchTerm):
        blacklist = Blacklist.objects.filter(first_name__icontains = searchTerm)
    else:
        blacklist = Blacklist.objects.all().order_by('-date_blacklisted')
    return render(request, 'show.html', {'searchName': searchTerm, 'blacklist':blacklist, 'no_records': no_records})

def edit(request, id):  
    blacklist = Blacklist.objects.get(id=id)  
    return render(request,'edit.html', {'blacklist':blacklist})  

def update(request, id):  
    blacklist = Blacklist.objects.get(id=id)  
    form = BlacklistForm(request.POST, instance = blacklist)  
    try:
        if (form.is_valid()):  
            form.save()  
            return redirect('show')
        else:
            blacklist.first_name = request.POST['first_name']
            blacklist.surname = request.POST['surname']
            blacklist.account_name = request.POST['account_name']
            blacklist.section = request.POST['choice']
            blacklist.institution = request.POST['institution']
            blacklist.account_manager = request.POST['account_manager']
            blacklist.date_blacklisted = request.POST['date_blacklisted']
            blacklist.save()
            return redirect('show')
    except ValueError:
            return render(request, 'edit.html', {'blacklist': blacklist, 'form': form})

def delete(request, id):  
    blacklist = Blacklist.objects.get(id=id)  
    blacklist.delete()  
    return redirect("/show")  