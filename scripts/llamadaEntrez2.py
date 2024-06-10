from Bio import Entrez
from datetime import datetime
import sqlite3
import time




# Configuración del correo electrónico para Entrez
Entrez.email = "fonsmartap@gmail.com"


# Función para registrar errores en un archivo
def log_error(mensaje):
    with open("C:/Users/34622/Documents/OUC/TFM/Prácticas/problemas_entrez.log", "a") as log_file:
        log_file.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) +" " + mensaje + "\n")
        log_file.close()


# Función para insertar datos en la base de datos
def insertintoDB(start, end, loci, chr, nombre):
    try:
        
        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('C:\\Users\\34622\\Documents\\OUC\\TFM\\Prácticas\\variantes.db')
        cursor = conn.cursor()

        # Verificar si el nombre ya existe en la base de datos
        cursor.execute("SELECT COUNT(*) FROM Gen WHERE Nombre = ?", (nombre,))
        result = cursor.fetchone()
        
        if result[0] > 0:
            print(f"El gen {nombre} ya existe en la base de datos.")
            return
        

        sql = f"INSERT INTO Gen (start, end, loci, chr, Nombre) VALUES (?,?,?,?,?)"
        cursor.execute(sql, (start, end, loci, chr, nombre))
        conn.commit()
    except sqlite3.Error as error:
        mensaje_error = f"Error SQLite:{error}"
        print(f"Error: {error}")
        log_error(mensaje_error)
    finally:
        conn.close()



# Ruta del archivo que contiene los identificadores de las variaciones genéticas
file_path = "C:/Users/34622/Documents/OUC/TFM/Prácticas/efo3761_2.txt"


# Leer los identificadores de variaciones genéticas desde el archivo de texto
with open(file_path, "r") as file:
    ids = [line.strip() for line in file]


contador=0
for id_individual in ids:
    contador+=1
    print(f"{contador}:{id_individual}")
    time.sleep(0.2)
    print("despues de contador")
    try:
        record = Entrez.read(Entrez.elink(dbfrom="snp", id=",".join(id_individual).replace('rs', ''), db="gene"), validate=False)# Lee los rs del archivo, los concatena en un único texto y elimina "rs" de las variantes para buscarlo
      
        print("despues de record")
        Link = record[0]['LinkSetDb'][0]['Link']
       


        #Iterar sobre cada parte y realizar la solicitus a la API

        for ID in Link:
            try:
                
                print("despues de record")
                consulta = Entrez.esummary(db="gene", id=ID['Id'])
                leerconsulta = Entrez.read(consulta)            
                consulta.close()
                info_genes = leerconsulta['DocumentSummarySet']['DocumentSummary'][0]
                nombre = info_genes['Name']
                chr = info_genes['Chromosome']
                start = info_genes['GenomicInfo'][0]['ChrStart']
                end = info_genes['GenomicInfo'][0]['ChrStop']
                loci = info_genes['MapLocation']

                
                # Insertar los datos en la base de datos
                insertintoDB(start, end, loci, chr, nombre)
                print("Introducido en base de datos")
            except Exception as e:
                mensaje_error = f"Error al procesar ID:{ID}: {e}"
                print(mensaje_error)
                log_error(mensaje_error)
    except Exception as e:
        mensaje_error = f"Error al procesar id_individual {id_individual}: {e}"
        print(mensaje_error)
        log_error(mensaje_error)
        continue  # Pasar al siguiente rs en caso de error

    
            
