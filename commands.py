class UselessBoxCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': 'circle-blue.svg',
                'Accel': "Ctrl+A",
                'MenuText': "UselessBox",
                'ToolTip': "This is the Useless Box"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("UselessBox activated")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

# The command must be "registered" with a unique name by calling its class.
FreeCADGui.addCommand('Useless_Box_Command', UselessBoxCommand())