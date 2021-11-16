from django.shortcuts import render, redirect
from .forms import LeadModelForm

# Create your views here.
from .models import Lead


def generateLeadView(request):
    form = LeadModelForm()#BlankForm
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