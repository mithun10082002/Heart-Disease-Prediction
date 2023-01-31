from django.shortcuts import render
from PredictionApp.HeartDiseaseAnalysis import train
import os
# Create your views here.
def home(request):
    if request.method=="GET":
        print(os.getcwd())
        return render(request,'home.html')
    if request.method=='POST':
        age=int(request.POST['age'])
        sex=int(request.POST['sex'])
        cp=int(request.POST['cp'])
        trestbps=int(request.POST['trestbps'])
        chol=int(request.POST['chol'])
        fbs=int(request.POST['fbs'])
        restecg=int(request.POST['restecg'])
        thalach=int(request.POST['thalach'])
        exang=int(request.POST['exang'])
        oldpeak=int(request.POST['oldpeak'])
        slope=int(request.POST['slope'])
        ca=int(request.POST['ca'])
        thal=int(request.POST['thal'])
        print(type(age))
        res=train(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        return render(request,'res.html',{'res':res[0]})

