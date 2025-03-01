class ClassificationEntries(KeyBasedTreeEntries,IEnumerable[KeyBasedTreeEntry],IEnumerable,IDisposable):
 """ A collection of ClassificationEntry objects that make up the classification table. """
 def Dispose(self):
  """ Dispose(self: KeyBasedTreeEntries,A_0: bool) """
  pass
 @staticmethod
 def LoadClassificationEntriesFromFile(filePath,loadContent):
  """
  LoadClassificationEntriesFromFile(filePath: str,loadContent: KeyBasedTreeEntriesLoadContent) -> bool
  
   Loads the contents of a classification text file into the provided 
    KeyBasedTreeEntriesLoadContent.
  
  
   filePath: The full path of the existing classification file.
   loadContent: The classification entries read from the filePath will be added to this object.

    
     A KeyBasedTreeEntriesLoadContent object will also be updated to contain 
    status information,
     including information about any errors that occurred 
    while reading the keynote entries from
     the specified file.
  
   Returns: True if reading the keynote file succeeds; False if the classification file 
    cannot be read.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: KeyBasedTreeEntries,disposing: bool) """
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
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
