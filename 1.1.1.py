import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


# import
class Mainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a tittel
        self.setWindowTitle("Hello Word!!")

        # set vartical layout
        # self.setLayout(qtw.QVBoxLayout())
        from_layout = qtw.QFormLayout()
        self.setLayout(from_layout)
        # add  stuff/widgets
        label_1 = qtw.QLabel("this  is a  cool Label row")
        label_1.setFont(qtg.QFont("helvetica", 24))
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # add  rows to app
        from_layout.addRow(label_1)
        from_layout.addRow("first name", f_name)
        from_layout.addRow("last name", label_1)
        from_layout.addRow(qtw.QPushButton("press me!",
                                           clicked=lambda: press_it()))

        #  creat a label
        # my_label = qtw.QLabel("pick something the list below:")

        #  change the font size of label
        # my_label.setFont(qtg.QFont('helvetica', 24))
        # self.layout().addWidget(my_label)

        # creat an entry box
        # my_entry = qtw.QLineEdit()
        # my_entry.setObjectName("name_field")
        # my_entry.setText("")
        # self.layout().addWidget(my_entry)

        # create an combo box
        # my_combo = qtw.QComboBox(self, editable = True, insertpolicy = qtw.QComboBox.InsertAtBottom)

        # creat an spin box
        # my_spin = qtw.QDoubleSpinBox(self,
        #             value = 10,
        #             maximum =100,
        #             minimum = 0,
        #             singleStep = 5.50,
        #             prefix = "#",
        #             suffix = "order")
        # chang font size of spinbox
        # my_spin.setFont(qtg.QFont('helvetica',18))

        # creat a textbox
        # my_text = qtw.QTextEdit(self,
        # plainText = "this is real text",
        # html = "<center><h1><em> Big Header Text!</em></h1></center>",
        #        acceptRichText = False,
        #        lineWrapMode = qtw.QTextEdit.FixedColumnWidth,
        #        lineWrapColumnOrWidth = 485,
        #        placeholderText = "hello world",
        #        readOnly = False,
        #       )

        # add Irem to th combo box (tittel)
        # -----------------------------
        # my_combo.addItem("ali","jalal")
        # my_combo.addItem("reza", 2)
        # my_combo.addItem("javad", qtw.QWidget)
        # my_combo.addItem("amir")
        # put combox on the screen
        # self.layout().addWidget()

        # create a button
        my_button = qtw.QPushButton("press me!",
                                    clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # show the app
        self.show()

        def press_it():
            label_1.setText(f"you clicked the button, {f_name}")

        # def press_it():
        #    my_label.setText(f"you Typed {()}! ")
        # my_text.setPlainText("you pressed the Button!")

        #   my_entry.setText("")


app = qtw.QApplication([])
mw = Mainwindow()

app.exec_()
