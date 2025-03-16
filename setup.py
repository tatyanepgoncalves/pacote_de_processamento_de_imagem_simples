from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_image_processor",
    version="0.0.1",
    author="Tatyane Gonçalves",
    author_email="tatyanegoncalves023@gmail.com",
    description="Um pacote simples para processamento de imagens.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tatyanepgoncalves/pacote_de_processamento_de_imagem_simples"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)