Ejemplo para utilizar el modelo gemini-pro-vision de Gemini, el cual recibirá una foto para determinar si es un automovil y se identifica la placa. El sistema devolvera una respuesta con el formato {'automivil': true/false, 'placa:''}.
Con la respuesta, se validará si el numero de placa devuelto se encuentra registrado en la lista de placas, si está lo dejará entrar  sino le negara el ingreso.

Antes de ejecutar el programa, deberá:
1. Crear una API de Gemini, https://ai.google.dev/
2. Configurar en las variables de entorno del sistema operativo del PC, una variable llamada GOOGLE_API_KEY asigandole la llave generada.
