
import os
import requests
import google.generativeai as genai

from io import BytesIO
from PIL import Image

import tkinter as tk
import json
import re




def analyze_image():
  #url = 'https://www.elcarrocolombiano.com/wp-content/uploads/2021/09/20210015-Proyecto-Ley-Placas-Colombia-01-750x518.jpg'
  #url = 'https://i.ebayimg.com/images/g/5l4AAOSw5d1kGfQe/s-l1600.jpg'
  #url = https://bolivarense.com/wp-content/uploads/2022/01/PICO-Y-PLACA-CTG.jpg

  label_resumen.config(text="")
  url = entry.get()
  response = requests.get(url)

  if response.status_code == 200:
      # Leer los datos de la imagen en bytes
      image_data = response.content
      
      # Convertir los datos de la imagen en un objeto de imagen
      image = Image.open(BytesIO(image_data))
      
      # Mostrar la imagen (opcional)
      #image.show()

      model = genai.GenerativeModel('gemini-pro-vision')
      # response = model.generate_content(image)

      response = model.generate_content(["Determine si la imagen contiene un automovil con placa, si es afirmativo responda en formato json asi 'automovil': true, 'placa':'placa' de lo contrario responda {automivil: false, placa:''} ", image], stream=True)
      response.resolve()

      
      texto = response.text.replace('`', '')
      diccionario = json.loads(texto) 
      label_resumen.config(font=("Arial", 20))
      if (diccionario["automovil"]):
        if(re.sub(r"\s+", "", diccionario["placa"]) in placas_registradas):
          label_resumen.config(text="Puedes entrar", fg="green")
        else:
          label_resumen.config(text="No puedes entrar", fg="red")  
      else:
         label_resumen.config(text="No puedes entrar", fg="red")



def build_interfaz():
    root = tk.Tk()
    root.title("Puerta Automática")
    root.geometry("800x600")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - root.winfo_screenwidth()) / 2
    y = (screen_height - root.winfo_screenheight()) / 2

    root.geometry("+%d+%d" % (x,y))

    label_titulo = tk.Label(root, text="Imagen")
    label_titulo.grid(row=0, column=0, padx=5, pady=5)
    global label_resumen
    label_resumen = tk.Label(root, text="")
    label_resumen.grid(row=1, column=0, padx=5, pady=5,  columnspan=2)


    global entry
    entry = tk.Entry(root, width=100)
    entry.grid(row=0, column=1, padx=5, pady=5)

    boton_abrir = tk.Button(root, text="Seleccionar archivo", command= analyze_image)
    boton_abrir.grid(row=0, column=2, padx=5,pady=5)


    root.mainloop()


# Ruta al archivo PDF
filename = ""
GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

placas_registradas = ["JNU540","PEK287","LYR967"]
build_interfaz()


