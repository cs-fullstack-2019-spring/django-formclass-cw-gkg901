from django import forms


class employeeApplicationForm(forms.Form):
    name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    position_applying_to = forms.CharField(max_length=50)
    salary = forms.IntegerField()
