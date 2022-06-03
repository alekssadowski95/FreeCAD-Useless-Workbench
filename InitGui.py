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

import FreeCAD
import FreeCADGui
import PartGui 

class UselessWorkbench(Workbench):

    MenuText = "Useless Workbench"
    ToolTip = "A description of the Useless workbench"
    Icon = os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "Useless", "circle-blue.svg")

    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
        import commands
        FreeCADGui.addCommand('Useless_Box_Command', commands.UselessBoxCommand())
        FreeCADGui.addCommand('UselessBox_On_Point_Command', commands.UselessBoxOnPointCommand())
        FreeCADGui.addCommand('Useless_Cylinder_Command', commands.UselessCylinderCommand())
        FreeCADGui.addCommand('Useless_Cylinder_Through_Line_Command', commands.UselessCylinderThroughLineCommand())
        FreeCADGui.addCommand('Useless_Square_Pipe_Along_Path_Command', commands.UselessSquarePipeAlongPathCommand())
        FreeCADGui.addCommand('Useless_Rectangle_Pipe_Along_Path_Command', commands.UselessRectanglePipeAlongPathCommand())
        FreeCADGui.addCommand('Useless_Circle_Pipe_Along_Path_Command', commands.UselessCirclePipeAlongPathCommand())
        FreeCADGui.addCommand('Useless_Rectangle_Grid_Command', commands.UselessRectangleGridCommand())
        
        # A list of command names created above
        self.uselesscommands = ["Useless_Box_Command"
            , "UselessBox_On_Point_Command"
            , "Useless_Cylinder_Command"
            , "Useless_Cylinder_Through_Line_Command"
            , "Useless_Square_Pipe_Along_Path_Command"
            , "Useless_Rectangle_Pipe_Along_Path_Command"
            , "Useless_Circle_Pipe_Along_Path_Command"
            , "Useless_Rectangle_Grid_Command"] 
        self.uselesscommands = ["Part_Cylinder"]
        self.appendToolbar("Useless Commands", self.uselesscommands) # creates a new toolbar with useless commands
        self.appendToolbar("Part Commands", self.partcommands) # creates a new toolbar with part commands
        self.appendMenu("Useless", self.uselesscommands) # creates a new menu with useless commands
        self.appendMenu("Part", self.partcommands) # creates a new menu with part commands

    def Activated(self):
        """This function is executed whenever the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("Useless commands", self.list) # add commands to the context menu

    def GetClassName(self): 
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"   

FreeCADGui.addWorkbench(UselessWorkbench())
