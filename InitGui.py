class UselessWorkbench(Workbench):

    MenuText = "Useless Workbench"
    ToolTip = "A description of the Useless workbench"
    Icon = """  
            /* XPM */
            static char *XPM_example[] = {
            "24 20 3 1 12 10 XPMEXT",
            "  c None",
            ". c #0000FF",
            "+ c #FF0000",
            "                        ",
            "    ..                  ",
            "   ....                 ",
            "  ......++++++++        ",
            " .........+++++++       ",
            " ..........+++++++      ",
            " ............++++++     ",
            " .............++++++    ",
            "  ..............++++    ",
            "   +.............+++    ",
            "   ++.............++    ",
            "   +++.............+    ",
            "   +++++.............   ",
            "   ++++++.............. ",
            "   ++++++++............ ",
            "   +++++++++........... ",
            "    +++++++++.........  ",
            "     ++++++++++.......  ",
            "      ++++++++++.....   ",
            "       +++++++++ ...    ",
            "XPMEXT author Anonymous",
            "XPMEXT address",
            "Beispielweg 42a",
            "0815 Beispielstadt",
            "LUMMERLAND",
            "mailto:anonymous@beispielstadt.lum",
            "XPMENDEXT"
            };
            """

    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
        import commands # import here all the needed files that create your FreeCAD commands
        self.list = ["Useless_Box_Command"] # A list of command names created in the line above
        self.appendToolbar("Useless Commands", self.list) # creates a new toolbar with your commands
        self.appendMenu("Useless New Menu", self.list) # creates a new menu
        self.appendMenu(["An existing Menu", "My submenu"], self.list) # appends a submenu to an existing menu

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

import FreeCADGui       
FreeCADGui.addWorkbench(UselessWorkbench())
print("Initializing Useless workbench GUI.")