from flask import Flask, send_file, render_template
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from pdf2image import convert_from_path
import os

# Instancia o aplicativo Flask
app = Flask(__name__)

PDF_PATH = 'doctxt.pdf'
IMG_FOLDER = 'static/images/'

def convert_pdf_to_images():
    images = convert_from_path(PDF_PATH)

    for i, image in enumerate(images):
        image_path = os.path.join(IMG_FOLDER, f'page_{i}.png')
        image.save(image_path, 'png')

def compile_latex():
    subprocess.call(['pdflatex', 'doctxt.tex'])

class MyHandler(FileSystemEventHandler):
    """Classe que trata eventos de modificação de arquivo."""
    def on_modified(self, event):
        if event.src_path.endswith('.tex'):
            print("Arquivo .tex modificado, recompilando...")
            compile_latex()
            convert_pdf_to_images()

@app.route('/')
def serve_html():
    """Rota que serve a página HTML."""
    # Lista de imagens para exibir
    images = [f for f in os.listdir(IMG_FOLDER) if f.endswith('.png')]
    return render_template('index.html', images=images)

@app.route('/pdf')
def serve_pdf():
    """Rota que serve o PDF gerado a partir do LaTeX."""
    #return send_file('doctxt.pdf', as_attachment=True)
    return send_file('doctxt.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    # Configura o observador para monitorar alterações nos arquivos .tex
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        # Inicia o servidor Flask
        print("Servidor rodando em http://0.0.0.0:5000/")
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
