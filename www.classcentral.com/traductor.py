from bs4 import BeautifulSoup
import requests
import json
import os

# obtener el contenido del archivo HTML
ruta_archivo = 'C:/Users/nicol/OneDrive/Desktop/ClassCentral/www.classcentral.com/index.html'
if os.path.exists(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        html = f.read()
else:
    print(f'No se encontró el archivo HTML en la ruta especificada: {ruta_archivo}')
    exit()

# crear un objeto Beautiful Soup a partir del contenido HTML
soup = BeautifulSoup(html, 'html.parser')

# crear una función para traducir texto a un idioma específico
def translate_text(text, target_lang):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"en|{target_lang}"
    }
    response = requests.get(url, params=params)
    json_str = json.dumps(response.text)
    data = json.loads(json_str)
    data_dict = json.loads(data)
    print(data_dict)
    try:
        json_str = json.dumps(response.text)
        data = json.loads(json_str)
        data_dict = json.loads(data)
    except json.decoder.JSONDecodeError:
        return None

    if 'responseData' in data_dict and 'translatedText' in data_dict['responseData']:
        return data_dict['responseData']['translatedText']
    return None

# encontrar todos los elementos de texto y traducirlos a Hindi
for tag in soup.find_all(text=True):
    if tag.strip() and not tag.parent.name == 'a':
        try:
            texto_traducido = translate_text(tag, "hi")
            tag.replace_with(tag.replace(tag, texto_traducido))
        except json.decoder.JSONDecodeError:
            print(f'Error al traducir el siguiente texto: {tag}')
            continue

# escribir el HTML con el texto traducido en un nuevo archivo
ruta_archivo_traducido = 'C:/Users/nicol/OneDrive/Desktop/ClassCentral/www.classcentral.com/index_hi.html'
with open(ruta_archivo_traducido, 'w', encoding='utf-8') as f:
    f.write(str(soup))
