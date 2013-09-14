'''
Created on 14.09.2013

@author: Emre Tekinalp
'''

from maya import cmds


class Node(object):
    """
    This class creates and contains any kind of existing nodes in maya
    """
    def __init__(self):
        pass
    #end def __init__():

    def addDoubleLinear(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('addDoubleLinear', name = name + "_" + suffix)
            else:
                cmds.createNode('addDoubleLinear', name = name + "_ADL")
        else:
            cmds.createNode('addDoubleLinear')
    #end def addDoubleLinear()

    def addMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('addMatrix', name = name + "_" + suffix)
            else:
                cmds.createNode('addMatrix', name = name + "_AMX")
        else:
            cmds.createNode('addMatrix')
    #end def addMatrix()

    def angleBetween(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('angleBetween', name = name + '_' + suffix)
            else:
                cmds.createNode('angleBetween', name = name + '_ABW')
        else:
            cmds.createNode('angleBetween')
    #end def angleBetween()

    def arrayMapper(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('arrayMapper', name = name + '_' + suffix)
            else:
                cmds.createNode('arrayMapper', name = name + '_AMP')
        else:
            cmds.createNode('arrayMapper')
    #end def arrayMapper()

    def blendColors(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('blendColors', name = name + '_' + suffix)
            else:
                cmds.createNode('blendColors', name = name + '_BLC')
        else:
            cmds.createNode('blendColors')
    #end def blendColors()

    def blendTwoAttr(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('blendTwoAttr', name = name + '_' + suffix)
            else:
                cmds.createNode('blendTwoAttr', name = name + '_BTA')
        else:
            cmds.createNode('blendTwoAttr')
    #end def blendTwoAttr()

    def bump2d(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('bump2d', name = name + '_' + suffix)
            else:
                cmds.createNode('bump2d', name = name + '_B2D')
        else:
            cmds.createNode('bump2d')
    #end def bump2d()

    def bump3d(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('bump3d', name = name + '_' + suffix)
            else:
                cmds.createNode('bump3d', name = name + '_B3D')
        else:
            cmds.createNode('bump3d')
    #end def bump3d()

    def closestPointOnMesh(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('closestPointOnMesh', name = name + '_' + suffix)
            else:
                cmds.createNode('closestPointOnMesh', name = name + '_CPM')                
        else:
            cmds.createNode('closestPointOnMesh')
    #end def closestPointOnMesh()

    def closestPointOnSurface(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('closestPointOnSurface', name = name + '_' + suffix)
            else:
                cmds.createNode('closestPointOnSurface', name = name + '_CPS')
        else:
            cmds.createNode('closestPointOnSurface')
    #end def closestPointOnSurface()

    def choice(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('choice', name = name + '_' + suffix)
            else:
                cmds.createNode('choice', name = name + '_CHO')
        else:
            cmds.createNode('choice')
    #end def choice()

    def chooser(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('chooser', name = name + '_' + suffix)
            else:
                cmds.createNode('chooser', name = name + '_CHU')
        else:
            cmds.createNode('chooser')
    #end def chooser()

    def clamp(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('clamp', name = name + '_' + suffix)
            else:
                cmds.createNode('clamp', name = name + '_CMP')                
        else:
            cmds.createNode('clamp')
    #end def clamp()

    def colorProfile(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('colorProfile', name = name + '_' + suffix)
            else:
                cmds.createNode('colorProfile', name = name + '_CPR')
        else:
            cmds.createNode('colorProfile')
    #end def colorProfile()

    def composeMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('composeMatrix', name = name + '_' + suffix)
            else:
                cmds.createNode('composeMatrix', name = name + '_CMX')
        else:
            cmds.createNode('composeMatrix')
    #end def composeMatrix()

    def condition(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('condition', name = name + '_' + suffix)
            else:
                cmds.createNode('condition', name = name + '_CND')
        else:
            cmds.createNode('condition')
    #end def condition()

    def contrast(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('contrast', name = name + '_' + suffix)
            else:
                cmds.createNode('contrast', name = name + '_CON')                
        else:
            cmds.createNode('contrast')
    #end def contrast()

    def curveInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('curveInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('curveInfo', name = name + '_CIN')
        else:
            cmds.createNode('curveInfo')
    #end def curveInfo()

    def decomposeMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('decomposeMatrix', name = name + '_' + suffix)
            else:
                cmds.createNode('decomposeMatrix', name = name + '_DCM')
        else:
            cmds.createNode('decomposeMatrix')
    #end def decomposeMatrix()

    def distanceBetween(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('distanceBetween', name = name + '_' + suffix)
            else:
                cmds.createNode('distanceBetween', name = name + '_DIB')
        else:
            cmds.createNode('distanceBetween')
    #end def distanceBetween()

    def doubleSwitch(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('doubleSwitch', name = name + '_' + suffix)
            else:
                cmds.createNode('doubleSwitch', name = name + '_DSW')
        else:
            cmds.createNode('doubleSwitch')
    #end def doubleSwitch()

    def frameCache(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('frameCache', name = name + '_' + suffix)
            else:
                cmds.createNode('frameCache', name = name + '_FRC')                
        else:
            cmds.createNode('frameCache')
    #end def frameCache()

    def gammaCorrect(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('gammaCorrect', name = name + '_' + suffix)
            else:
                cmds.createNode('gammaCorrect', name = name + '_GMC')
        else:
            cmds.createNode('gammaCorrect')
    #end def gammaCorrect()

    def heightField(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('heightField', name = name + '_' + suffix)
            else:
                cmds.createNode('heightField', name = name + '_HFI')
        else:
            cmds.createNode('heightField')
    #end def heightField()

    def hsvToRgb(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('hsvToRgb', name = name + '_' + suffix)
            else:
                cmds.createNode('hsvToRgb', name = name + '_H2R')
        else:
            cmds.createNode('hsvToRgb')
    #end def hsvToRgb()

    def inverseMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('inverseMatrix', name = name + '_' + suffix)
            else:
                cmds.createNode('inverseMatrix', name = name + '_INM')
        else:
            cmds.createNode('inverseMatrix')
    #end def inverseMatrix()

    def lightInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('lightInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('lightInfo', name = name + '_LIN')
        else:
            cmds.createNode('lightInfo')
    #end def lightInfo()

    def luminance(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('luminance', name = name + '_' + suffix)
            else:
                cmds.createNode('luminance', name = name + '_LUM')
        else:
            cmds.createNode('luminance')
    #end def luminance()

    def multDoubleLinear(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('multDoubleLinear', name = name + '_' + suffix)
            else:
                cmds.createNode('multDoubleLinear', name = name + '_MDL')
        else:
            cmds.createNode('multDoubleLinear')
    #end def multDoubleLinear()

    def multiplyDivide(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('multiplyDivide', name = name + '_' + suffix)
            else:
                cmds.createNode('multiplyDivide', name = name + '_MLT')
        else:
            cmds.createNode('multiplyDivide')
    #end def multiplyDivide()

    def nearestPointOnCurve(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('nearestPointOnCurve', name = name + '_' + suffix)
            else:
                cmds.createNode('nearestPointOnCurve', name = name + '_NPC')
        else:
            cmds.createNode('nearestPointOnCurve')
    #end def nearestPointOnCurve()

    def particleSampler(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('particleSampler', name = name + '_' + suffix)
            else:
                cmds.createNode('particleSampler', name = name + '_PSA')
        else:
            cmds.createNode('particleSampler')
    #end def particleSampler()

    def place2dTexture(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('place2dTexture', name = name + '_' + suffix)
            else:
                cmds.createNode('place2dTexture', name = name + '_P2T')
        else:
            cmds.createNode('place2dTexture')
    #end def place2dTexture()

    def place3dTexture(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('place3dTexture', name = name + '_' + suffix)
            else:
                cmds.createNode('place3dTexture', name = name + '_P3T')
        else:
            cmds.createNode('place3dTexture')
    #end def place3dTexture()

    def plusMinusAverage(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('plusMinusAverage', name = name + '_' + suffix)
            else:
                cmds.createNode('plusMinusAverage', name = name + '_PMA')
        else:
            cmds.createNode('plusMinusAverage')
    #end def plusMinusAverage()

    def pointMatrixMult(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('pointMatrixMult', name = name + '_' + suffix)
            else:
                cmds.createNode('pointMatrixMult', name = name + '_PMM')
        else:
            cmds.createNode('pointMatrixMult')
    #end def pointMatrixMult()

    def pointOnCurveInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('pointOnCurveInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('pointOnCurveInfo', name = name + '_PCI')
        else:
            cmds.createNode('pointOnCurveInfo')
    #end def pointOnCurveInfo()

    def pointOnSurfaceInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('pointOnSurfaceInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('pointOnSurfaceInfo', name = name + '_PSI')
        else:
            cmds.createNode('pointOnSurfaceInfo')
    #end def pointOnSurfaceInfo()

    def pointOnPolyConstraint(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('pointOnPolyConstraint', name = name + '_' + suffix)
            else:
                cmds.createNode('pointOnPolyConstraint', name = name + '_PPC')
        else:
            cmds.createNode('pointOnPolyConstraint')
    #end def pointOnPolyConstraint()

    def projection(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('projection', name = name + '_' + suffix)
            else:
                cmds.createNode('projection', name = name + '_PRJ')
        else:
            cmds.createNode('projection')
    #end def projection()

    def quadSwitch(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('quadSwitch', name = name + '_' + suffix)
            else:
                cmds.createNode('quadSwitch', name = name + '_QSW')
        else:
            cmds.createNode('quadSwitch')
    #end def quadSwitch()

    def remapColor(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('remapColor', name = name + '_' + suffix)
            else:
                cmds.createNode('remapColor', name = name + '_RMC')
        else:
            cmds.createNode('remapColor')
    #end def remapColor()

    def remapHsv(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('remapHsv', name = name + '_' + suffix)
            else:
                cmds.createNode('remapHsv', name = name + '_RMH')
        else:
            cmds.createNode('remapHsv')
    #end def remapHsv()

    def remapValue(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('remapValue', name = name + '_' + suffix)
            else:
                cmds.createNode('remapValue', name = name + '_RMV')
        else:
            cmds.createNode('remapValue')
    #end def remapValue()

    def reverse(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('reverse', name = name + '_' + suffix)
            else:
                cmds.createNode('reverse', name = name + '_REV')
        else:
            cmds.createNode('reverse')
    #end def reverse()

    def rgbToHsv(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('rgbToHsv', name = name + '_' + suffix)
            else:
                cmds.createNode('rgbToHsv', name = name + '_R2H')
        else:
            cmds.createNode('rgbToHsv')
    #end def rgbToHsv()

    def samplerInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('samplerInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('samplerInfo', name = name + '_SMP')
        else:
            cmds.createNode('samplerInfo')
    #end def samplerInfo()

    def setRange(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('setRange', name = name + '_' + suffix)
            else:
                cmds.createNode('setRange', name = name + '_SRA')
        else:
            cmds.createNode('setRange')
    #end def setRange()

    def singleSwitch(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('singleSwitch', name = name + '_' + suffix)
            else:
                cmds.createNode('singleSwitch', name = name + '_SSW')
        else:
            cmds.createNode('singleSwitch')
    #end def singleSwitch()

    def stencil(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('stencil', name = name + '_' + suffix)
            else:
                cmds.createNode('stencil', name = name + '_STE')
        else:
            cmds.createNode('stencil')
    #end def stencil()

    def surfaceInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('surfaceInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('surfaceInfo', name = name + '_SFI')
        else:
            cmds.createNode('surfaceInfo')
    #end def surfaceInfo()

    def surfaceLuminance(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('surfaceLuminance', name = name + '_' + suffix)
            else:
                cmds.createNode('surfaceLuminance', name = name + '_SLU')
        else:
            cmds.createNode('surfaceLuminance')
    #end def surfaceLuminance()

    def transposeMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('transposeMatrix', name = name + '_' + suffix)
            else:
                cmds.createNode('transposeMatrix', name = name + '_TMX')
        else:
            cmds.createNode('transposeMatrix')
    #end def transposeMatrix()

    def tripleSwitch(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('tripleSwitch', name = name + '_' + suffix)
            else:
                cmds.createNode('tripleSwitch', name = name + '_TRI')
        else:
            cmds.createNode('tripleSwitch')
    #end def tripleSwitch()

    def unitConversion(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('unitConversion', name = name + '_' + suffix)
            else:
                cmds.createNode('unitConversion', name = name + '_UNI')
        else:
            cmds.createNode('unitConversion')
    #end def unitConversion()

    def vectorProduct(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('vectorProduct', name = name + '_' + suffix)
            else:
                cmds.createNode('vectorProduct', name = name + '_VCP')
        else:
            cmds.createNode('vectorProduct')
    #end def vectorProduct()

nd = Node()
nd.choice()
