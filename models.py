import FreeCAD
import FreeCADGui
import Part

class UselessBox():
    def __init__(self, obj):
        self.Type = 'UselessBox'
        obj.Proxy = self
        obj.addProperty('App::PropertyLength', 'Width x', 'Dimensions', 'Box width in x direction').Width_x = 10.0
        obj.addProperty('App::PropertyLength', 'Width y', 'Dimensions', 'Box width in y direction').Width_y = 10.0
        obj.addProperty('App::PropertyLength', 'Height z', 'Dimensions', 'Box height in z direction').Height_z = 10.0

    def execute(self, obj):
        '''
        Called on document recompute
        '''
        pass

def create_useless_box():
    '''
    UselessBox object creation method
    '''
    # create a new document object
    obj = FreeCAD.ActiveDocument.addObject('Part::FeaturePython', 'UselessBox')
    # create a UselessBox object and connect it to the new document object
    UselessBox(obj)
    # define the view provider. Here the view provider is defined as the default one.
    obj.ViewObject.Proxy = 0
    # recompute the active document
    FreeCAD.ActiveDocument.recompute()
    # return the newly created custom FreeCAD document object
    return obj


class UselessBoxOnPoint():
    pass

class UselessCylinder():
    pass

class UselessCylinderThroughLine():
    pass

class UselessCirclePipeAlongPath():
    pass

class UselessSquarePipeAlongPath():
    pass

class UselessRectanglePipeAlongPath():
    pass

class UselessRectangleGrid():
    pass