import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("Este es un mensaje de depuración (no se verá con nivel INFO)")
logging.info("El programa inició correctamente")
logging.warning("Cuidado: esta acción puede ser riesgosa")
logging.error("Error: ocurrió un problema")
logging.critical("¡CRÍTICO! El sistema falló")