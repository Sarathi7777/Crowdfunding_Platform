# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Campaign, Pledge

from .forms import CampaignForm, PledgeForm




# campaigns/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'campaigns/home.html')








def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaigns/campaign_list.html', {'campaigns': campaigns})

def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'campaigns/campaign_detail.html', {'campaign': campaign})

def create_campaign(request):
    if request.method == "POST":
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.owner = request.user
            campaign.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'campaigns/create_campaign.html')

@login_required
def pledge_campaign(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == "POST":
        form = PledgeForm(request.POST)
        if form.is_valid():
            pledge = form.save(commit=False)
            pledge.user = request.user
            pledge.campaign = campaign
            pledge.save()
            campaign.current_amount += pledge.amount
            campaign.save()
            return redirect('campaign_detail', pk=pk)
    else:
        form = PledgeForm()
    return render(request, 'campaigns/pledge_campaign.html', {'form': form, 'campaign': campaign})
