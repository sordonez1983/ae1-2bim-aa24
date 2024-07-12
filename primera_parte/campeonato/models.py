from django.db import models

class equipo_futbol(models.Model):
    nombre = models.CharField(max_length=30)
    colores = models.CharField(max_length=30)
    plantilla_jugadores = models.IntegerField()
    rentabilidad = models.IntegerField()
    estadio = models.CharField(max_length=100)

    def __str__(self): 
        return """Nombre: %s - Colores: %s \n     #representacion del objeto en determinada instancia
                Plantilla_jugadores: %d\n
                Rentabilidad: %d\n
                Estadio: %s""" % (self.nombre,
                self.colores,
                self.plantilla_jugadores,
                self.rentabilidad,
                self.estadio)