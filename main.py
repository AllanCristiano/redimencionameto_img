# converter ui para python
# pyuic5 name.ui -o name.py
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from novo.design import Ui_MainWindow


# instance class
class App(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        # methods super class
        super().__init__(parent)
        super().setupUi(self)
        # chamada method open image
        self.btn_BuscarImg.clicked.connect(self.open_img)
        # chamada method para o click do btn
        self.btn_Redimencionar.clicked.connect(self.resize_image)
        # chamada do method para salva image
        self.salvar.clicked.connect(self.save_image)

    def open_img(self):
        # open caixa de dialogo para adicionar o endereço url a uma variavel
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'/home/',
            options=QFileDialog.DontUseNativeDialog
        )
        # add url da imagem no input
        self.input_Url_Img.setText(image)
        # create uma imagem original para nao alterar a imagem original
        self.original_img = QPixmap(image)
        # apresentar a imagem no label
        self.label_Image.setPixmap(self.original_img)
        # apresentar as dimençoes  da imagem no inputs de largura e altura
        self.input_Largura.setText(str(self.original_img.width()))
        self.input_Altura.setText(str(self.original_img.height()))

    def resize_image(self):
        # recebe a largura da imagem
        width = int(self.input_Largura.text())
        # cria uma nova imagem com base na largura
        self.nova_imagem = self.original_img.scaledToWidth(width)
        self.label_Image.setPixmap(self.nova_imagem)  # add imagem ao label
        # apresentar as novas dimençoes  da imagem no inputs de largura e altura
        self.input_Largura.setText(str(self.nova_imagem.width()))
        self.input_Altura.setText(str(self.nova_imagem.height()))

    def save_image(self):
        # add abre a caixa de  dialogo para salvar a nova imagem em uma variavel
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            r'/home/',
            options=QFileDialog.DontUseNativeDialog
        )
        # salva a imagem com formato preferido
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
