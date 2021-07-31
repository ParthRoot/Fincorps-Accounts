"""
fincorpsconsultancy@gmail.com
fincorps_consultancy123
fcc@123
"""

from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from .models import User
from fincorps_accounts. models import User, General_Ledger

# Create your views here.

#index page
def index(request):
    return render(request, "index.html")

#report page
def report(request):
    return render(request, "report.html")

#general ledger page
def gl(request):
    return render(request, "gl.html")

#home page
def home(request):
    return render(request, "home.html")

#add_account
def add_account(request):
    return render(request, "add_account.html")

#login
def login_ex(request):
    if 'user' in request.session:
        current_user = request.session['uname']
        parm = {'current_user':current_user}
        return render(request, "home.html", parm)
    else:
        return redirect('login')
    
    return render(request, "index.html")
    
def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        passw = request.POST.get('pass')
        
        check_user = User.objects.filter(username=uname, password = passw)
        
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:  
            message = "please enter valid username and password"
            return render(request, "index.html" ,{'msg' : message})
        
    return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('pass')
        
        if User.objects.filter(username=uname).count()>0:
            message = "user is already exist"
            return render(request, 'signup.html', {'msg':message})
        else:
            user = User(username=uname, password = passw)
            user.save()
            message = "user successfully register"
            return render(request, "index.html" ,{'msg' : message})
    else:
        return render(request, 'signup.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')


#data entry
def general_ledger_entry(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        accounts = request.POST.get('accounts')
        details = request.POST.get('details')
        debit = request.POST.get('debit')
        credit = request.POST.get('credit')

        
        #insert data in database
        
        ins = General_Ledger(date=date, accounts=accounts, details=details,debit=debit, credit=credit)
        ins.save()
        
        
        message = "Data insert successfully!!!"
        
        return render(request, "gl.html", {'msg':message})
    else:
        message = "Sorry some problem occured!!!!"
        return render(request, "gl.html", {'msg':message})
    
def retrive_gl_data(request):
    if request.method == 'POST':
        start_date = request.POST.get('sdate')
        end_date = request.POST.get('edate')
        account = request.POST.get('accounts')
        t = 0
        if start_date <= end_date:
            # filter data date wise
            #info = register_form.objects.order_by('add_date')
            info = General_Ledger.objects.filter(
                date__gte=start_date,  date__lte=end_date, accounts=account)
            
            t = 1
            
            total_credit = 0.0
            total_debit = 0.0
            for i in info:
                total_credit = total_credit + i.credit
                total_debit = total_debit + i.debit
                
            
            return render(request, 'report.html', {'info': info, "account":account, "sdate":start_date,"edate":end_date, "t":t, "total_credit":total_credit, "total_debit":total_debit})
            
        elif start_date > end_date:
            message = "please select date properly......!!!"
            return render(request, 'report.html', {'msg': message})

        else:
            message = "please select date properly......!!!"
            return render(request, 'report.html', {'msg': message})


    else:
        
        return redirect('report')
        
    

