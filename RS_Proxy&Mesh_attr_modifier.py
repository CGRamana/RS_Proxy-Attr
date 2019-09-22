import maya.cmds as cmds
import os, sys 
import maya.mel as mm



###########################################################################################################################################
##### this Script controls all selected mesh and proxy shape attributes                                                                   #
##### developed by Ramana vajrapu(v.01)                                                                                                   #
##### any bugs or suggetions please send details to cgramana92@gmail.com                                                                          #
###########################################################################################################################################


if cmds.window("RSAttr", exists=True):
            cmds.deleteUI("RSAttr")

mainWindow = cmds.window("RSAttr", t="RS Mesh&Proxy Modifier", w=265, h=200, s=False)
mainLayout = cmds.columnLayout(w=265, h=230,adjustableColumn=True )
cmds.separator(style='in')
cmds.separator(style='in')
rowColumnLayout1 = cmds.rowColumnLayout(nc=3,  cw=[(1, 50), (2, 150), (3, 30)])
cmds.separator(style='none', h=20)
cmds.separator(style='none', h=20)
cmds.separator(style='none', h=20)
cmds.separator(style='none', h=20)
rowColumnLayout2= cmds.columnLayout( adjustableColumn=True )
cmds.checkBox( label = "Proxy_Subdivsion", bgc=(0.79,0.79, 0.79), ofc="SlSubdivOff()", onc="SlSubdivON()" )
cmds.separator(style='none',h=20)
cmds.checkBox( label = "Proxy_Displacement", bgc=(0.79,0.79, 0.79), ofc="SlDispOff()", onc="SlDispON()")
cmds.separator(style='none', h=20)
cmds.checkBox( label = "Proxy_Matte", bgc=(0.79,0.79, 0.79), ofc="SlmTOff()", onc="SlmTON()")
cmds.separator(style='none', h=20)
mainLayout1= cmds.columnLayout(w=300, h=200)
rowColumnLayout3= cmds.rowColumnLayout(nc=1,  cw=[(1, 150)])
cmds.separator(style='in',w=40)
cmds.button(label ="Redshift_Visibility_Options", c="RSAttrModify()")
cmds.separator(style='in',w=250)
mainLayout1= cmds.columnLayout(w=500, h=200)
cmds.separator(style='in',h=25)
rowColumnLayout4= cmds.rowColumnLayout(nc=1,  cw=[1, 150])
cmds.text( label='CGramana92@gmail.com', align='center' ,w=150, bgc =(0.59,0.39,0.79) )

cmds.showWindow()

    
########### Proxy and Mesh subdiv Enable 
def SlSubdivOff():
    sel = cmds.ls(sl=True) 
    for x in sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            aa=cmds.listHistory(x)[1]
            cmds.setAttr(aa+".visibilityMode",1)
            cmds.setAttr(aa+".tessellationMode",1)
            cmds.setAttr(x+".rsEnableSubdivision",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x + ".rsEnableSubdivision",0)            
def SlSubdivON():
    sel = cmds.ls(sl=True)
    for x in sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            aa=cmds.listHistory(x)[1]
            cmds.setAttr(aa+".visibilityMode",1)
            cmds.setAttr(aa+".tessellationMode",1)
            cmds.setAttr(x+".rsEnableSubdivision",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x + ".rsEnableSubdivision",1)

######## Proxy and Mesh DisplalceMent  Enable 
def SlDispOff():
    sel = cmds.ls(sl=True)  
    for x in sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            aa=cmds.listHistory(x)[1]
            cmds.setAttr(aa+".visibilityMode",1)
            cmds.setAttr(aa+".tessellationMode",1)
            cmds.setAttr(x+".rsEnableDisplacement",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x + ".rsEnableDisplacement",0)            
def SlDispON():
    sel = cmds.ls(sl=True)
    for x in sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            aa=cmds.listHistory(x)[1]
            cmds.setAttr(aa+".visibilityMode",1)
            cmds.setAttr(aa+".tessellationMode",1)
            cmds.setAttr(x+".rsEnableDisplacement",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x + ".rsEnableDisplacement",1)

######### Proxy and Mesh Matte  Enable 
def SlmTOff():
    sel = cmds.ls(sl=True)
    for x in sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            aa=cmds.listHistory(x)[1]
            cmds.setAttr(aa+".visibilityMode",1)
            cmds.setAttr(x+".rsMatteEnable",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x + ".rsMatteEnable",0)            
