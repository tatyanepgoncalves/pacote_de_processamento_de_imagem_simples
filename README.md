# Simple Image Processor

## 📌 Sobre o Projeto

O **Simple Image Processor** é um pacote Python simples para processamento de imagens, permitindo realizar operações como conversão para escala de cinza, aplicação de desfoque, redimensionamento e conversão para arrays NumPy.

## 🚀 Funcionalidades

- 📷 **Carregar imagens** (suporte a formatos comuns como JPG e PNG)
- 🎨 **Converter para escala de cinza**
- 🌫️ **Aplicar efeito de desfoque**
- 🔄 **Redimensionar imagens**
- 🧮 **Converter imagem para array NumPy**
- 💾 **Salvar imagens processadas**

## 📂 Estrutura do Projeto

```
simple_image_processor/
├── simple_image_processor/
│   ├── __init__.py
│   ├── processor.py
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
```

## 📦 Instalação

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/tatyanepgoncalves/pacote_de_processamento_de_imagem_simples
cd simple-image-processor
```

### 2️⃣ Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Instalar o Pacote

```bash
pip install -e .
```

## 🛠️ Uso

```python
from simple_image_processor import ImageProcessor

# Carregar imagem
img_proc = ImageProcessor("minha_imagem.jpg")

# Converter para escala de cinza
gray_image = img_proc.to_grayscale()
gray_image.show()

gray_image.save("imagem_cinza.jpg")
```

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo! 🚀

