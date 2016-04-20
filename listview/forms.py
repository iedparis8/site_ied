from django import forms
from listview.models import ListViewContactItem
from listview.utils import get_personnel
from django.conf import settings


class PersonnelForm(forms.ModelForm):

    person = forms.ChoiceField(required=True, label='IED Personnel')

    def __init__(self, *args, **kwargs):
        super(PersonnelForm, self).__init__(*args, **kwargs)
        persons = get_personnel()
        names = [(p['id'], p['prenom']+' '+p['nom']) for p in persons]
        names = sorted(names, key=lambda tup: tup[1])
        self.fields['person'].choices = names

    class Meta:
        model = ListViewContactItem
