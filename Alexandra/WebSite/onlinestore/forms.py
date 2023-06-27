from django import forms
from .models import AlbumTitleSuggestion

class AlbumTitleSuggestionForm(forms.ModelForm):
    class Meta:
        model = AlbumTitleSuggestion
        fields = ['title']