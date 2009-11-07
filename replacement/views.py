# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from replacement import myForms
from models import ShipPrice, Ticket
from replacement.myForms import TicketForm
from django.template.context import RequestContext
import datetime

#TODO: simple news system for status updates
#TODO: more Code documentation

def index(request, action=None):
    if request.method == 'POST':
        ticketForm = myForms.TicketForm(request.POST)
        if ticketForm.is_valid():
            newTicket = Ticket(
                             issuer = request.user.username,
                             victim = ticketForm.cleaned_data['victim'],
                             ship = ticketForm.cleaned_data['ship'],
                             kbLink = ticketForm.cleaned_data['kbLink'],
                             notes = ticketForm.cleaned_data['notes'],
                             statusOpen = True,
                             #date_entry = datetime.datetime.now(),
                             date_closed = None,
                             )
            #print newTicket
            newTicket.save()
            return HttpResponseRedirect('.')
        else:
            print 'ticket error'
            return HttpResponseRedirect('.')
    else:
        ticketForm = myForms.TicketForm()
        rList = ShipPrice.objects.all()
        tList = Ticket.objects.all()
        loginForm = None
        if request.user and request.user.is_authenticated() and not request.user.is_anonymous():
            user = request.user
        else:
            user = None
            loginForm = myForms.LoginForm()
        return render_to_response('index.html', {
                                                'current_user':user,
                                                'loginForm':loginForm,
                                                'ticketForm':ticketForm,
                                                'rList':rList,
                                                'tList':tList,
                                                },
                                                context_instance=RequestContext(request))


def markTicket(request, ticketID):
    if request.user and request.user.is_staff:
        ticket = Ticket.objects.get(id=ticketID)
        ticket.statusOpen = False
        ticket.date_closed = datetime.datetime.now()
        ticket.save()
    #return HttpResponse(ticketID)
    return HttpResponseRedirect('/eve')

def deleteTicket(request, ticketID):
    if request.user and request.user.is_staff:
        ticket = Ticket.objects.get(id=ticketID)
        ticket.delete()
    return HttpResponseRedirect('/eve')

def registerUser(request):
    if request.method == 'POST':
        form = myForms.RegisterForm(request.POST)
        #handle user authentication and login
        if form.is_valid():
            name = form.cleaned_data['uNameField']
            pwd = form.cleaned_data['uPassField1']
            if form.cleaned_data['uMailField']:
                email = form.cleaned_data['uMailField']
            else:
                email = "no@mail.here"
            user = User.objects.create_user(name, email, pwd)
            user.groups.add('user')
            user.save()
            return HttpResponseRedirect('/eve')
        else:
            return render_to_response('register.html', {
                                                        'form':form,
                                                        },
                                                        context_instance=RequestContext(request))
    else:
        form = myForms.RegisterForm()
        return render_to_response('register.html', {
                                            'form':form,
                                            },
                                            context_instance=RequestContext(request))

def loginUser(request):
    if request.method == 'POST':
        form = myForms.LoginForm(request.POST)
        #handle user authentication and login
        if form.is_valid():
            print 'valid form'
            name = form.cleaned_data['uNameField']
            pwd = form.cleaned_data['uPassField']
            user = authenticate(username=name, password=pwd)
            if user is not None:
                if user.is_active:
                    response =  HttpResponseRedirect('.')
                    login(request, user)
                    return response
                else:#acc disabled
                    return HttpResponse('account disabled!')
            else:#wrong username or pass
                return HttpResponseRedirect('.')
        else:#invalid form
            print 'invalid form'
            return HttpResponseRedirect('.')
    #no post-request, show form
    else:
        form = myForms.LoginForm()
        return render_to_response('index,html', {
                                            'form':form,
                                            },
                                            context_instance=RequestContext(request))
        
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('.')