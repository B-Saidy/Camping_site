from django import forms
from comments.models import Comment
class CommentForm(forms.Form):
     author = forms.CharField(widget = forms.HiddenInput)
     text = forms.CharField(widget = forms.Textarea)
     content_type = forms.CharField(widget = forms.HiddenInput)
     object_id = forms.IntegerField(widget = forms.HiddenInput)
