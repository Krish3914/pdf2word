
from django.db.models import Model,FileField

# Create your models here.

class pdf_class(Model):
    pdf_name = FileField(upload_to='pdf_fol')

    def __str__(self) -> str:
        return self.pdf_name



