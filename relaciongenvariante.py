import sqlite3
from Bio import Entrez
import time


# Configuración del correo electrónico para Entrez
Entrez.email = "fonsmartap@gmail.com"

def obtenervariantes():
    try:
     # Conectar a la base de datos SQLite
        conn = sqlite3.connect('C:\\Users\\34622\\Documents\\OUC\\TFM\\Prácticas\\variantes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM variante")
        resultado = cursor.fetchall()
        return resultado
    except:
        print("error")
        return "error"
    finally:
        conn.close()


listavariantes = obtenervariantes()

def obtenergenes(variante):
    try:
        record = Entrez.read(Entrez.elink(dbfrom="snp", id=",".join(variante).replace('rs', ''), db="gene"), validate=False)
        time.sleep(0.2)
        genID = record[0]['LinkSetDb'][0]['Link'][0]['Id']
        handle = Entrez.esummary(db="gene", id=genID)
        uid_record = Entrez.read(handle)
        info_genes = uid_record['DocumentSummarySet']['DocumentSummary'][0]
        nombre = info_genes['Name']
        handle.close()
        return (nombre)
    except:
        return("error")

def obtenergenID(nombre2):
    try:
     # Conectar a la base de datos SQLite
        conn = sqlite3.connect('C:\\Users\\34622\\Documents\\OUC\\TFM\\Prácticas\\variantes.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT ID_GEN FROM Gen WHERE NOMBRE = {nombre2}")
        resultado = cursor.fetchone()
        return resultado
    except:
        return "error"
    finally:
        conn.close()

for variante in listavariantes:
    gen = obtenergenes(variante[0])
    #print((variante))
    if not gen == "error":
        genID = obtenergenID(gen)
        print(variante[0] + " "+ gen+ " " +genID)
        #updatevariante(variante, genID)
    else:
        continue

