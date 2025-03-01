class BuiltInCategory(Enum,IComparable,IFormattable,IConvertible):
 """
 A list of all the built in categories within Revit.
 

 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 INVALID=None
 OST_AdaptivePoints=None
 OST_AdaptivePoints_HiddenLines=None
 OST_AdaptivePoints_Lines=None
 OST_AdaptivePoints_Planes=None
 OST_AdaptivePoints_Points=None
 OST_AlwaysExcludedInAllViews=None
 OST_Analemma=None
 OST_AnalysisDisplayStyle=None
 OST_AnalysisResults=None
 OST_AnalyticalNodes=None
 OST_AnalyticalNodes_Lines=None
 OST_AnalyticalNodes_Planes=None
 OST_AnalyticalNodes_Points=None
 OST_AnalyticalRigidLinks=None
 OST_AnalyticSpaces=None
 OST_AnalyticSurfaces=None
 OST_AnnotationCrop=None
 OST_AnnotationCropSpecial=None
 OST_AppearanceAsset=None
 OST_ArcWallRectOpening=None
 OST_AreaColorFill=None
 OST_AreaInteriorFill=None
 OST_AreaInteriorFillVisibility=None
 OST_AreaLoads=None
 OST_AreaLoadTags=None
 OST_AreaPolylines=None
 OST_AreaReference=None
 OST_AreaReferenceVisibility=None
 OST_AreaRein=None
 OST_AreaReinBoundary=None
 OST_AreaReinSketchOverride=None
 OST_AreaReinSpanSymbol=None
 OST_AreaReinTags=None
 OST_AreaReinXVisibility=None
 OST_AreaReport_Arc_Minus=None
 OST_AreaReport_Arc_Plus=None
 OST_AreaReport_Boundary=None
 OST_AreaReport_Triangle=None
 OST_Areas=None
 OST_AreaSchemeLines=None
 OST_AreaSchemes=None
 OST_AreaTags=None
 OST_Assemblies=None
 OST_AssemblyOrigin=None
 OST_AssemblyOrigin_Lines=None
 OST_AssemblyOrigin_Planes=None
 OST_AssemblyOrigin_Points=None
 OST_AssemblyTags=None
 OST_Automatic=None
 OST_AxisOfRotation=None
 OST_AxisX=None
 OST_AxisY=None
 OST_AxisZ=None
 OST_BasePointAxisX=None
 OST_BasePointAxisY=None
 OST_BasePointAxisZ=None
 OST_BeamAnalytical=None
 OST_BeamAnalyticalTags=None
 OST_BeamEndSegment=None
 OST_BeamLocalCoordSys=None
 OST_BeamStartSegment=None
 OST_BeamSystemTags=None
 OST_Blocks=None
 OST_BoundaryConditions=None
 OST_BraceAnalytical=None
 OST_BraceAnalyticalTags=None
 OST_BraceEndSegment=None
 OST_BraceLocalCoordSys=None
 OST_BraceStartSegment=None
 OST_BranchPanelScheduleTemplates=None
 OST_BrokenSectionLine=None
 OST_BuildingPad=None
 OST_CableTray=None
 OST_CableTrayCenterLine=None
 OST_CableTrayDrop=None
 OST_CableTrayFitting=None
 OST_CableTrayFittingCenterLine=None
 OST_CableTrayFittingTags=None
 OST_CableTrayRiseDrop=None
 OST_CableTrayRun=None
 OST_CableTrayTags=None
 OST_Cage=None
 OST_CalloutBoundary=None
 OST_CalloutHeads=None
 OST_CalloutLeaderLine=None
 OST_Callouts=None
 OST_Cameras=None
 OST_Camera_Lines=None
 OST_Casework=None
 OST_CaseworkHiddenLines=None
 OST_CaseworkTags=None
 OST_Catalogs=None
 OST_CeilingOpening=None
 OST_Ceilings=None
 OST_CeilingsCut=None
 OST_CeilingsCutPattern=None
 OST_CeilingsDefault=None
 OST_CeilingsFinish1=None
 OST_CeilingsFinish2=None
 OST_CeilingsHiddenLines=None
 OST_CeilingsInsulation=None
 OST_CeilingsMembrane=None
 OST_CeilingsProjection=None
 OST_CeilingsStructure=None
 OST_CeilingsSubstrate=None
 OST_CeilingsSurfacePattern=None
 OST_CeilingTags=None
 OST_CenterLines=None
 OST_CLines=None
 OST_CloudLines=None
 OST_ColorFillLegends=None
 OST_ColorFillSchema=None
 OST_ColumnAnalytical=None
 OST_ColumnAnalyticalGeometry=None
 OST_ColumnAnalyticalRigidLinks=None
 OST_ColumnAnalyticalTags=None
 OST_ColumnEndSegment=None
 OST_ColumnLocalCoordSys=None
 OST_ColumnOpening=None
 OST_Columns=None
 OST_ColumnsHiddenLines=None
 OST_ColumnStartSegment=None
 OST_CommunicationDevices=None
 OST_CommunicationDeviceTags=None
 OST_CompassInner=None
 OST_CompassOuter=None
 OST_CompassPrimaryMonth=None
 OST_CompassSecondaryMonth=None
 OST_CompassSection=None
 OST_CompassSectionFilled=None
 OST_ComponentRepeater=None
 OST_ComponentRepeaterSlot=None
 OST_Conduit=None
 OST_ConduitCenterLine=None
 OST_ConduitDrop=None
 OST_ConduitFitting=None
 OST_ConduitFittingCenterLine=None
 OST_ConduitFittingTags=None
 OST_ConduitRiseDrop=None
 OST_ConduitRun=None
 OST_ConduitStandards=None
 OST_ConduitTags=None
 OST_ConnectorElem=None
 OST_ConnectorElemXAxis=None
 OST_ConnectorElemYAxis=None
 OST_ConnectorElemZAxis=None
 OST_Constraints=None
 OST_ContourLabels=None
 OST_ControlAxisX=None
 OST_ControlAxisY=None
 OST_ControlAxisZ=None
 OST_ControlLocal=None
 OST_CoordinateSystem=None
 OST_Cornices=None
 OST_Coupler=None
 OST_CouplerHiddenLines=None
 OST_CouplerTags=None
 OST_CoverType=None
 OST_CropBoundary=None
 OST_CropBoundarySpecial=None
 OST_CurtainGrids=None
 OST_CurtainGridsCurtaSystem=None
 OST_CurtainGridsRoof=None
 OST_CurtainGridsSystem=None
 OST_CurtainGridsWall=None
 OST_CurtainWallMullions=None
 OST_CurtainWallMullionsCut=None
 OST_CurtainWallMullionsHiddenLines=None
 OST_CurtainWallPanels=None
 OST_CurtainWallPanelsHiddenLines=None
 OST_CurtainWallPanelTags=None
 OST_Curtain_Systems=None
 OST_CurtaSystem=None
 OST_CurtaSystemFaceManager=None
 OST_CurtaSystemHiddenLines=None
 OST_CurtaSystemTags=None
 OST_Curves=None
 OST_CurvesMediumLines=None
 OST_CurvesThinLines=None
 OST_CurvesWideLines=None
 OST_CutOutlines=None
 OST_DataDevices=None
 OST_DataDeviceTags=None
 OST_DataPanelScheduleTemplates=None
 OST_DecalElement=None
 OST_DecalType=None
 OST_DemolishedLines=None
 OST_DesignOptions=None
 OST_DesignOptionSets=None
 OST_DetailComponents=None
 OST_DetailComponentsHiddenLines=None
 OST_DetailComponentTags=None
 OST_Dimensions=None
 OST_DimLockControlLeader=None
 OST_DirectionEdgeLines=None
 OST_DisplacementElements=None
 OST_DisplacementPath=None
 OST_DividedPath=None
 OST_DividedSurface=None
 OST_DividedSurfaceBelt=None
 OST_DividedSurface_DiscardedDivisionLines=None
 OST_DividedSurface_Gridlines=None
 OST_DividedSurface_Nodes=None
 OST_DividedSurface_PatternFill=None
 OST_DividedSurface_PatternLines=None
 OST_DividedSurface_PreDividedSurface=None
 OST_DividedSurface_TransparentFace=None
 OST_DivisionProfile=None
 OST_DivisionRules=None
 OST_Divisions=None
 OST_Doors=None
 OST_DoorsFrameMullionCut=None
 OST_DoorsFrameMullionProjection=None
 OST_DoorsGlassCut=None
 OST_DoorsGlassProjection=None
 OST_DoorsHiddenLines=None
 OST_DoorsOpeningCut=None
 OST_DoorsOpeningProjection=None
 OST_DoorsPanelCut=None
 OST_DoorsPanelProjection=None
 OST_DoorTags=None
 OST_DormerOpeningIncomplete=None
 OST_DSR_ArrowHeadStyleId=None
 OST_DSR_CenterlinePatternCatId=None
 OST_DSR_CenterlineTickMarkStyleId=None
 OST_DSR_DimStyleHeavyEndCategoryId=None
 OST_DSR_DimStyleHeavyEndCatId=None
 OST_DSR_DimStyleTickCategoryId=None
 OST_DSR_InteriorTickMarkStyleId=None
 OST_DSR_LeaderTickMarkStyleId=None
 OST_DSR_LineAndTextAttrCategoryId=None
 OST_DSR_LineAndTextAttrFontId=None
 OST_DuctAccessory=None
 OST_DuctAccessoryTags=None
 OST_DuctColorFillLegends=None
 OST_DuctColorFills=None
 OST_DuctCurves=None
 OST_DuctCurvesCenterLine=None
 OST_DuctCurvesContour=None
 OST_DuctCurvesDrop=None
 OST_DuctCurvesInsulation=None
 OST_DuctCurvesLining=None
 OST_DuctCurvesRiseDrop=None
 OST_DuctFitting=None
 OST_DuctFittingCenterLine=None
 OST_DuctFittingInsulation=None
 OST_DuctFittingLining=None
 OST_DuctFittingTags=None
 OST_DuctInsulations=None
 OST_DuctInsulationsTags=None
 OST_DuctLinings=None
 OST_DuctLiningsTags=None
 OST_DuctSystem=None
 OST_DuctSystem_Reference=None
 OST_DuctSystem_Reference_Visibility=None
 OST_DuctTags=None
 OST_DuctTerminal=None
 OST_DuctTerminalTags=None
 OST_EAConstructions=None
 OST_EdgeSlab=None
 OST_EditCutProfile=None
 OST_ElecDistributionSys=None
 OST_ElectricalCircuit=None
 OST_ElectricalCircuitTags=None
 OST_ElectricalDemandFactor=None
 OST_ElectricalDemandFactorDefinitions=None
 OST_ElectricalEquipment=None
 OST_ElectricalEquipmentHiddenLines=None
 OST_ElectricalEquipmentTags=None
 OST_ElectricalFixtures=None
 OST_ElectricalFixturesHiddenLines=None
 OST_ElectricalFixtureTags=None
 OST_ElectricalInternalCircuits=None
 OST_ElectricalLoadClassifications=None
 OST_ElectricalVoltage=None
 OST_Elev=None
 OST_ElevationMarks=None
 OST_Entourage=None
 OST_EntourageHiddenLines=None
 OST_EPS_Demolished=None
 OST_EPS_Existing=None
 OST_EPS_Future=None
 OST_EPS_New=None
 OST_EPS_Temporary=None
 OST_Extrusions=None
 OST_FabricAreaBoundary=None
 OST_FabricAreas=None
 OST_FabricAreaSketchEnvelopeLines=None
 OST_FabricAreaSketchSheetsLines=None
 OST_FabricAreaTags=None
 OST_FabricationContainment=None
 OST_FabricationContainmentCenterLine=None
 OST_FabricationContainmentDrop=None
 OST_FabricationContainmentRise=None
 OST_FabricationContainmentSymbology=None
 OST_FabricationContainmentTags=None
 OST_FabricationDuctwork=None
 OST_FabricationDuctworkCenterLine=None
 OST_FabricationDuctworkDrop=None
 OST_FabricationDuctworkInsulation=None
 OST_FabricationDuctworkLining=None
 OST_FabricationDuctworkRise=None
 OST_FabricationDuctworkSymbology=None
 OST_FabricationDuctworkTags=None
 OST_FabricationHangers=None
 OST_FabricationHangerTags=None
 OST_FabricationPartsTmpGraphicDrag=None
 OST_FabricationPartsTmpGraphicEnd=None
 OST_FabricationPipework=None
 OST_FabricationPipeworkCenterLine=None
 OST_FabricationPipeworkDrop=None
 OST_FabricationPipeworkInsulation=None
 OST_FabricationPipeworkRise=None
 OST_FabricationPipeworkSymbology=None
 OST_FabricationPipeworkTags=None
 OST_FabricationServiceElements=None
 OST_FabricReinforcement=None
 OST_FabricReinforcementBoundary=None
 OST_FabricReinforcementTags=None
 OST_FabricReinforcementWire=None
 OST_FabricReinSpanSymbol=None
 OST_FaceSplitter=None
 OST_Fascia=None
 OST_FilledRegion=None
 OST_FillPatterns=None
 OST_FireAlarmDevices=None
 OST_FireAlarmDeviceTags=None
 OST_Fixtures=None
 OST_FlexDuctCurves=None
 OST_FlexDuctCurvesCenterLine=None
 OST_FlexDuctCurvesContour=None
 OST_FlexDuctCurvesInsulation=None
 OST_FlexDuctCurvesPattern=None
 OST_FlexDuctTags=None
 OST_FlexPipeCurves=None
 OST_FlexPipeCurvesCenterLine=None
 OST_FlexPipeCurvesContour=None
 OST_FlexPipeCurvesInsulation=None
 OST_FlexPipeCurvesPattern=None
 OST_FlexPipeTags=None
 OST_FloorAnalytical=None
 OST_FloorAnalyticalTags=None
 OST_FloorLocalCoordSys=None
 OST_FloorOpening=None
 OST_Floors=None
 OST_FloorsAnalyticalGeometry=None
 OST_FloorsCut=None
 OST_FloorsCutPattern=None
 OST_FloorsDefault=None
 OST_FloorsFinish1=None
 OST_FloorsFinish2=None
 OST_FloorsInsulation=None
 OST_FloorsInteriorEdges=None
 OST_FloorsMembrane=None
 OST_FloorsProjection=None
 OST_FloorsStructure=None
 OST_FloorsSubstrate=None
 OST_FloorsSurfacePattern=None
 OST_FloorTags=None
 OST_Fluids=None
 OST_FndSlabLocalCoordSys=None
 OST_FootingAnalyticalGeometry=None
 OST_FootingSpanDirectionSymbol=None
 OST_FoundationSlabAnalytical=None
 OST_FoundationSlabAnalyticalTags=None
 OST_FramingAnalyticalGeometry=None
 OST_Furniture=None
 OST_FurnitureHiddenLines=None
 OST_FurnitureSystems=None
 OST_FurnitureSystemsHiddenLines=None
 OST_FurnitureSystemTags=None
 OST_FurnitureTags=None
 OST_GbXMLFaces=None
 OST_gbXML_Ceiling=None
 OST_gbXML_ExteriorWall=None
 OST_gbXML_FixedSkylight=None
 OST_gbXML_FixedWindow=None
 OST_gbXML_InteriorFloor=None
 OST_gbXML_InteriorWall=None
 OST_gbXML_NonSlidingDoor=None
 OST_GbXML_Opening=None
 OST_gbXML_OpeningAir=None
 OST_gbXML_OperableSkylight=None
 OST_gbXML_OperableWindow=None
 OST_gbXML_RaisedFloor=None
 OST_gbXML_Roof=None
 OST_gbXML_Shade=None
 OST_gbXML_SlabOnGrade=None
 OST_gbXML_SlidingDoor=None
 OST_GbXML_SType_Exterior=None
 OST_GbXML_SType_Interior=None
 OST_GbXML_SType_Shade=None
 OST_GbXML_SType_Underground=None
 OST_gbXML_SurfaceAir=None
 OST_gbXML_UndergroundCeiling=None
 OST_gbXML_UndergroundSlab=None
 OST_gbXML_UndergroundWall=None
 OST_GenericAnnotation=None
 OST_GenericLines=None
 OST_GenericModel=None
 OST_GenericModelHiddenLines=None
 OST_GenericModelTags=None
 OST_Girder=None
 OST_GraphicalWarning_OpenConnector=None
 OST_GridChains=None
 OST_GridHeads=None
 OST_Grids=None
 OST_GuideGrid=None
 OST_Gutter=None
 OST_HiddenFloorLines=None
 OST_HiddenLines=None
 OST_HiddenStructuralColumnLines=None
 OST_HiddenStructuralConnectionLines_Deprecated=None
 OST_HiddenStructuralFoundationLines=None
 OST_HiddenStructuralFramingLines=None
 OST_HiddenWallLines=None
 OST_HorizontalBracing=None
 OST_HostFin=None
 OST_HostFinCeiling=None
 OST_HostFinFloor=None
 OST_HostFinHF=None
 OST_HostFinRoof=None
 OST_HostFinTags=None
 OST_HostFinWall=None
 OST_HostTemplate=None
 OST_HVAC_Load_Building_Types=None
 OST_HVAC_Load_Schedules=None
 OST_HVAC_Load_Space_Types=None
 OST_HVAC_Zones=None
 OST_HVAC_Zones_Boundary=None
 OST_HVAC_Zones_ColorFill=None
 OST_HVAC_Zones_InteriorFill=None
 OST_HVAC_Zones_InteriorFill_Visibility=None
 OST_HVAC_Zones_Reference=None
 OST_HVAC_Zones_Reference_Visibility=None
 OST_ImportObjectStyles=None
 OST_InstanceDrivenLineStyle=None
 OST_InsulationLines=None
 OST_InternalAreaLoads=None
 OST_InternalAreaLoadTags=None
 OST_InternalLineLoads=None
 OST_InternalLineLoadTags=None
 OST_InternalLoads=None
 OST_InternalPointLoads=None
 OST_InternalPointLoadTags=None
 OST_InvisibleLines=None
 OST_IOS=None
 OST_IOSAligningLine=None
 OST_IOSAlignmentGraphics=None
 OST_IOSArrays=None
 OST_IOSAttachedDetailGroups=None
 OST_IOSBackedUpElements=None
 OST_IOSBBoxScreenSize=None
 OST_IOSConstructionLine=None
 OST_IOSCrashGraphics=None
 OST_IOSCuttingGeometry=None
 OST_IOSDatumPlane=None
 OST_IOSDetailGroups=None
 OST_IOSDragBox=None
 OST_IOSDragBoxInverted=None
 OST_IOSFabricReinSpanSymbolCtrl=None
 OST_IOSFlipControl=None
 OST_IOSFreeSnapLine=None
 OST_IOSGhost=None
 OST_IOSGroups=None
 OST_IOSMeasureLine=None
 OST_IOSMeasureLineScreenSize=None
 OST_IOSModelGroups=None
 OST_IOSNavWheelPivotBall=None
 OST_IOSNotSilhouette=None
 OST_IOSOpening=None
 OST_IOSRebarSystemSpanSymbolCtrl=None
 OST_IOSRegeneratedElements=None
 OST_IOSRegenerationFailure=None
 OST_IOSRoomCalculationPoint=None
 OST_IOSRoomComputationHeight=None
 OST_IOSRoomPerimeterLines=None
 OST_IOSRoomTagToRoomLines=None
 OST_IOSRoomUpperLowerLines=None
 OST_IOSSketchGrid=None
 OST_IOSSlabShapeEditorAutoCrease=None
 OST_IOSSlabShapeEditorBoundary=None
 OST_IOSSlabShapeEditorExplitCrease=None
 OST_IOSSlabShapeEditorPointBoundary=None
 OST_IOSSlabShapeEditorPointInterior=None
 OST_IOSSuspendedSketch=None
 OST_IOSSuspendedSketch_obsolete=None
 OST_IOSThinPixel=None
 OST_IOSThinPixel_Dash=None
 OST_IOSThinPixel_DashDot=None
 OST_IOSThinPixel_Dot=None
 OST_IOSTilePatternGrid=None
 OST_IOSWallCoreBoundary=None
 OST_IOS_GeoLocations=None
 OST_IOS_GeoSite=None
 OST_IsolatedFoundationAnalytical=None
 OST_IsolatedFoundationAnalyticalTags=None
 OST_Joist=None
 OST_KeynoteTags=None
 OST_KickerBracing=None
 OST_LayoutNodes=None
 OST_LayoutPathBase_Pipings=None
 OST_LayoutPath_Bases=None
 OST_LegendComponents=None
 OST_LevelHeads=None
 OST_Levels=None
 OST_LightingDevices=None
 OST_LightingDeviceTags=None
 OST_LightingFixtures=None
 OST_LightingFixturesHiddenLines=None
 OST_LightingFixtureSource=None
 OST_LightingFixtureTags=None
 OST_LightLine=None
 OST_Lights=None
 OST_LineLoads=None
 OST_LineLoadTags=None
 OST_Lines=None
 OST_LinesBeyond=None
 OST_LinesHiddenLines=None
 OST_LinkAnalyticalTags=None
 OST_LinksAnalytical=None
 OST_LoadCases=None
 OST_LoadCasesAccidental=None
 OST_LoadCasesDead=None
 OST_LoadCasesLive=None
 OST_LoadCasesRoofLive=None
 OST_LoadCasesSeismic=None
 OST_LoadCasesSnow=None
 OST_LoadCasesTemperature=None
 OST_LoadCasesWind=None
 OST_Loads=None
 OST_MaskingRegion=None
 OST_Mass=None
 OST_MassAreaFaceTags=None
 OST_MassCutter=None
 OST_MassExteriorWall=None
 OST_MassExteriorWallUnderground=None
 OST_MassFaceSplitter=None
 OST_MassFloor=None
 OST_MassFloorsAll=None
 OST_MassFloor_Obsolete_IdInWrongRange=None
 OST_MassForm=None
 OST_MassGlazing=None
 OST_MassGlazingAll=None
 OST_MassHiddenLines=None
 OST_Massing=None
 OST_MassingCutOutlines=None
 OST_MassingProjectionOutlines=None
 OST_MassInteriorWall=None
 OST_MassOpening=None
 OST_MassRoof=None
 OST_MassShade=None
 OST_MassSkylights=None
 OST_MassSlab=None
 OST_MassSurface_Obsolete_IdInWrongRange=None
 OST_MassTags=None
 OST_MassTags_Obsolete_IdInWrongRange=None
 OST_MassWallsAll=None
 OST_MassZone=None
 OST_Mass_Obsolete_IdInWrongRange=None
 OST_MatchAll=None
 OST_MatchAnnotation=None
 OST_MatchDetail=None
 OST_Matchline=None
 OST_MatchModel=None
 OST_MatchProfile=None
 OST_MatchSiteComponent=None
 OST_Materials=None
 OST_MaterialTags=None
 OST_MechanicalEquipment=None
 OST_MechanicalEquipmentHiddenLines=None
 OST_MechanicalEquipmentTags=None
 OST_MEPSpaceColorFill=None
 OST_MEPSpaceInteriorFill=None
 OST_MEPSpaceInteriorFillVisibility=None
 OST_MEPSpaceReference=None
 OST_MEPSpaceReferenceVisibility=None
 OST_MEPSpaces=None
 OST_MEPSpaceSeparationLines=None
 OST_MEPSpaceTags=None
 OST_ModelText=None
 OST_MultiCategoryTags=None
 OST_MultiReferenceAnnotations=None
 OST_MultistoryStairs=None
 OST_MultiSurface=None
 OST_NodeAnalyticalTags=None
 OST_NumberingSchemas=None
 OST_NurseCallDevices=None
 OST_NurseCallDeviceTags=None
 OST_OBSOLETE_ElemArrayHiddenLines=None
 OST_OBSOLETE_FabricationPartsTmpGraphicDrop=None
 OST_OBSOLETE_FabricationPartsTmpGraphicDropDrag=None
 OST_OverheadLines=None
 OST_PanelScheduleGraphics=None
 OST_ParamElemElectricalLoadClassification=None
 OST_Parking=None
 OST_ParkingHiddenLines=None
 OST_ParkingTags=None
 OST_PartHiddenLines=None
 OST_Parts=None
 OST_PartTags=None
 OST_PathRein=None
 OST_PathReinBoundary=None
 OST_PathReinSpanSymbol=None
 OST_PathReinTags=None
 OST_Phases=None
 OST_PipeAccessory=None
 OST_PipeAccessoryTags=None
 OST_PipeColorFillLegends=None
 OST_PipeColorFills=None
 OST_PipeConnections=None
 OST_PipeCurves=None
 OST_PipeCurvesCenterLine=None
 OST_PipeCurvesContour=None
 OST_PipeCurvesDrop=None
 OST_PipeCurvesInsulation=None
 OST_PipeCurvesRiseDrop=None
 OST_PipeFitting=None
 OST_PipeFittingCenterLine=None
 OST_PipeFittingInsulation=None
 OST_PipeFittingTags=None
 OST_PipeInsulations=None
 OST_PipeInsulationsTags=None
 OST_PipeMaterials=None
 OST_PipeSchedules=None
 OST_PipeSegments=None
 OST_PipeTags=None
 OST_PipingSystem=None
 OST_PipingSystem_Reference=None
 OST_PipingSystem_Reference_Visibility=None
 OST_PlaceHolderDucts=None
 OST_PlaceHolderPipes=None
 OST_PlanRegion=None
 OST_Planting=None
 OST_PlantingHiddenLines=None
 OST_PlantingTags=None
 OST_PlumbingFixtures=None
 OST_PlumbingFixturesHiddenLines=None
 OST_PlumbingFixtureTags=None
 OST_PointClouds=None
 OST_PointLoads=None
 OST_PointLoadTags=None
 OST_PreviewLegendComponents=None
 OST_ProfileFamilies=None
 OST_ProjectBasePoint=None
 OST_ProjectInformation=None
 OST_Property=None
 OST_PropertySet=None
 OST_Purlin=None
 OST_RailingBalusterRail=None
 OST_RailingBalusterRailCut=None
 OST_RailingHandRail=None
 OST_RailingHandRailAboveCut=None
 OST_RailingRailPathExtensionLines=None
 OST_RailingRailPathLines=None
 OST_Railings=None
 OST_RailingSupport=None
 OST_RailingSystem=None
 OST_RailingSystemBaluster=None
 OST_RailingSystemBalusterHiddenLines_Deprecated=None
 OST_RailingSystemHandRail=None
 OST_RailingSystemHandRailBracket=None
 OST_RailingSystemHandRailBracketHiddenLines_Deprecated=None
 OST_RailingSystemHandRailHiddenLines_Deprecated=None
 OST_RailingSystemHardware=None
 OST_RailingSystemHiddenLines_Deprecated=None
 OST_RailingSystemPanel=None
 OST_RailingSystemPanelBracketHiddenLines_Deprecated=None
 OST_RailingSystemPanelHiddenLines_Deprecated=None
 OST_RailingSystemPost=None
 OST_RailingSystemPostHiddenLines_Deprecated=None
 OST_RailingSystemRail=None
 OST_RailingSystemRailHiddenLines_Deprecated=None
 OST_RailingSystemSegment=None
 OST_RailingSystemSegmentHiddenLines_Deprecated=None
 OST_RailingSystemTags=None
 OST_RailingSystemTermination=None
 OST_RailingSystemTerminationHiddenLines_Deprecated=None
 OST_RailingSystemTopRail=None
 OST_RailingSystemTopRailHiddenLines_Deprecated=None
 OST_RailingSystemTransition=None
 OST_RailingSystemTransitionHiddenLines_Deprecated=None
 OST_RailingTermination=None
 OST_RailingTopRail=None
 OST_RailingTopRailAboveCut=None
 OST_Ramps=None
 OST_RampsAboveCut=None
 OST_RampsDownArrow=None
 OST_RampsDownText=None
 OST_RampsHiddenLines=None
 OST_RampsIncomplete=None
 OST_RampsStringer=None
 OST_RampsStringerAboveCut=None
 OST_RampsUpArrow=None
 OST_RampsUpText=None
 OST_RasterImages=None
 OST_Rebar=None
 OST_RebarCover=None
 OST_RebarHiddenLines=None
 OST_RebarLines=None
 OST_RebarSetToggle=None
 OST_RebarShape=None
 OST_RebarSketchLines=None
 OST_RebarTags=None
 OST_ReferenceLines=None
 OST_ReferencePoints=None
 OST_ReferencePoints_HiddenLines=None
 OST_ReferencePoints_Lines=None
 OST_ReferencePoints_Planes=None
 OST_ReferencePoints_Points=None
 OST_ReferenceViewer=None
 OST_ReferenceViewerSymbol=None
 OST_RemovedGridSeg=None
 OST_RemovedGridSeg_Obsolete_IdInWrongRange=None
 OST_RenderRegions=None
 OST_RepeatingDetailLines=None
 OST_Reveals=None
 OST_RevisionClouds=None
 OST_RevisionCloudTags=None
 OST_Revisions=None
 OST_RigidLinksAnalytical=None
 OST_Roads=None
 OST_RoadsHiddenLines=None
 OST_RoofOpening=None
 OST_Roofs=None
 OST_RoofsCut=None
 OST_RoofsCutPattern=None
 OST_RoofsDefault=None
 OST_RoofsFinish1=None
 OST_RoofsFinish2=None
 OST_RoofsHiddenLines=None
 OST_RoofsInsulation=None
 OST_RoofsInteriorEdges=None
 OST_RoofsMembrane=None
 OST_RoofSoffit=None
 OST_RoofsProjection=None
 OST_RoofsStructure=None
 OST_RoofsSubstrate=None
 OST_RoofsSurfacePattern=None
 OST_RoofTags=None
 OST_RoomColorFill=None
 OST_RoomInteriorFill=None
 OST_RoomInteriorFillVisibility=None
 OST_RoomPolylines=None
 OST_RoomReference=None
 OST_RoomReferenceVisibility=None
 OST_Rooms=None
 OST_RoomSeparationLines=None
 OST_RoomTags=None
 OST_RouteCurve=None
 OST_RouteCurveBranch=None
 OST_RouteCurveMain=None
 OST_RoutingPreferences=None
 OST_RvtLinks=None
 OST_ScheduleGraphics=None
 OST_ScheduleViewParamGroup=None
 OST_SecondaryTopographyContours=None
 OST_SectionBox=None
 OST_SectionHeadMediumLines=None
 OST_SectionHeads=None
 OST_SectionHeadThinLines=None
 OST_SectionHeadWideLines=None
 OST_SectionLine=None
 OST_Sections=None
 OST_SecurityDevices=None
 OST_SecurityDeviceTags=None
 OST_Sewer=None
 OST_ShaftOpening=None
 OST_ShaftOpeningHiddenLines=None
 OST_SharedBasePoint=None
 OST_Sheets=None
 OST_Site=None
 OST_SiteHiddenLines=None
 OST_SitePoint=None
 OST_SitePointBoundary=None
 OST_SiteProperty=None
 OST_SitePropertyLineSegment=None
 OST_SitePropertyLineSegmentTags=None
 OST_SitePropertyTags=None
 OST_SiteRegion=None
 OST_SiteSurface=None
 OST_SiteTags=None
 OST_SketchLines=None
 OST_SpanDirectionSymbol=None
 OST_SpecialityEquipment=None
 OST_SpecialityEquipmentHiddenLines=None
 OST_SpecialityEquipmentTags=None
 OST_SplitterProfile=None
 OST_SpotCoordinates=None
 OST_SpotCoordinateSymbols=None
 OST_SpotElevations=None
 OST_SpotElevSymbols=None
 OST_SpotSlopes=None
 OST_SpotSlopesSymbols=None
 OST_Sprinklers=None
 OST_SprinklerTags=None
 OST_StackedWalls=None
 OST_StackedWalls_Obsolete_IdInWrongRange=None
 OST_Stair2012_Deprecated=None
 OST_StairLanding2012HiddenLines_Deprecated=None
 OST_StairRun2012HiddenLines_Deprecated=None
 OST_Stairs=None
 OST_Stairs2012HiddenLines_Deprecated=None
 OST_StairsAboveCut_ToBeDeprecated=None
 OST_StairsCutMarks=None
 OST_StairsCutMarksAboveCut=None
 OST_StairsDownArrows=None
 OST_StairsDownText=None
 OST_StairsHiddenLines=None
 OST_StairsIncomplete_Deprecated=None
 OST_StairsLandings=None
 OST_StairsLandingTags=None
 OST_StairsNosingLines=None
 OST_StairsNosingLinesAboveCut=None
 OST_StairsOutlines=None
 OST_StairsOutlinesAboveCut=None
 OST_StairsPaths=None
 OST_StairsPathsAboveCut=None
 OST_StairsRailing=None
 OST_StairsRailingAboveCut=None
 OST_StairsRailingBaluster=None
 OST_StairsRailingHiddenLines=None
 OST_StairsRailingRail=None
 OST_StairsRailingTags=None
 OST_StairsRiserLines=None
 OST_StairsRiserLinesAboveCut=None
 OST_StairsRuns=None
 OST_StairsRunTags=None
 OST_StairsSketchBoundaryLines=None
 OST_StairsSketchLandingCenterLines=None
 OST_StairsSketchPathLines=None
 OST_StairsSketchRiserLines=None
 OST_StairsSketchRunLines=None
 OST_StairsStringerCarriage=None
 OST_StairsSupports=None
 OST_StairsSupportsAboveCut=None
 OST_StairsSupportTags=None
 OST_StairsTags=None
 OST_StairStringer2012HiddenLines_Deprecated=None
 OST_StairStringer2012_Deprecated=None
 OST_StairsTriserNumbers=None
 OST_StairsTrisers=None
 OST_StairsTriserTags=None
 OST_StairsUpArrows=None
 OST_StairsUpText=None
 OST_StairTread2012HiddenLines_Deprecated=None
 OST_StickSymbols_Obsolete_IdInWrongRange=None
 OST_StructConnectionAnchors=None
 OST_StructConnectionBolts=None
 OST_StructConnectionFailed=None
 OST_StructConnectionHiddenLines=None
 OST_StructConnectionOthers=None
 OST_StructConnectionPlates=None
 OST_StructConnectionProfiles=None
 OST_StructConnectionReference=None
 OST_StructConnections=None
 OST_StructConnectionStale=None
 OST_StructConnectionSymbol=None
 OST_StructConnectionSymbols=None
 OST_StructConnectionTags=None
 OST_StructLocationLineControl=None
 OST_StructuralAnnotations=None
 OST_StructuralBracePlanReps=None
 OST_StructuralColumnLocationLine=None
 OST_StructuralColumns=None
 OST_StructuralColumnStickSymbols=None
 OST_StructuralColumnTags=None
 OST_StructuralConnectionHandlerTags_Deprecated=None
 OST_StructuralConnectionHandler_Deprecated=None
 OST_StructuralFoundation=None
 OST_StructuralFoundationTags=None
 OST_StructuralFraming=None
 OST_StructuralFramingLocationLine=None
 OST_StructuralFramingOpening=None
 OST_StructuralFramingOther=None
 OST_StructuralFramingSystem=None
 OST_StructuralFramingSystemHiddenLines_Obsolete=None
 OST_StructuralFramingTags=None
 OST_StructuralStiffener=None
 OST_StructuralStiffenerHiddenLines=None
 OST_StructuralStiffenerTags=None
 OST_StructuralTruss=None
 OST_StructuralTrussHiddenLines=None
 OST_StructuralTrussStickSymbols=None
 OST_StructWeldLines=None
 OST_Sun=None
 OST_SunPath1=None
 OST_SunPath2=None
 OST_SunriseText=None
 OST_SunsetText=None
 OST_SunStudy=None
 OST_SunSurface=None
 OST_SWallRectOpening=None
 OST_SwitchboardScheduleTemplates=None
 OST_SwitchSystem=None
 OST_Tags=None
 OST_TelephoneDevices=None
 OST_TelephoneDeviceTags=None
 OST_TextNotes=None
 OST_TilePatterns=None
 OST_TitleBlockMediumLines=None
 OST_TitleBlocks=None
 OST_TitleBlockThinLines=None
 OST_TitleBlockWideLines=None
 OST_Topography=None
 OST_TopographyContours=None
 OST_TopographyHiddenLines=None
 OST_TopographySurface=None
 OST_Truss=None
 OST_TrussBottomChordCurve=None
 OST_TrussChord=None
 OST_TrussDiagWebCurve=None
 OST_TrussDummy=None
 OST_TrussTags=None
 OST_TrussTopChordCurve=None
 OST_TrussVertWebCurve=None
 OST_TrussWeb=None
 OST_VerticalBracing=None
 OST_Viewers=None
 OST_ViewportLabel=None
 OST_Viewports=None
 OST_Views=None
 OST_VolumeOfInterest=None
 OST_WallAnalytical=None
 OST_WallAnalyticalTags=None
 OST_WallFoundationAnalytical=None
 OST_WallFoundationAnalyticalTags=None
 OST_WallLocalCoordSys=None
 OST_WallRefPlanes=None
 OST_WallRefPlanes_Obsolete_IdInWrongRange=None
 OST_Walls=None
 OST_WallsAnalyticalGeometry=None
 OST_WallsCutOutlines=None
 OST_WallsCutPattern=None
 OST_WallsDefault=None
 OST_WallsFinish1=None
 OST_WallsFinish2=None
 OST_WallsInsulation=None
 OST_WallsMembrane=None
 OST_WallsProjectionOutlines=None
 OST_WallsStructure=None
 OST_WallsSubstrate=None
 OST_WallsSurfacePattern=None
 OST_WallTags=None
 OST_WeakDims=None
 OST_Windows=None
 OST_WindowsFrameMullionCut=None
 OST_WindowsFrameMullionProjection=None
 OST_WindowsGlassCut=None
 OST_WindowsGlassProjection=None
 OST_WindowsHiddenLines=None
 OST_WindowsOpeningCut=None
 OST_WindowsOpeningProjection=None
 OST_WindowsSillHeadCut=None
 OST_WindowsSillHeadProjection=None
 OST_WindowTags=None
 OST_Wire=None
 OST_WireHomeRunArrows=None
 OST_WireInsulations=None
 OST_WireMaterials=None
 OST_WireTags=None
 OST_WireTemperatureRatings=None
 OST_WireTickMarks=None
 OST_XRayConstrainedProfileEdge=None
 OST_XRayImplicitPathCurve=None
 OST_XRayPathCurve=None
 OST_XRayPathPoint=None
 OST_XRayProfileEdge=None
 OST_XRaySideEdge=None
 OST_ZoneSchemes=None
 OST_ZoneTags=None
 OST_ZoningEnvelope=None
 value__=None
