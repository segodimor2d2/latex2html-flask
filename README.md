# latex2html-flask

precisa ter o compliador de latex instalado para poder compilar o pdf

e poder usar o comando:
```bash
pdflatex document.txt
```

- poppler - para usar a lib pdf2image
- venv - para criar um ambiente virtual
- flask - para rodar o servidor
- watchdog - para monitorar o txt
- pdf2image - para converter o pdf para imagem e poder ven no html
```bash
python -m venv 01latex

sudo pacman -S poppler

pip install flask watchdog pdf2image
```
