from PyQt5.QtWidgets import QComboBox,QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout

class App_Gui(QWidget):

    def __init__(self, logic):
        super().__init__()

        #Se establecen las características de la ventana
        self.title = 'Graphics Vigilance'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        #Inicializamos la ventana principal
        self.GUI()
        #Asignamos el valor de la lógica
        self.logic = logic
        self.update_parameters()
   

    def update_parameters(self):
        initial = self.logic.input()
        self.txt_sub.setText("")
        self.txt_sheet.setCurrentText(initial["Excel sheet name"])
        self.txt_bands.setCurrentText(initial["Bands name or Channels name"])
        self.txt_group.setText(initial["Subject name"])
        self.txt_graphics.setCurrentText(initial["Graphics name"])

    
    def update_graphics(self):
        txt_subValue = self.txt_sub.text() 
        txt_sheetValue = self.txt_sheet.currentText() 
        txt_bandsValue = self.txt_bands.currentText() 
        txt_groupValue = self.txt_group.text() 
        txt_graphicsValue = self.txt_graphics.currentText() 
        self.logic.graph(txt_subValue,txt_sheetValue,txt_bandsValue,txt_groupValue,txt_graphicsValue)
    
    def GUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()

        self.label_sub = QLabel('Number of Subjects')
        self.txt_sub = QLineEdit()

        #Creamos las etiquetas y campos de texto de la materia la caja de materias
        self.label_sheet = QLabel('Excel sheet name')
        # creamos un desplegable
        self.txt_sheet = QComboBox()
        self.txt_sheet.addItems(["Channels","SBJ Post", "SBJ Global","SBJ 1ch","Reactivity Post","Reactivity Global","WDN1","WDN","WRD","Vertex","Relations Post","Relations Global","Relations 1ch","Qualitative","True_alpha","Rest_alpha"])
        self.label_bands = QLabel('Bands name or Channels name')
        self.txt_bands = QComboBox()
        self.txt_bands.addItems(["Fz, Cz, Pz, O1O2","alpha_theta", "alpha_deltatheta", "alpha_delta","alpha_theta","all_bands","reactivity","Ch_Post","BandsWDN1","BandsWDN","BandsWRD","Bipolar","alpha","alpha_1ch","alpha2","delta","theta","deltatheta","beta","gamma","all_ind_bands","Qualitative"])


        self.label_group = QLabel('Subject name')
        self.txt_group = QLineEdit()
        
        self.label_graphics = QLabel('Graphics name')
        self.txt_graphics =  QComboBox()
        self.txt_graphics.addItems(["Individual bands", "Qualitative", "Reactivity","Quantitative and Qualitative"])

    
        #Creamos la caja de materias
        self.box = QGroupBox("Parameters")
        distr_box = QGridLayout()
        self.box.setLayout(distr_box)

        #Creamos la caja de botones
        self.box_buttons = QGroupBox()
        distr_box_buttons = QHBoxLayout()
        self.box_buttons.setLayout(distr_box_buttons)
        
        #Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.box)
        self.distr_vertical.addWidget(self.box_buttons)
        
        #Definimos el distribuidor principal de la ventana             
        self.setLayout(self.distr_vertical)
        
        #Agregamos a la caja de materias las etiquetas
        distr_box.addWidget(self.label_sub, 0,0)
        distr_box.addWidget(self.label_sheet, 1,0)
        distr_box.addWidget(self.label_bands, 2,0)
        distr_box.addWidget(self.label_group, 3,0)
        distr_box.addWidget(self.label_graphics, 4,0)

        #Agregamos a la caja de materias los campos de texto
        distr_box.addWidget(self.txt_sub, 0,1)
        distr_box.addWidget(self.txt_sheet, 1,1)
        distr_box.addWidget(self.txt_bands, 2,1)
        distr_box.addWidget(self.txt_group, 3,1)
        distr_box.addWidget(self.txt_graphics, 4,1)
        
        #Creamos los botones para la caja de botones
        self.ok = QPushButton("Ok")
        
        #Agregamos los botones a la caja de botones
        distr_box_buttons.addWidget(self.ok)    

        #Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.box)
        self.distr_vertical.addWidget(self.box_buttons)
        
        #Definimos el distribuidor principal de la ventana             
        self.setLayout(self.distr_vertical)
        self.ok.clicked.connect(self.update_graphics)
        self.show()