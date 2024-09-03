from django.shortcuts import render ,redirect
from django.http import HttpResponse 
from visittrack_App.models import User , Addvisitor ,Dept 



#from visittrack_app.models import user

# Create your views here    #page route

def index(request):
    return render(request,'login.html',{})

def signup(request):
    return render(request,'signup.html',{})

def dashboard(request):
    id = request.session['user_id'] 
    obj =  Dept.objects.filter(u_id= id)
    obj1 =  Dept.objects.filter(u_id= id,active_id=1)
    obj2 =  Addvisitor.objects.filter( uid = id)
    obj3 =  Addvisitor.objects.filter(uid=id,active_id=1)
    a = len(obj)
    b = len(obj1)
    c = len(obj2)
    d = len(obj3)
    return render(request,'index.html',{'a':a , 'b' : b , 'c':c ,'d':d})


def newvisitor(request):
    user_id = request.session['user_id'] 
    data = Addvisitor.objects.all()
    data = Addvisitor.objects.filter(uid=user_id ,active_id=0)
    return render(request,'newvisitor.html',{'data':data})  

# def managevisitor(request):
#     return render(request,'managevisitor.html',{})

# def bwdate(request):
#     d1 = request.session['date_id']
#     d2 = request.session['date1_id']
#     msg = request.session['msg']
#     return render(request,'bwdate.html',{})

def deletevisitor(request):
    user_id = request.session['user_id'] 
    # data = Addvisitor.objects.all()
    data = Addvisitor.objects.filter(uid=user_id ,active_id=1)
    return render(request,'deletevisitor.html',{'data':data})                  
    

def managedept(request):
    user_id = request.session['user_id'] 
    data = Dept.objects.filter(u_id=user_id ,active_id=0 )
    return render(request,'managedept.html',{'data':data})  

def logout(request):
    return render(request,'login.html',{})

def restoredept(request):
    user_id = request.session['user_id']
    data = Dept.objects.filter(u_id=user_id ,active_id=1 )
    return render(request,'restoredept.html',{'data':data}) 
    

def profile(request): 
    id = request.session['user_id'] 
    obj = User.objects.get(uid=id)
    return render(request,'profile.html',{'data':obj})

def updateprofile(request):
    id = request.session['user_id']
    obj = User.objects.filter(uid=id)
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        add = request.POST.get('address')
        phone = request.POST.get('phoneno')
        pass1 = request.POST.get('tpass')

        if len(phone)==10:
            obj.update(name=name, email=email, address=add, phoneno=phone, password=pass1)
            return redirect('/profile')
        else:
            obj.update(name=name, email=email, address=add, phoneno="None", password=pass1)
            return redirect('/profile')
    else:
        return redirect('/dashboard')

            

            

    if len(obj)==1:
       if request.method=="POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          pass1 = request.POST.get('tpass')
          pass2 = request.POST.get('password')

          obj.update(name=name, email=email,  password=pass1)
          print("Data updated done")
          return redirect('/profile')
       else : 
           print("form method not match")  
    else:
        print('len not match')
        return redirect('/profile')




#**************************** ACTION ROUTE START ****************************

