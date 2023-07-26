import re

from django import forms
from  .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['message', 'tag_set', 'photo', 'is_public']

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message = re.sub(r'[a-zA-Z]+', '', message)
        return message