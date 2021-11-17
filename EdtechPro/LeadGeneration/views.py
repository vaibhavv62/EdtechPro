from django.shortcuts import render, redirect
from .forms import LeadModelForm
from django.views.generic import DetailView

# Create your views here.
from .models import Lead


def generateLeadView(request):
    print("r.u.u",request.user)
    form = LeadModelForm(
        initial={
            'handled_by':request.user
        }
    )#BlankForm
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_leads')
    context = {'form':form}
    template_name = 'LeadGeneration/generate_lead.html'
    return render(request,template_name,context)

def showLeadsView(request):
    lead_objs = Lead.objects.all()
    context = {'leads':lead_objs}
    template_name = 'LeadGeneration/show_leads.html'
    return render(request,template_name,context)

def updateLeadView(request,leadid):
    lead = Lead.objects.get(id=leadid)
    form = LeadModelForm(instance=lead)#BlankForm
    if request.method == 'POST':
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('show_leads')
    context = {'form':form}
    template_name = 'LeadGeneration/generate_lead.html'
    return render(request,template_name,context)

class DetailLeadView(DetailView):
    model = Lead