def storeUser(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('temail')
        pass1 = request.POST.get('tpass')
        pass2 = request.POST.get('tpass1')
        add = 'None'
        phone = 'None'
        if pass1==pass2:
          data = User(name=name, email=email, address=add, phoneno=phone, password=pass1)          
          data.save()
          print("All data stored")
          return redirect('/')
        else:
            print("Pass not match")
            return redirect('/signup')
    else:
        print("Something Error")
        return redirect('/signup')
    
def checkUser(request):
    if request.method=="POST":
        email = request.POST.get('temail')      
        pass1 = request.POST.get('tpass')
        
        data = User.objects.filter(email=email, password=pass1)
        data1 = User.objects.get(email=email, password=pass1)
        print(data1.uid)
        request.session['user_id'] = data1.uid      #store data in session
        print(len(data))

        if len(data)==1:
            print("Sharvari login Success")
            return redirect('/dashboard')     
        else:
         print("len not match")
         return redirect('/')
        #*************************************** VISITOR PART  ****************************************8
def storenewvisitor(request):
    user_id = request.session['user_id'] 
    if request.method == "POST" :
        fullname=request.POST.get("tfullname") 
        emailid=request.POST.get("temailid")
        phoneno=request.POST.get("tphoneno")
        address=request.POST.get("taddress")
        companyname=request.POST.get("tcompanyname")
        whometomeet=request.POST.get("twhometomeet")
        department=request.POST.get("tdepartment")
        reasontomeet=request.POST.get("treasontomeet")
        wheretomeet=request.POST.get("twheretomeet")
        datetomeet=request.POST.get("tdatetomeet")
        timetomeet=request.POST.get("ttimetomeet")   
       

        data = Addvisitor(fullname=fullname, emailid=emailid, phoneno=phoneno, address=address, companyname=companyname, \
                        whometomeet=whometomeet,  department=department, reasontomeet=reasontomeet, wheretomeet=wheretomeet,\
                        datetomeet= datetomeet,timetomeet=timetomeet ,uid=user_id)
      
        data.save()
        return redirect('/newvisitor')
    else:
         print('New visitor not added')
         return redirect('/newvisitor')

def view(request,vid):
    data = Addvisitor.objects.get(vid=vid)
    return render(request,'view.html',{'data' :data}) 

def view_update(request,vid):                       #update page route
    data = Addvisitor.objects.get(vid=vid)
    request.session['newvi_id'] = vid                     #store data in session
    return render(request,'update.html',{'data' :data}) 

def update_data(request):
    newvi_id = request.session['newvi_id'] 
    if request.method == "POST" :
        fullname=request.POST.get("tfullname") 
        emailid=request.POST.get("temailid")
        phoneno=request.POST.get("tphoneno") 
        address=request.POST.get("taddress")
        companyname=request.POST.get("tcompanyname")
        whometomeet=request.POST.get("twhometomeet") 
        department=request.POST.get("tdepartment")
        reasontomeet=request.POST.get("treasontomeet")
        wheretomeet=request.POST.get("twheretomeet")
        datetomeet=request.POST.get("tdatetomeet")
        timetomeet=request.POST.get("ttimetomeet")   
       

        data = Addvisitor.objects.filter( vid= newvi_id)  
        
        data.update( fullname= fullname, emailid=emailid, phoneno=phoneno, address=address, companyname=companyname, \
                        whometomeet=whometomeet,  department=department, reasontomeet=reasontomeet, wheretomeet=wheretomeet,\
                        datetomeet= datetomeet,timetomeet=timetomeet )
        return redirect('/newvisitor')
    else:
         print('New visitor not updated')
         return redirect('/newvisitor')
    
def delete_newvi(request,vid):
    data = Addvisitor.objects.filter(vid=vid)
    data.update(active_id = 1)
    print("visitor is deleted successfully")
    return redirect('/newvisitor')

def restore_newvi(request,vid):        #(means restore visitor)
    data = Addvisitor.objects.filter(vid=vid)
    data.update(active_id = 0)
    print("visitor is deleted successfully")
    return redirect('/deletevisitor')

def deleted_newvisitor(request,vid):        #(means restore visitor)
    data = Addvisitor.objects.filter(vid=vid)
    data.delete()
    print("visitor is deleted successfully")
    return redirect('/deletevisitor')


#****************************** DEPARTMENT PART **********************************************

def store_dept(request):
    user_id = request.session['user_id']
    if request.method == 'POST' :
        name = request.POST.get('name')

        data = Dept(name=name ,u_id=user_id)
        data.save()
        return redirect('/managedept')
    else:
       print('Department not added')
       return redirect('/managedept')

def viewdept(request, d_id):
    data = Dept.objects.get(d_id=d_id)
    return render(request,'viewdept.html',{'data':data})


def view_upd_dept(request, d_id):              #update page route
    data = Dept.objects.get(d_id=d_id)
    request.session['dept_id'] = d_id           #store data in session
    return render(request,'updatedept.html',{'data':data})

def update_dept(request):
   dept_id = request.session['dept_id'] 
   if request.method == 'POST' :
        name = request.POST.get('name')

        data = Dept.objects.filter(d_id=dept_id)
        data.update(name=name)
        return render(request,'updatedept.html',{'data':data})   
        #return redirect('/managedept')
   else:
       print('Department not get update')
       return redirect('/managedept')                   
    

def del_dept(request, d_id):
    data = Dept.objects.filter(d_id=d_id)
    data.update(active_id=1)
    print("Department is deleted successfully")
    return redirect('/managedept')    


def restore_department(request, d_id):
    data = Dept.objects.filter(d_id=d_id)
    data.update(active_id =0) 
    print("Department is deleted successfully")
    return redirect('/restoredept')        
    

def delete_department(request, d_id):
    data = Dept.objects.filter(d_id=d_id)
    data.delete()
    print("Department is deleted successfully")
    return redirect('/restoredept')        
    
      
 #***********************************************************************************************       















# def store_date(request):
#     if request.method=="POST":
#         fromdate=request.POST.get('tfromdate')
#         todate=request.POST.get('ttodate')
#         request.session['date_id'] =  fromdate
#         request.session['date1_id'] = todate
#         msg="show data"
#         request.session['msg'] = msg
#         print('show date')
#     return redirect('/bwdate')
    

    


    















































