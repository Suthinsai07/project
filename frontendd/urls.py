from django.urls import path
from frontendd import views

urlpatterns = [
    path('homepagefn/',views.homepagefn,name="homepagefn"),
    path('patientloginfn/',views.patientloginfn,name="patientloginfn"),
    path('donorloginfn/',views.donorloginfn,name="donorloginfn"),
    path('patienthomePagefn/',views.patienthomePagefn,name="patienthomePagefn"),
    path('pateientregfn/',views.pateientregfn,name="pateientregfn"),
    path('savepatientregfn/',views.savepatientregfn,name="savepatientregfn"),
    path('donorregfn/',views.donorregfn,name="donorregfn"),
    path('savedonorregfn/',views.savedonorregfn,name="savedonorregfn"),
    path('patientrequest/',views.patientrequest,name="patientrequest"),
    path('patientloginfnn/',views.patientloginfnn,name="patientloginfnn"),
    path('saverequest/',views.saverequest,name="saverequest"),
    path('patienthistory/',views.patienthistory,name="patienthistory"),
    path('donorhomePagefn/',views.donorhomePagefn,name="donorhomePagefn"),
    path('donorloginfnn/',views.donorloginfnn,name="donorloginfnn"),
    path('donateBloodfn/',views.donateBloodfn,name="donateBloodfn"),
    path('savedonatebloodfn/',views.savedonatebloodfn,name="savedonatebloodfn"),
    path('donationhistoryfn/',views.donationhistoryfn,name="donationhistoryfn"),
    path('patientLogout/',views.patientLogout,name="patientLogout"),
    path('donorLogout/',views.donorLogout,name="donorLogout")

]