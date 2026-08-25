import os
from markitdown import MarkItDown

def convertir_archivos():
    md = MarkItDown()
    
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivos = os.listdir(directorio_actual)
    
    # Ahora acepta tanto PDFs como archivos de Word (.docx)
    archivos_validos = [a for a in archivos if a.lower().endswith(('.pdf', '.docx'))]
    
    if not archivos_validos:
        print("❌ No encontre ningun PDF o Word (.docx) en esta carpeta.")
        return
        
    for archivo in archivos_validos:
        ruta_origen = os.path.join(directorio_actual, archivo)
        nombre_base = os.path.splitext(archivo)[0]
        archivo_md = os.path.join(directorio_actual, f"{nombre_base}.md")
        
        print(f"🔄 Convertedor procesando: {archivo}...")
        try:
            resultado = md.convert(ruta_origen)
            with open(archivo_md, "w", encoding="utf-8") as f:
                f.write(resultado.text_content)
            print(f"✅ ¡Exito! Creado: {nombre_base}.md")
        except Exception as e:
            print(f"❌ Error al procesar {archivo}: {e}")

if __name__ == "__main__":
    convertir_archivos()