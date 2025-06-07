""" QApplication e QPushButton de Pyside6.QtWidgets"""
#QApplication -> Widget principal da aplicação
#QPushButton -> Um botão
#PySide6.QtWidgets -> Onde estão os widgets do Pyside6
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app= QApplication(sys.argv) # renderiza um widgets por janela   
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Minha Janela Bonita")

botao = QPushButton('Texto do Botao')
botao.setStyleSheet('font-size: 40px;')
# botao.show()

# Dessa forma os botões geram duas janelas
botao2 = QPushButton('Texto do Botao') 
botao2.setStyleSheet('font-size: 40px;')
# botao2.show()

botao3 = QPushButton('Texto do Botao') 
botao3.setStyleSheet('font-size: 40px;')
# botao2.show()

layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2)
layout.addWidget(botao3, 3, 1, 1, 2) # Expandido o botão para duas colunas

# statusBar

status_bar = window.statusBar()
status_bar.showMessage('Mensagem de Status')

# menuBar
menu = window.menuBar()
# menu.addMenu('Qualquer coisa')
primeiro_menu = menu.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('Primeira Ação')

# Introdução de Sinal e Slot
# def slot_example():
    # print("Teste de acao")
@Slot()
def slot_example(status_bar):
    status_bar.showMessage("Slot executado")
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

@Slot()
def outro_slot(cheked):
    print('Está amarcado?', cheked)

def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


segunda_acao = primeiro_menu.addAction('Segunda Ação')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

botao.clicked.connect(terceiro_slot(segunda_acao))

window.show()
app.exec()

