from django import forms

class TOPICFORM(forms.Form):
    topic_name=forms.CharField(max_length=100)