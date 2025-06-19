from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import FA1, FA2, FA3, FA4
from .forms import FA1form, FA2form, FA3form, FA4form
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import csv



def home(request):
    records = FA1.objects.all()
    return render(request, 'home.html', {'records': records})
def next(request):
    records2 = FA2.objects.all()
    return render(request, 'next.html', {'records2': records2})
def next2(request):
    records3 = FA3.objects.all()
    return render(request, 'next2.html', {'records3': records3})
def next3(request):
    records4 = FA4.objects.all()
    return render(request, 'next3.html', {'records4': records4})

def add_record(request):
    if request.method == 'POST':
        form = FA1form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FA1form()
    return render(request, 'add_record.html', {'form': form})

def add_record2(request):
    if request.method == 'POST':
        form2 = FA2form(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('next')
    else:
        form2 = FA2form()
    return render(request, 'add_record2.html', {'form2': form2})

def add_record3(request):
    if request.method == 'POST':
        form3 = FA3form(request.POST)
        if form3.is_valid():
            form3.save()
            return redirect('next2')
    else:
        form3 = FA3form()
    return render(request, 'add_record3.html', {'form3': form3})

def add_record4(request):
    if request.method == 'POST':
        form4 = FA4form(request.POST)
        if form4.is_valid():
            form4.save()
            return redirect('next3')
    else:
        form4 = FA4form()
    return render(request, 'add_record4.html', {'form4': form4})

def delete_record(request, pk):
    record = get_object_or_404(FA1, pk=pk)
    record.delete()
    return redirect('home')

def delete_record2(request, pk):
    record2 = get_object_or_404(FA2, pk=pk)
    record2.delete()
    return redirect('next')

def delete_record3(request, pk):
    try:
        record3 = FA3.objects.get(pk=pk)
        record3.delete()
        return redirect('next2')
    except FA3.DoesNotExist:
        return redirect('next2')  # Redirect to the next2 page if the record does not exist

def delete_record4(request, pk):
    record4 = get_object_or_404(FA4, pk=pk)
    record4.delete()
    return redirect('next3')


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="FA1.csv"'

    writer = csv.writer(response)
    writer.writerow(['SL No', 'Name', 'Eng', 'Kan', 'Hin', 'Maths', 'Sci', 'Soc Sci', 'Total'])

    records = FA1.objects.all()
    for record in records:
        writer.writerow([record.slno, record.name, record.eng, record.kan, record.hin, record.maths, record.sci, record.soc_sci, record.total])

    return response

def export_csv2(request):
    response2 = HttpResponse(content_type='text/csv')
    response2['Content-Disposition'] = 'attachment; filename="FA2.csv"'

    writer = csv.writer(response2)
    writer.writerow(['SL No', 'Name', 'Eng', 'Kan', 'Hin', 'Maths', 'Sci', 'Soc Sci', 'Total'])

    records2 = FA2.objects.all()
    for record in records2:
        writer.writerow([record.slno, record.name, record.eng, record.kan, record.hin, record.maths, record.sci, record.soc_sci, record.total])

    return response2 

def export_csv3(request):
    response3 = HttpResponse(content_type='text/csv')
    response3['Content-Disposition'] = 'attachment; filename="FA3.csv"'

    writer = csv.writer(response3)
    writer.writerow(['SL No', 'Name', 'Eng', 'Kan', 'Hin', 'Maths', 'Sci', 'Soc Sci', 'Total'])

    records3 = FA3.objects.all()
    for record in records3:
        writer.writerow([record.slno, record.name, record.eng, record.kan, record.hin, record.maths, record.sci, record.soc_sci, record.total])

    return response3

def export_csv4(request):
    response4 = HttpResponse(content_type='text/csv')
    response4['Content-Disposition'] = 'attachment; filename="FA4.csv"'

    writer = csv.writer(response4)
    writer.writerow(['SL No', 'Name', 'Eng', 'Kan', 'Hin', 'Maths', 'Sci', 'Soc Sci', 'Total'])

    records4 = FA4.objects.all()
    for record in records4:
        writer.writerow([record.slno, record.name, record.eng, record.kan, record.hin, record.maths, record.sci, record.soc_sci, record.total])

    return response4

def aggregate_marks(request):
    aggregated_records = []

    fa1_records = FA1.objects.all()
    fa2_records = FA2.objects.all()
    fa3_records = FA3.objects.all()
    fa4_records = FA4.objects.all()

    for fa1, fa2, fa3, fa4 in zip(fa1_records, fa2_records, fa3_records, fa4_records):
        eng_sum = fa1.eng + fa2.eng + fa3.eng + fa4.eng
        kan_sum = fa1.kan + fa2.kan + fa3.kan + fa4.kan
        hin_sum = fa1.hin + fa2.hin + fa3.hin + fa4.hin
        maths_sum = fa1.maths + fa2.maths + fa3.maths + fa4.maths
        sci_sum = fa1.sci + fa2.sci + fa3.sci + fa4.sci
        soc_sci_sum = fa1.soc_sci + fa2.soc_sci + fa3.soc_sci + fa4.soc_sci

        eng = round((eng_sum / 200) * 25)
        kan = round((kan_sum / 200) * 20)
        hin = round((hin_sum / 200) * 20)
        maths = round((maths_sum / 200) * 20)
        sci = round((sci_sum / 200) * 20)
        soc_sci = round((soc_sci_sum / 200) * 20)
        total = eng + kan + hin + maths + sci + soc_sci

        aggregated_record = {
            'slno': fa1.slno,
            'name': fa1.name,
            'fa1': {'eng': fa1.eng, 'kan': fa1.kan, 'hin': fa1.hin, 'maths': fa1.maths, 'sci': fa1.sci, 'soc_sci': fa1.soc_sci},
            'fa2': {'eng': fa2.eng, 'kan': fa2.kan, 'hin': fa2.hin, 'maths': fa2.maths, 'sci': fa2.sci, 'soc_sci': fa2.soc_sci},
            'fa3': {'eng': fa3.eng, 'kan': fa3.kan, 'hin': fa3.hin, 'maths': fa3.maths, 'sci': fa3.sci, 'soc_sci': fa3.soc_sci},
            'fa4': {'eng': fa4.eng, 'kan': fa4.kan, 'hin': fa4.hin, 'maths': fa4.maths, 'sci': fa4.sci, 'soc_sci': fa4.soc_sci},
            'eng_sum': eng_sum,
            'kan_sum': kan_sum,
            'hin_sum': hin_sum,
            'maths_sum': maths_sum,
            'sci_sum': sci_sum,
            'soc_sci_sum': soc_sci_sum,
            'eng': eng,
            'kan': kan,
            'hin': hin,
            'maths': maths,
            'sci': sci,
            'soc_sci': soc_sci,
            'total': total,
        }
        aggregated_records.append(aggregated_record)

    return render(request, 'aggregate_marks.html', {'aggregated_records': aggregated_records})

def export_aggregate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="aggregated_marks.csv"'

    writer = csv.writer(response)
    writer.writerow(['SL No', 'Name', 'English', 'Kannada', 'Hindi', 'Maths', 'Science', 'Social Science'])

    fa1_records = FA1.objects.all()
    fa2_records = FA2.objects.all()
    fa3_records = FA3.objects.all()
    fa4_records = FA4.objects.all()

    for fa1, fa2, fa3, fa4 in zip(fa1_records, fa2_records, fa3_records, fa4_records):
        eng_sum = fa1.eng + fa2.eng + fa3.eng + fa4.eng
        kan_sum = fa1.kan + fa2.kan + fa3.kan + fa4.kan
        hin_sum = fa1.hin + fa2.hin + fa3.hin + fa4.hin
        maths_sum = fa1.maths + fa2.maths + fa3.maths + fa4.maths
        sci_sum = fa1.sci + fa2.sci + fa3.sci + fa4.sci
        soc_sci_sum = fa1.soc_sci + fa2.soc_sci + fa3.soc_sci + fa4.soc_sci

        eng = round((eng_sum / 200) * 25)
        kan = round((kan_sum / 200) * 20)
        hin = round((hin_sum / 200) * 20)
        maths = round((maths_sum / 200) * 20)
        sci = round((sci_sum / 200) * 20)
        soc_sci = round((soc_sci_sum / 200) * 20)
        total = eng + kan + hin + maths + sci + soc_sci

        writer.writerow([fa1.slno, fa1.name])
        writer.writerow(['', 'FA1', fa1.eng, fa1.kan, fa1.hin, fa1.maths, fa1.sci, fa1.soc_sci])
        writer.writerow(['', 'FA2', fa2.eng, fa2.kan, fa2.hin, fa2.maths, fa2.sci, fa2.soc_sci])
        writer.writerow(['', 'FA3', fa3.eng, fa3.kan, fa3.hin, fa3.maths, fa3.sci, fa3.soc_sci])
        writer.writerow(['', 'FA4', fa4.eng, fa4.kan, fa4.hin, fa4.maths, fa4.sci, fa4.soc_sci])
        writer.writerow(['', 'Total', eng_sum, kan_sum, hin_sum, maths_sum, sci_sum, soc_sci_sum])
        writer.writerow(['', '25/20', eng, kan, hin, maths, sci, soc_sci])

    return response

# def register(request):
#     if request.method == 'POST':
#         form5 = TeacherRegistrationForm(request.POST)
#         if form5.is_valid():
#             form5.save()
#             return redirect('login')
#     else:
#         form5 = TeacherRegistrationForm()
#     return render(request, 'register.html', {'form5': form5})

# def login_view(request):
#     if request.method == 'POST':
#         form6 = AuthenticationForm(request, data=request.POST)
#         if form6.is_valid():
#             email = form6.cleaned_data.get('username')
#             password = form6.cleaned_data.get('password')
#             teacher = authenticate(request, email=email, password=password)
#             if teacher is not None:
#                 login(request, teacher)
#                 return redirect('login')
#     else:
#         form6 = AuthenticationForm()
#     return render(request, 'login.html', {'form6': form6})

# def logout_view(request):
#     logout(request)
#     return redirect('login')

def export_aggregate_pdf(request):
    # Fetch the data to be displayed in the PDF
    aggregated_records = []

    fa1_records = FA1.objects.all()
    fa2_records = FA2.objects.all()
    fa3_records = FA3.objects.all()
    fa4_records = FA4.objects.all()

    for fa1, fa2, fa3, fa4 in zip(fa1_records, fa2_records, fa3_records, fa4_records):
        eng_sum = fa1.eng + fa2.eng + fa3.eng + fa4.eng
        kan_sum = fa1.kan + fa2.kan + fa3.kan + fa4.kan
        hin_sum = fa1.hin + fa2.hin + fa3.hin + fa4.hin
        maths_sum = fa1.maths + fa2.maths + fa3.maths + fa4.maths
        sci_sum = fa1.sci + fa2.sci + fa3.sci + fa4.sci
        soc_sci_sum = fa1.soc_sci + fa2.soc_sci + fa3.soc_sci + fa4.soc_sci
    
        eng = round((eng_sum / 200) * 25)
        kan = round((kan_sum / 200) * 20)
        hin = round((hin_sum / 200) * 20)
        maths = round((maths_sum / 200) * 20)
        sci = round((sci_sum / 200) * 20)
        soc_sci = round((soc_sci_sum / 200) * 20)
        total = eng + kan + hin + maths + sci + soc_sci

        aggregated_record = {
            'slno': fa1.slno,
            'name': fa1.name,
            'fa1': {'eng': fa1.eng, 'kan': fa1.kan, 'hin': fa1.hin, 'maths': fa1.maths, 'sci': fa1.sci, 'soc_sci': fa1.soc_sci},
            'fa2': {'eng': fa2.eng, 'kan': fa2.kan, 'hin': fa2.hin, 'maths': fa2.maths, 'sci': fa2.sci, 'soc_sci': fa2.soc_sci},
            'fa3': {'eng': fa3.eng, 'kan': fa3.kan, 'hin': fa3.hin, 'maths': fa3.maths, 'sci': fa3.sci, 'soc_sci': fa3.soc_sci},
            'fa4': {'eng': fa4.eng, 'kan': fa4.kan, 'hin': fa4.hin, 'maths': fa4.maths, 'sci': fa4.sci, 'soc_sci': fa4.soc_sci},
            'eng_sum': eng_sum,
            'kan_sum': kan_sum,
            'hin_sum': hin_sum,
            'maths_sum': maths_sum,
            'sci_sum': sci_sum,
            'soc_sci_sum': soc_sci_sum,
            'eng': eng,
            'kan': kan,
            'hin': hin,
            'maths': maths,
            'sci': sci,
            'soc_sci': soc_sci,
            'total': total,
        }
        aggregated_records.append(aggregated_record)
    
    # Render the template with the data

    template_path = 'aggregate_marks_pdf.html'
    context = {'aggregated_records': aggregated_records}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="aggregated_marks.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


        