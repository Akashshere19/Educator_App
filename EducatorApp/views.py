from django.shortcuts import render,redirect
from .models import EducatorRecord
from .forms import EducatorRegistration
from django.contrib import messages

# Create your views here.
def add_Educator(request):
    if request.method=='POST':
        bn=EducatorRegistration(request.POST)
        if bn.is_valid():
            fn=bn.cleaned_data['FirstName']
            mn=bn.cleaned_data['MiddleName']
            ln=bn.cleaned_data['LastName']
            od=bn.cleaned_data['OutDate']
            id=bn.cleaned_data['InDate']
            cn=bn.cleaned_data['ClassName']
            mb=bn.cleaned_data['MobNo']
            reg=EducatorRecord(FirstName=fn,MiddleName=mn,LastName=ln,OutDate=od,InDate=id,ClassName=cn,MobNo=mb)
            reg.save()
            messages.success(request,"your details has been submitted.!")
            bn=EducatorRegistration()
    else:
        bn=EducatorRegistration()
    show=EducatorRecord.objects.all()
    return render(request,'update.html',{'form':bn,'show':show})

def delete_data(request,id): # use for Delete Data
    if request.method == 'POST':
        delete = EducatorRecord.objects.get(pk=id)
        delete.delete()
        messages.info(request,"Delete Successfully.")
        return redirect('/')
def update_data(request,id): # use for Update Data
    if request.method =='POST':
        edit =EducatorRecord.objects.get(pk=id)
        bn = EducatorRegistration(request.POST,instance=edit)
        if bn.is_valid():
            bn.save()
        messages.info(request, "Update Successfully.")
    else:
        edit = EducatorRecord.objects.get(pk=id)
        bn = EducatorRegistration(instance=edit)
    return render(request, 'update.html', {'form':bn})
    return redirect('/')
