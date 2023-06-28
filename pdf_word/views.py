from django.shortcuts import render,redirect
from .models import *
# import os
     
# Create your views here.
def convert(request):
    if request.method == "POST":

        data = request.POST
        pdf_name = request.FILES.get('pdf_name')
        pdf_class.objects.create(pdf_name=pdf_name)
        print('submitted')
#           if str(receipe_image).endswith('.pdf'):
#                print("submitted")
#                from pdf2docx import Converter
#                # C:\Users\ASEEM\Documents\test\django_newton\public\static\pdf_fol\OOPS_in_Java.pdf
#                pdf_file = os.path.join('C:\\Users\\ASEEM\\Documents\\test\\django_newton\\public\\static\\pdf_fol',str(receipe_image))
#                docx_name=str(receipe_image).replace('pdf','docx')
#                docx_file = os.path.join('C:\\Users\\ASEEM\\Documents\\test\\django_newton\\public\\static\\pdf_fol',str(docx_name))
               
#                # docx_file = os.path.join(docx_name)


# # convert pdf to docx
#                cv = Converter(pdf_file)
#                cv.convert(docx_file)      # all pages by default
#                cv.close()
#                context={'f': docx_file,'d':docx_name}
#                print(f"downloadind {docx_file}")
#                return render(request,'pd.html',context)
     
    queryset = pdf_class.objects.all()
    
    context = {'p':queryset}  
     

    return render(request,"pdf_2_word.html",context)

# /media/{{receipe.receipe_image}}