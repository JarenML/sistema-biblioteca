from django import forms
from .models import Categoria, Autor, Libro, Prestamo

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre[:3] != 'aa.':
            raise forms.ValidationError("El nombre debe comenzar con 'aa.'")
        return nombre
    
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={
                'type': 'date'
            })
        }


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'

        widgets = {
            'fecha_devolucion': forms.DateInput(
                attrs={'type': 'date'}),
            'fecha_prestamo': forms.DateInput(
                attrs={'readonly': 'True'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personalizar las etiquetas de las opciones
        self.fields['libro'].label_from_instance = lambda obj: f"{obj.titulo} {'(Disponible)' if obj.disponible else '(No disponible)'}"

    

    def clean(self):
        cleaned_data = super().clean()
        libro = cleaned_data.get('libro')
        devuelto = cleaned_data.get('devuelto')

       
        if not self.instance.pk and devuelto:
            raise forms.ValidationError("No puedes devolver el Libro en la creación del Prestamo")
        

        if not self.instance.pk or not (self.instance.libro == libro):
            if not libro.disponible and not devuelto:
                raise forms.ValidationError("Este libro ya se encuentra prestado")
        
        return cleaned_data