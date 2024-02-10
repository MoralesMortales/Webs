from django import forms
from .models import Post
    
class PostNameClass(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Post
        fields = ('title','description')
