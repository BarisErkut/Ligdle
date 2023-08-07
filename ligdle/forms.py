from django import forms

class PlayerSearchForm(forms.Form):
    player_name = forms.CharField(label='Oyuncu adı girin')