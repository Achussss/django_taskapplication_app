from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,FormView
from tasks.forms import TaskForm,RegistrationForm,LoginForm
from tasks.models import Tasks
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout



class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})




class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("home")


class IndexView(TemplateView):
    template_name="index.html"


#localhost:8000/tasks/add
#get

class TaskCreateView(CreateView):

    template_name="task-add.html"
    form_class=TaskForm
    success_url=reverse_lazy("task-list")
    #def get(self,request,*args,**kw):
     #   form=TaskForm
      #  return render(request,"task-add.html",{"form":form})


    

    #def post(self,request,*args,**kw):
     #   form=TaskForm(request.POST)
      #  if form.is_valid():
       #     form.save()
        #    return redirect("task-create") 
        #else:
         #   return render(request,"task-add.html",{"form":form})   
                
#localhost:800/tasks/all

class TaskListView(ListView):
    model=Tasks
    template_name="task-list.html"
    context_object_name="todos"

    #def get(self,request,*args,**kw):
     #   qs=Tasks.objects.all()
      #  return render(request,"task-list.html",{"todos":qs})


#localhost:8000/tasks/1


class TaskDetailView(DetailView):
    model=Tasks
    template_name="task-detail.html"
    context_object_name="todo"
    pk_url_kwarg="id"


   # def get(self,request,*args,**kwargs):
    #    id=kwargs.get("id")
     #   qs=Tasks.objects.get(id=id)
      #  return render(request,"task-detail.html",{"todo":qs})



class TaskDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Tasks.objects.get(id=id).delete()
        return redirect("task-list")        

def sign_out(request,*args,**kw):
        logout(request)
        return redirect("signin")


# Create your views here.
