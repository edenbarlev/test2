from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        labels = {"description": "שם הקובץ",
                  "document": "העלאת הקובץ עצמו",
                  "isittrue": "האם הקובץ מסוג אקסל?"
                  }
        fields = ('description', 'document', 'isittrue')