def SlmTON():
    sel = cmds.ls(sl=True)    
    for x in sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            aa=cmds.listHistory(x)[1]
            cmds.setAttr(aa+".visibilityMode",1)
            cmds.setAttr(x+".rsMatteEnable",1) 
            cmds.setAttr(x +".rsMatteAlpha", 0)
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x + ".rsMatteEnable",1)
            cmds.setAttr(x + ".rsMatteAlpha", 0)
#######################################################################################################################

    
def RSAttrModify():
    if cmds.window("RSAttrC", exists=True):
                cmds.deleteUI("RSAttrC")           
    window = cmds.window("RSAttrC", t='RS_Attr', width=300, h=200, s=False )
    cmds.columnLayout(w=220, h=240,adjustableColumn=True )
    cmds.columnLayout( adjustableColumn=True )
    cmds.separator(st="none", h=10)
    cmds.checkBox( label = "Global Visibility Enable", bgc=(0.79,0.79, 0.79), onc="GlobalOVR()")
    cmds.separator(st="none", h=10)
    cmds.checkBox( label='PrimaryRayVisible' , ofc="PrimaryRayVisblrOFF()", onc="PrimaryRayVisblrON()" )
    cmds.checkBox( label='Cast Shadows', ofc="CastShdOff()", onc="CastShdON()" )
    cmds.checkBox( label='Receive Shadows',ofc="RSOFF()",onc="RSON()" )
    cmds.checkBox( label='Self Shadows' ,ofc="SFShdOFF()",onc="SFShdON()")
    cmds.checkBox( label='Visible in Reflection' ,ofc="VIROff()", onc="VIRON()")
    cmds.checkBox( label='Visible in Refraction' ,ofc="VIRFOff()",onc="VIRFON()")
    cmds.checkBox( label='Cast Reflection' ,ofc="CsRflOff()" , onc="CsRflON()")
    cmds.checkBox( label='Cast Refraction' ,ofc="CsRFracOff()", onc="CsRFracON()")
    cmds.checkBox( label='ForceBruteForce GI' ,ofc="CBFOff()", onc="CBFON()")
    cmds.separator(st="none", h=20)
    cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)'), bgc=(0.79, 0.79, 0.79) )
    cmds.showWindow()
  

def GlobalOVR():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            aa=cmds.listHistory(x)[1]
            cmds.setAttr(aa+".visibilityMode",1)
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x + ".rsEnableVisibilityOverrides",1)

### Primary Visibility Modifyer
def PrimaryRayVisblrOFF():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsPrimaryRayVisible",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsPrimaryRayVisible",0)     
def PrimaryRayVisblrON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsPrimaryRayVisible",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsPrimaryRayVisible",1)       

### Cast Shadow Attr Modifyer            
def CastShdON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsShadowCaster",1)
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsShadowCaster",1)            
def CastShdOff():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsShadowCaster",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsShadowCaster",0)
                 
### Receive Shadow Attr Modifyer             
def RSON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsShadowReceiver",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsShadowReceiver",1)               
def RSOFF():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsShadowReceiver",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsShadowReceiver",0) 
            
### Self Shadow Attr Modifyer             
def SFShdON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsSelfShadows",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsSelfShadows",1)          
def SFShdOFF():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsSelfShadows",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsSelfShadows",0) 
             
### reflection Attr Modifyer                    
def VIRON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsReflectionVisible",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsReflectionVisible",1)             
def VIROff():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsReflectionVisible",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsReflectionVisible",0) 
            
### Visible refraction Attr Modifyer             
def VIRFON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsRefractionVisible",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsRefractionVisible",1)   
def VIRFOff():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsRefractionVisible",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsRefractionVisible",0)  
            
### Cast reflection Attr Modifyer           
def CsRflOff():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsReflectionVisible",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsReflectionCaster",0)                     
def CsRflON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsReflectionVisible",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsReflectionCaster",1) 
               
### Cast refraction Attr Modifyer                   
def CsRFracOff():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsRefractionCaster",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsRefractionCaster",0)          
def CsRFracON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsRefractionCaster",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsRefractionCaster",1)             
            
### Cast BruteForce GI Attr Modifyer                   
def CBFOff():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsForceBruteForceGI",0) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsForceBruteForceGI",0)          
def CBFON():
    Geo_sel =cmds.ls(sl=True)
    for x in Geo_sel:
        if cmds.listConnections(cmds.listRelatives(x,s=True)[0],type="RedshiftProxyMesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x+".rsForceBruteForceGI",1) 
        elif cmds.listRelatives(x,typ="mesh"):
            cmds.setAttr(x+".rsEnableVisibilityOverrides",1)
            cmds.setAttr(x + ".rsForceBruteForceGI",1)              
            
                         
        

            
#########################################################################################################
            
            
    
    
    


