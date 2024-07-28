# latex2html-flask

Precisa ter o compilador de latex instalado para poder compilar o pdf e poder usar o comando:

```bash
pdflatex doc.txt
```
## Dependências
- poppler - para usar a lib pdf2image
- venv - para criar um ambiente virtual
- flask - para rodar o servidor
- watchdog - para monitorar o txt
- pdf2image - para converter o pdf para imagem e poder ver no html

```bash
python -m venv 01latex

sudo pacman -S poppler

pip install flask watchdog pdf2image
```

## para rodar o servidor
```bash
python app.py
```
## o servidor vai rodar no localhost:5000
http://192.168.15.11:5000

## para baixar o pdf compilado
http://192.168.15.11:5000/pdf
