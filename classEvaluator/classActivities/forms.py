from ctypes.wintypes import SIZE
from django import forms


class ActivityForm(forms.Form):
    name = forms.CharField(label="Activity name", max_length=100)
    available_from = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    available_until = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )
    grade_scale = forms.IntegerField(label="Grade scale", max_value=100, min_value=0)
    subject = forms.IntegerField(widget=forms.HiddenInput())


class SubjectForm(forms.Form):
    name = forms.CharField(label="Subject name", max_length=100, required=True)
    author = forms.IntegerField(widget=forms.HiddenInput())
