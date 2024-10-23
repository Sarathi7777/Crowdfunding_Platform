from django import forms
from .models import Campaign, Pledge

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'description', 'goal_amount', 'end_date']

class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ['amount']





