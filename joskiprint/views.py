# Create your views here.
import email
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Order, UserDetails, PrintOptions, Pricing
from .forms import orderform, usersignupform
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'joskiprint/index.html')
    
def about(request):
    return render(request, 'joskiprint/about.html')

class userCreateview(CreateView):
    form_class=usersignupform
    template_name='joskiprint/usersignup.html'


    def form_valid(self, form):
        User.objects.create_user(email=self.request.POST['email'], username=self.request.POST['username'], password=self.request.POST['password'])
        return redirect('joskiprint:index')



class userDetails(CreateView):
    model=UserDetails
    fields='__all__'
    success_url=reverse_lazy('joskiprint:order')

    def get_initial(self):
        if self.request.user.is_authenticated:
            initial=super().get_initial()
            initial['email']=self.request.user.email
            initial['name']=self.request.user
            return initial
        return super().get_initial()
    
    def form_valid(self, form):
        self.request.session["username"]=self.request.POST['name']
        self.request.session['email']=self.request.POST['email']
        self.request.session['phone_no']=self.request.POST['phoneNumber']
        self.request.session['address']=self.request.POST['address']
        user_form=form.save()
        self.request.session['user_pk']=user_form.id
        return super().form_valid(form)   

    

class makeOrder(CreateView):  
    form_class=orderform
    success_url=reverse_lazy('joskiprint:printoptions')
    template_name='joskiprint/order_form.html'

    def form_valid(self, form):
        
        user=UserDetails.objects.get(
            name__exact=self.request.session["username"],
            email__exact=self.request.session["email"],
            phoneNumber__exact=self.request.session["phone_no"],
            address__exact=self.request.session["address"],
            pk=self.request.session['user_pk'],
        )
        order=form.save(commit=False)
        order.userDetails=user
        order.save()
        self.request.session['pk']= order.id
        return super().form_valid(form)
    

class printOptions(CreateView):
    model=PrintOptions
    fields='__all__'

    def form_valid(self, form):
        self.request.session['startpage']=self.request.POST['startPage']
        self.request.session['endpage']=self.request.POST['endpage']
        self.request.session['frontandback']=self.request.POST['frontAndBack']
        self.request.session['coloured']=self.request.POST['coloured']

        global order
        order=Order.objects.get(pk=self.request.session['pk'])
        order.printOptions=form.instance
        return super().form_valid(form)  
        
    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse('joskiprint:ordersuccess', kwargs={'pk':order.pk})
        else:
            return reverse('joskiprint:index')
            
class orderSuccessful(generic.DetailView):
    model=Order
    template_name="joskiprint/ordered.html"

class orderSuccesses(generic.ListView):
    model=Order
    template_name="joskiprint/ordersuccess.html"   

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('joskiprint:index')

        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Order.objects.filter(userDetails__email=self.request.user.email).order_by('-order_date')

class OrderUpdate(UpdateView):
    model=Order
    fields='__all__'
    success_url=reverse_lazy('joskiprint:successes')

class OrderDelete(DeleteView):
    model=Order
    success_url=reverse_lazy('joskiprint:successes')