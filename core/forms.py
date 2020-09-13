from django import forms
from django.core.exceptions import ValidationError
import re
from datetime import date
from core.models import Genre,Movie

def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')

class PastMonthField(forms.DateField):
    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError("only past dates allowed here")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month,day=1)


# class MovieForm(forms.Form):
#     title=forms.CharField(max_length=100)
#     genre = forms.ModelChoiceField(queryset=Genre.objects.all())
#     rating= forms.IntegerField(min_value=1,max_value=10)
#     released=PastMonthFiels()
#     description= forms.CharField(widget=forms.Textarea,required=False)

class MovieForm(forms.ModelForm):

    class Meta:
        model= Movie
        fields= '__all__'
        # fields=('title',
        #         'rating',
        #         'released',
        #         )
    title = forms.CharField(validators=[capitalized_validator])
    # genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = PastMonthField()
    # description = forms.CharField(widget=forms.Textarea, required=False)

    def clean_description(self):
        initial=self.cleaned_data['description']
        sentences=re.sub(r'\s*\.\s',',',initial).split(',')
        cleaned=','.join(sentence.capitalize() for sentence in sentences)
        return cleaned

    def clean(self):
        result=super().clean()
        if result['genre'].name =='comedy' and result['rating']>5:
            raise ValidationError("the best comedy is worth a 4.")
        return result


    # director=models.ForeignKey(Director,null=True,on_delete=models.SET_NULL)
    # countrys=models.ManyToManyField(Country,related_name='movie')