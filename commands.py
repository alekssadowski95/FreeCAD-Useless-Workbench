# ***************************************************************************
# *   Copyright (c) 2022 Aleksander Sadowski  www.alsado.de                 *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************/

import os

import FreeCADGui

from widgets import UselessBoxWidget, UselessBoxOnPointWidget, UselessCylinderWidget

class UselessBoxCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'circle-blue.svg'),
                'Accel': "Ctrl+A",
                'MenuText': "UselessBox",
                'ToolTip': "This is the Useless Box"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        main_window = FreeCADGui.getMainWindow()
        useless_box_dialog = UselessBoxWidget(main_window)
        useless_box_dialog.show()
        if useless_box_dialog.exec_():
            print('Success')
        else:
            print('Cancel')

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessBoxOnPointCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'circle-blue.svg'),
                'Accel': "Ctrl+S",
                'MenuText': "UselessBoxOnPoint",
                'ToolTip': "This is the Useless Box on a Point"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        main_window = FreeCADGui.getMainWindow()
        useless_box_dialog = UselessBoxOnPointWidget(main_window)
        useless_box_dialog.show()
        if useless_box_dialog.exec_():
            print('Success')
        else:
            print('Cancel')

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessCylinderCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'circle-blue.svg'),
                'Accel': "Ctrl+D",
                'MenuText': "UselessCylinder",
                'ToolTip': "This is the Useless Cylinder"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        main_window = FreeCADGui.getMainWindow()
        useless_box_dialog = UselessCylinderWidget(main_window)
        useless_box_dialog.show()
        if useless_box_dialog.exec_():
            print('Success')
        else:
            print('Cancel')

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessCylinderThroughLineCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'circle-blue.svg'),
                'Accel': "Ctrl+F",
                'MenuText': "UselessCylinderThroughLine",
                'ToolTip': "This is the Useless Cylinder through a Line"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("UselessCylinderThroughLine activated")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessSquarePipeAlongPathCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'circle-blue.svg'),
                'Accel': "Ctrl+G",
                'MenuText': "UselessSquarePipeAlongPath",
                'ToolTip': "This is the Useless Square Pipe along a Path"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("UselessSquarePipeAlongPath activated")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessRectanglePipeAlongPathCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'circle-blue.svg'),
                'Accel': "Ctrl+H",
                'MenuText': "UselessRectanglePipeAlongPath",
                'ToolTip': "This is the Useless Rectangle Pipe along a Path"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("UselessRectanglePipeAlongPath activated")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessCirclePipeAlongPathCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'circle-blue.svg'),
                'Accel': "Ctrl+J",
                'MenuText': "UselessCirclePipeAlongPath",
                'ToolTip': "This is the Useless Circle Pipe along a Path"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("UselessCirclePipeAlongPath activated")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessRectangleGridCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'circle-blue.svg'),
                'Accel': "Ctrl+K",
                'MenuText': "UselessRectangleGrid",
                'ToolTip': "This is the Useless Rectangle Grid"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("UselessRectangleGrid activated")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True