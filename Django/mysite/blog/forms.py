from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()  # default wideget is EmailField
    to = forms.EmailField()
    # each Field type has built-in widget with default value
    # but we override widget to tell django to render this field as texteara
    # instead of default input
    comments = forms.CharField(widget=forms.Textarea, required=False)
