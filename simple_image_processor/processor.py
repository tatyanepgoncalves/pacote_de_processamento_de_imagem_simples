from PIL import Image, ImageFilter
import numpy as np

class ImageProcessor:
  def __init__(self, image_path):
    self.image = Image.open(image_path)

  def to_grayscale(self):
    """Converte a imagem para escala de cinza."""
    return self.image.convert("L")
  
  def apply_blur(self):
    """Aplica desfoque na imagem."""
    return self.image.filter(ImageFilter.BLUR)
  
  def to_numpy(self):
    """Retorna a imagem como array numpy."""
    return np.array(self.image)
  
  def save(self, output_path):
    """Salva a imagem processada."""
    return self.image.save(output_path)