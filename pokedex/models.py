from django.db import models

class trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    trainer = models.ForeignKey(trainer, on_delete=models.CASCADE, related_name='pokemons') 
    picture = models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)   
    def __str__(self):
        return self.name
