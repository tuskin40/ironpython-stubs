class AnalyticalLink(Element,IDisposable):
 """ An analytical link element that is used to create connections between other AnalyticalModel elements. """
 @staticmethod
 def Create(doc,type,startHubId,endHubId):
  """
  Create(doc: Document,type: ElementId,startHubId: ElementId,endHubId: ElementId) -> AnalyticalLink
  
   Creates a new instance of a AnalyticalLink element between two Hubs.
  
   doc: Document to which new AnalyticalLink should be added.
   type: AnalyticalLinkType for the new AnalyticalLink.
   startHubId: Hub at start of AnalyticalLink.
   endHubId: Hub at end of AnalyticalLink.
   Returns: The newly created AnalyticalLink instance.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def IsAutoGenerated(self):
  """
  IsAutoGenerated(self: AnalyticalLink) -> bool
  
   Specifies whether or not an AnalyticalLink was created by an AnalyticalModel 
    element.
  
   Returns: True if AnalyticalLink was created by an AnalyticalModel element,false 
    otherwise.
  """
  pass
 @staticmethod
 def IsValidHub(doc,hubId):
  """
  IsValidHub(doc: Document,hubId: ElementId) -> bool
  
   Checks whether input hub is valid for an AnalyticalLink.
  
   doc: Hubs's document.
   hubId: Hub to test for validity.
   Returns: True is returned when provided hubId points hub that is valid for 
    AnalyticalLink,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The point at the end of the AnalyticalLink.

Get: End(self: AnalyticalLink) -> XYZ

"""
 EndHubId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Hub ID at end of AnalyticalLink.

Get: EndHubId(self: AnalyticalLink) -> ElementId

"""
 OwnerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ElementId of AnalyticalModel element which created the AnalyticalLink (if any)
   invalidElementId if this Analytical Link was created by the User or API

Get: OwnerId(self: AnalyticalLink) -> ElementId

"""
 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The point at the start of the AnalyticalLink.

Get: Start(self: AnalyticalLink) -> XYZ

"""
 StartHubId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Hub ID at start of AnalyticalLink.

Get: StartHubId(self: AnalyticalLink) -> ElementId

"""

