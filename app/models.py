from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válidocopy
        if len(postData['title']) < 5:
            errors["title"] = "DATO OBLIGATORIO: Titulo debe tener al menos 5 caracteres"
        if len(postData['network']) < 3:
            errors["network"] = "DATO OBLIGATORIO: ID del canal debe tener al menos 2 caracteres"
        if len(postData['date']) < 1:
            errors["date"] = "DATO OBLIGATORIO: Indicar la fecha de la creacion del canal"
        if len(postData['description']) > 0 & len(postData['description']) < 10:
            errors["description"] = "ATENCION: Ingrese una descripcion de al menos 10 caracteres o dejar vacio"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"{self.title} - {self.network} - {self.date}"
    def __str__(self):
        return f"{self.title} - {self.network} - {self.date}"