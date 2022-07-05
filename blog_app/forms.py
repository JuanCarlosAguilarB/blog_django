from django import forms 

# importación de modelos que vamos a utilizar 
from .models import Post

# clase que se encargará del formulario
class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post  # modelo que estamos editando
        fields = ('title','content')   # nombre de los campos del modelo que vamos a modificar 

    ### ya con el formulario listo, lo mandamos a la vista 
