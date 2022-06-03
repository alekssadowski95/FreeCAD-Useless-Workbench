from PySide2.QtWidgets import QDialog, QDialogButtonBox, QDoubleSpinBox, QSpinBox, QPushButton

from uiloader import loadUi

import os


class UselessBoxWidget(QDialog):
    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)

        # load the ui file
        self.ui = loadUi( os.path.join(os.path.dirname(os.path.abspath(__file__)), 'useless-box-ui.ui'), 
            self, 
            workingDirectory = os.path.dirname(os.path.abspath(__file__)))

        # create aliases for ui elements
        self.width_x_spinbox = self.findChild(QDoubleSpinBox, 'width_x_spinbox')
        self.width_y_spinbox = self.findChild(QDoubleSpinBox, 'width_y_spinbox')
        self.height_x_spinbox = self.findChild(QDoubleSpinBox, 'height_z_spinbox')
        self.width_x_help_button = self.findChild(QPushButton, 'width_x_help_button')
        self.width_y_help_button = self.findChild(QPushButton, 'width_y_help_button')
        self.height_z_help_button = self.findChild(QPushButton, 'height_z_help_button')
        self.buttonBox = self.findChild(QDialogButtonBox, 'buttonBox')
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

class UselessBoxOnPointWidget(QDialog):
    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)

        # load the ui file
        self.ui = loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'useless-box-on-point-ui.ui'),
            self, 
            workingDirectory = os.path.dirname(os.path.abspath(__file__)))

        # create aliases for ui elements
        self.width_x_spinbox = self.findChild(QDoubleSpinBox, 'width_x_spinbox')
        self.width_y_spinbox = self.findChild(QDoubleSpinBox, 'width_y_spinbox')
        self.height_x_spinbox = self.findChild(QDoubleSpinBox, 'height_z_spinbox')
        self.point_help_button = self.findChild(QPushButton, 'point_help_button')
        self.width_x_help_button = self.findChild(QPushButton, 'width_x_help_button')
        self.width_y_help_button = self.findChild(QPushButton, 'width_y_help_button')
        self.height_z_help_button = self.findChild(QPushButton, 'height_z_help_button')
        self.buttonBox = self.findChild(QDialogButtonBox, 'buttonBox')
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

class UselessCylinderWidget(QDialog):
    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)

        # load the ui file
        self.ui = loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'useless-cylinder-ui.ui'),
            self, 
            workingDirectory = os.path.dirname(os.path.abspath(__file__)))

        # create aliases for ui elements
        self.diameter_spinbox = self.findChild(QDoubleSpinBox, 'diameter_spinbox')
        self.height_z_spinbox = self.findChild(QDoubleSpinBox, 'height_z_spinbox')
        self.diameter_help_button = self.findChild(QPushButton, 'diameter_help_button')
        self.height_z_help_button = self.findChild(QPushButton, 'height_z_help_button')
        self.buttonBox = self.findChild(QDialogButtonBox, 'buttonBox')
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)