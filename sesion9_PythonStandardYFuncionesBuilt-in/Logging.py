import logging
logging.basicConfig(level=logging.INFO)  # Aquí definimos el nivel de alerta mínimo para que se muestre en consola
# En caso de no poner esa línea, se mostrarán solo los warning, error y critical.
# Podemos definir a partir de cual se muestran con logging.basicConfig(level=logging.TIPODELOGGING)
# El orden es: DEBUG-> INFO-> WARNING-> ERROR-> CRITICAL  de menos a mas importante


print("La librería logging sirve para generar ficheros de registro:")

logging.info("Esto es un logging.info(): Arrancando programa")  # No se muestra en pantalla el nivel info,
# para que se muestre, linea 2.
logging.warning("Esto es un logging.warning()") # Los warning si se muestran aunque no implementemos lin 2
logging.error("Esto es un logging.error()")
logging.critical("Esto es un logging.critical()")

