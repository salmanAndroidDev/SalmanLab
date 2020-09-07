from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()  # default wideget is EmailField
    to = forms.EmailField()
    # each Field type has built-in widget with default value
    # but we override widget to tell django to render this field as texteara
    # instead of default input
    comments = forms.CharField(widget=forms.Textarea, required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        # exclude = ('name', 'email', 'body') ---> You can exclude the list by uncommenting this
