from django.shortcuts import render,redirect
from frontendd.models import userregisterdb,donorregisterdb,makerequestdb,donateblooddb


# Create your views here.
def homepagefn(request):
    return render(request,"homepage.html")

def patientloginfn(request):
    return render(request,"PatientLogin.html")

def patientloginfnn(request):
    if request.method == "POST":
        un =request.POST.get('uname')
        pwd =request.POST.get('upass')
        if userregisterdb.objects.filter(username=un,password=pwd).exists():
            request.session['username'] = un
            request.session['password'] = pwd
            return redirect(patienthomePagefn)
        else:
            return redirect(patientloginfn)
    else:
        return redirect(patientloginfn)


def donorloginfn(request):
    return render(request,"DonorLogin.html")


def donorloginfnn(request):
    if request.method == "POST":
        un =request.POST.get('uname')
        pwd =request.POST.get('upass')
        if donorregisterdb.objects.filter(username=un,password=pwd).exists():
            request.session['username'] = un
            request.session['password'] = pwd
            return redirect(donorhomePagefn)
        else:
            return redirect(donorloginfn)
    else:
        return redirect(donorloginfn)

def patienthomePagefn(request):
    x=0
    data =makerequestdb.objects.filter(patientname=request.session['username'])
    for d in data:
        if d.patientname!="":
            x=x+1


    return render(request,"PatientPage.html",{'data':data,'x':x})


def donorhomePagefn(request):
    x = 0
    data = donateblooddb.objects.filter(donorname=request.session['username'])
    for d in data:
        if d.donorname != "":
            x = x + 1

    return render(request,"DonorPage.html",{'data':data,'x':x})

def pateientregfn(request):
    return render(request,"PatientReg.html")

def patienthistory(request):
    data = makerequestdb.objects.filter(patientname=request.session['username'])
    return render(request,"requestHistory.html",{'data':data})



def savepatientregfn(request):
    if request.method == "POST":
        a = request.POST.get('pusern')

        c = request.POST.get('ppass')
        d = request.POST.get('pcpass')
        e = request.POST.get('page')
        f = request.POST.get('pblood')
        g = request.POST.get('pdis')
        h = request.POST.get('paddress')
        i = request.POST.get('pcontact')
        img = request.FILES['pimage']
        obj = userregisterdb(username=a, password=c, confirmpassword=d, age=e,bloodgroup=f,disease=g,address=h,contact=i,photo=img)
        obj.save()
        return redirect(patientloginfn)


def donorregfn(request):
    return render(request,"DonorReg.html")



def savedonorregfn(request):
    if request.method == "POST":

        usern = request.POST.get('dusern')
        passs = request.POST.get('dpass')
        cpass = request.POST.get('dcpass')
        agee = request.POST.get('dage')
        blood = request.POST.get('dblood')

        addressp = request.POST.get('daddress')
        contactp = request.POST.get('dcontact')
        imge = request.FILES['dimage']
        obj = donorregisterdb(username=usern, password=passs, confirmpassword=cpass, age=agee,bloodgroup=blood,address=addressp,contact=contactp,photo=imge)
        obj.save()
        return redirect(donorloginfn)

def patientrequest(request):
    return render(request,"MakeRequestPat.html")

def saverequest(request):
    if request.method == "POST":
        name=request.POST.get('pname')
        age= request.POST.get('page')
        rea = request.POST.get('preason')
        blood=request.POST.get('pblood')
        uni = request.POST.get('punit')
        obj=makerequestdb(patientname=name,patientage=age,reason=rea,bloodgroup=blood,unit=uni)
        obj.save()
        return redirect(patienthomePagefn)


def donateBloodfn(request):
    return render(request,"DonateBlood.html")


def savedonatebloodfn(request):
    if request.method == "POST":
        name=request.POST.get('dname')
        age= request.POST.get('dage')
        dis = request.POST.get('ddis')
        blood=request.POST.get('dblood')
        uni = request.POST.get('dunit')

        obj=donateblooddb(donorname=name,donorage=age, disease =dis,bloodgroup=blood,unit=uni)
        obj.save()
        return redirect(donorhomePagefn)


def donationhistoryfn(request):
    data = donateblooddb.objects.filter(donorname=request.session['username'])
    return render(request, "DonationHistory.html", {'data': data})


def patientLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(patientloginfn)


def donorLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(donorloginfn)









