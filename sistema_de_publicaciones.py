from abc import ABC, abstractmethod
import time as tm

# Clase base para publicaciones
class Publicacion(ABC):
    def __init__(self, contenido):
        self.contenido = contenido
    
    @abstractmethod
    def publicar(self):
        pass
    
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def resumir(self):
        pass

    @abstractmethod
    def obtener_estadisticas(self):
        pass

# Publicación de imagen
class Imagen(Publicacion):
    def __init__(self, contenido, resolucion):
        super().__init__(contenido)
        self.resolucion = resolucion

    def publicar(self):
        print(f"Publicando imagen con resolucion {self.resolucion}...\n")
        tm.sleep(2)
    
        print("Espere 2 segundos se esta publicando la imagen...\n")
        tm.sleep(2)
    
        return"Imagen publicada con exito!\n"
    
    def info(self):
        return f"Nombre de la imagen: {self.contenido}\n"

    def resumir(self):
        return f"Resolucion de la imagen:{self.resolucion}\n"

    def obtener_estadisticas(self):
        return {"me gusta": 100,"comentarios:":10, "compartidos": 10}  # Simulación de estadísticas

# Publicación de video
class Video(Publicacion):
    def __init__(self, contenido, duracion):
        super().__init__(contenido)
        self.duracion = duracion

    def publicar(self):
        print(f"Publicando video con duracion {self.duracion}...\n")
        tm.sleep(2)
    
        print("Espere 2 segundos se esta publicando el video...\n")
        tm.sleep(2)
    
        return"Video publicado con exito!\n"
    
    
    def info(self):
        return f"Nombre del video: {self.contenido}\n"


    def resumir(self):
        return f"Video de duracion {self.duracion} segundos\n"

    def obtener_estadisticas(self):
        return {"vistas": 500,"comentario":4,"me gusta": 50}

# Publicación de enlace
class Enlace(Publicacion):
    def __init__(self, contenido, url):
        super().__init__(contenido)
        self.url = url

    def publicar(self):
        return f"Publicando enlace: {self.url}\n"
    
    def info(self):
        return f"Nombre del enlace: {self.contenido}\n"


    def resumir(self):
        return f"Enlace a {self.url}\n"

    def obtener_estadisticas(self):
        return "visitado por 200 usuarios"

# Ejemplo de uso
publicaciones = [
        #Imagen("Logo de Python", "1920x1080"),
        # Video("Tutorial de Python", 120),
        Enlace("Midudev portafolio", "https://porfolio.dev/")
]

for pub in publicaciones:
    print(pub.publicar())
    print(pub.info())
    print(pub.resumir())
    print(pub.obtener_estadisticas())
    print("-" * 30)
