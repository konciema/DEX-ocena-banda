from django import forms


class BandForm(forms.Form):
    def __init__(self, dex_attributes={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in dex_attributes.items():
            v.insert(0, "*")
            choices = list(zip(v, v))
            self.fields[k] = forms.ChoiceField(
                choices=choices, widget=forms.Select(
                    attrs={"class": "form-control"})
            )


class BandFormMain(forms.Form):
    def __init__(self, dex_attributes={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in dex_attributes.items():
            choices = list(zip(v['choices'], v['choices']))
            self.fields[k] = forms.ChoiceField(
                choices=choices, widget=forms.Select(
                    attrs={"class": "form-control"}),
            )
