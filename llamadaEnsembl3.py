import requests, sys
import json
import time
import sqlite3

def insertintoDB(jsonresults,id):
    try:
        #Se crea una variable para guardar la lista de los rs id alamacenados
        guardados = []
        #Conexión a la base de datos
        conn = sqlite3.connect('C:\\Users\\34622\\Documents\\OUC\\TFM\\Prácticas\\variantes.db')
        cursor = conn.cursor()
        #Definir variables para iterar sobre los resultados json
        start = ""
        end = ""
        chr = ""
        MAF = ""
        nombre = ""
        tipo = ""
        aleloREF = ""
        aleloALT = ""
        synonyms = ""
         # Verificar que el ID está presente en los resultados JSON
        if id[0] not in jsonresults:
            print(f"ID {id[0]} no encontrado en los resultados JSON.")
            return
        # Iterar sobre los resultados JSON
        
        valores = jsonresults[id[0]]
        mappings = valores['mappings']
        MAF = valores['MAF']
        if MAF is None:
            MAF = '0'
        nombre = valores['name']
        if not nombre in guardados: #Evitar duplicados
            for map in mappings:
                if map['coord_system'] == 'chromosome' and map['strand'] == 1:
                    start = map.get('start')
                    end = map.get('end')
                    chr = map.get('seq_region_name')
                    tipo = map.get('source')
                    aleloREF = map.get('ancestral_allele')
                    aleloALT = map.get('allele_string')
                    synonyms = map.get('synonyms')
            insert_query = f"INSERT INTO Variante(start,end,chr,MAF, nombre, tipo, aleloREF, aleloALT, synonyms) VALUES({start},{end},{chr},{MAF},'{nombre}','{tipo}','{aleloREF}','{aleloALT}','{synonyms}')"
            cursor.execute(insert_query)
            conn.commit()  # Realizar los cambios en la base de datos
            guardados.append(nombre)
    except sqlite3.Error as error:
        print("Error en la inserción de datos a la base de datos:","variantes", ":", error)
    finally:
        conn.close()

# Guardar los datos filtrados en un archivo JSON
#filtered_output_file_path = "C:/Users/34622/Documents/OUC/TFM/Prácticas/Outputstfm/filtered_data.json"

# Ruta del archivo.txt que contiene los identificadores de las variaciones genéticas
file_path = "C:/Users/34622/Documents/OUC/TFM/Prácticas/efo3761.txt"

# Leer los identificadores de variaciones genéticas desde el archivo de texto
with open(file_path, "r") as file:
    ids = [line.strip() for line in file]

server = "https://rest.ensembl.org"
ext = "/variation/homo_sapiens"
headers={ "Content-Type" : "application/json", "Accept" : "application/json"}

# Dividir la lista de identificadores de uno en uno
n=1
chunks = [ids[i:i + n] for i in range(0, len(ids), n)]
#print(chunks)
print(type(chunks))

# Iterar sobre cada parte y realizar la solicitud a la API de Ensembl
contador=1
for id in chunks:
    time.sleep(0.2)
    print(str(contador)+" "+str(id))
    contador += 1
    try:
        # Realiza la solicitud para cada chunk de ID
        r = requests.post(server + ext, headers=headers, json={"ids": id})
        r.raise_for_status()
        if r.status_code == 200:
            jsonresults = r.json()
            insertintoDB(jsonresults, id)
        else:
            print(f"Error {r.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud para los IDs:", id, e)
