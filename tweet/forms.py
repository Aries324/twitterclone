from django import forms


class TweetAddForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)

