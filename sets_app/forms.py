import datetime

from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from sets_app.models import Boat, Rider

# TODO: use django.forms.ModelForm
class AddSetForm(forms.Form):
    date_set = forms.DateField(
        help_text="Enter the date of the set.",
        required=True,
        label="Date of set",
        initial=str(datetime.date.today()),
        widget=forms.DateInput,
    )

    duration = forms.FloatField(
        help_text="Enter duration of set.", required=True, label="Duration of set",
    )

    driver = forms.CharField(
        help_text="Enter name of driver.", required=True, label="Name of driver",
    )

    rider = forms.CharField(
        help_text="Enter name of rider.", required=True, label="Name of rider",
    )

    # rider = forms.ModelChoiceField(
    #     queryset=Rider.objects.all(),
    #     help_text="Enter rider's name.",
    #     required=True,
    #     label="Rider"
    # )

    boat = forms.ModelChoiceField(
        queryset=Boat.objects.all(),
        help_text="Enter boat used.",
        required=True,
        label="Boat",
    )

    def clean_duration(self):
        # getting clean data (using default validators)
        data = self.cleaned_data["duration"]

        # Check if duration is non-zero or negative value
        if data <= 0:
            raise ValidationError(
                _("Duration of set must be value larger than 0 minutes.")
            )

        # returning validated data
        return data

    def clean_rider(self):
        # TODO: check if rider exists in database, if not raise validationError
        data = self.cleaned_data["rider"]





class AddRiderModelFrom(ModelForm):

    class Meta:
        model = Rider
        fields = '__all__'
        DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
               '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
               '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
               '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
               '2012', '2013', '2014', '2015')
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=DOY)
        }



    def clean_first_name(self):
        data = self.cleaned_data['first_name']

        # check if first name field is empty
        if data == "":
            raise ValidationError(_("Invalid empty entry for first name"))

        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']

        # check if first name field is empty
        if data == "":
            raise ValidationError(_("Invalid empty entry for last name"))

        return data

