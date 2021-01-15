
from django import forms

categories = [
    (None,'Select one...'),
    ('Fashion','Fashion'),
    ('Electronics','Electronics'),
    ('Home','Home'),
    ('Sports','Sports'),
    ('Toys','Toys'),
    ('Automobile','Automobile'),
    ('Books','Books'),
    ('Videogames','Videogames'),
    ('Others','Others')
]

class BidForm(forms.Form):
    bid_value = 0.00

    def __init__(self, bid_value,*args,**kwargs ):
        super().__init__(*args,**kwargs)
        self.bid_value = bid_value + 1
        self.fields['bid'].widget.attrs['min'] = self.bid_value 
 
    bid = forms.DecimalField(decimal_places=2)

class CreateForm(forms.Form):
    title = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder': 'title'}))
    desc= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'description'}))
    starting_bid= forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Starting bid'}))
    category = forms.ChoiceField(choices=categories)
    photo = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
            
