PARAM_BUTTONS_PARAMS =    {
    'UpscaleState':             False,
    'UpscaleMode':              0,
    'UpscaleModes':             ['GFPGAN', 'CF'],
    'UpscaleAmount':            [100, 100],
    'UpscaleMin':               0,
    'UpscaleMax':               100,
    'UpscaleInc':               5,                            
    'UpscaleUnit':              '%', 
    'UpscaleIcon':              './rope/media/gfpgan_logo.png',
    'UpscaleMessage':           'UPSCALER - Upscales faces. [LB: on/off, RB: GFPGAN/Codeformer, MW: amount]',  
    
    'DiffState':                False,
    'DiffMode':                 0, 
    'DiffModes':                ['Diff'], 
    'DiffAmount':               [4],
    'DiffMin':                  0,
    'DiffMax':                  100,
    'DiffInc':                  1,                                                  
    'DiffUnit':                 '%', 
    'DiffIcon':                 './rope/media/diff.png',
    'DiffMessage':              'DIFFERENCER - Blends between Target Face and Swapped Face based on pixel difference. [LB: on/off, MW: difference threshold]',
    
    'MaskState':                False,
    'MaskMode':                 0, 
    'MaskModes':                ['Mask Top', 'Mask Sides', 'Mask Bottom', 'Mask Blur'],  
    'MaskAmount':               [10, 10, 5, 5],
    'MaskMin':                  0,
    'MaskMax':                  64,
    'MaskInc':                  1,                                                 
    'MaskUnit':                 '%', 
    'MaskIcon':                 './rope/media/maskup.png',
    'MaskMessage':              'MASK - Initial mask. A rectangle with adjustable top and sides that blends the Swapped Face into the original background. [RB: top/sides/bottom/blur, MW: amount]',   
    
    'MaskViewState':            False,
    'MaskViewMode':             0, 
    'MaskViewModes':            ['Show Masks'],  
    'MaskViewAmount':           [5],
    'MaskViewMin':              0,
    'MaskViewMax':              50,
    'MaskViewInc':              0,                                                 
    'MaskViewUnit':             '', 
    'MaskViewIcon':             './rope/media/maskblur.png',
    'MaskViewMessage':          'MASK BLUR - Blurs the edges of the mask. [MW: amount]', 

    'CLIPState':                False,
    'CLIPMode':                 0, 
    'CLIPModes':                ['CLIP'], 
    'CLIPAmount':               [50],
    'CLIPMin':                  0,
    'CLIPMax':                  100,
    'CLIPInc':                  1,                                                  
    'CLIPUnit':                 '%', 
    'CLIPIcon':                 './rope/media/CLIP.png',
    'CLIPMessage':              'CLIP - Text based occluder. Occluded objects are visible in the final image (occluded from the mask). [LB: on/off, MW: amount]',                              

    'OccluderState':            False,
    'OccluderMode':             0, 
    'OccluderModes':            ['Occluder'],  
    'OccluderAmount':           [50],
    'OccluderMin':              0,
    'OccluderMax':              100,
    'OccluderInc':              0,                                                 
    'OccluderUnit':             '', 
    'OccluderIcon':             './rope/media/occluder.png',
    'OccluderMessage':          'OCCLUDER - Automatic occluder. Any object in the face region is occluded. [LB: on/off]', 
    
    'FaceParserState':          False,
    'FaceParserMode':           0, 
    'FaceParserModes':          ['Mouth', 'Background'],  
    'FaceParserAmount':         [0, 0],
    'FaceParserMin':            -50,
    'FaceParserMax':            50,
    'FaceParserInc':            1,                                                 
    'FaceParserUnit':           '%', 
    'FaceParserIcon':           './rope/media/parse.png',
    'FaceParserMessage':        'PARSER - Performs occlusion based on features. [LB: on/off, RB: mouth/everything but the face, MW: amount (0 is off, <0 is inside of mouth only for mouth mode)]',
    
    'BlurState':                False,
    'BlurMode':                 0, 
    'BlurModes':                ['Blur'],  
    'BlurAmount':               [5],
    'BlurMin':                  0,
    'BlurMax':                  100,
    'BlurInc':                  1,                                                 
    'BlurUnit':                 '%', 
    'BlurIcon':                 './rope/media/blur.png',
    'BlurMessage':              'BLUR - Global blur. Blurs the combined masks to soften the edges. Is not applied to the inital mask. [MW: amount]',
    
    'ThresholdState':           False,
    'ThresholdMode':            0, 
    'ThresholdModes':           ['Threshold'],  
    'ThresholdAmount':          [85],
    'ThresholdMin':             0,
    'ThresholdMax':             100,
    'ThresholdInc':             1,                                                 
    'ThresholdUnit':            '%', 
    'ThresholdIcon':            './rope/media/thresh.png',
    'ThresholdMessage':         'THRESHOLD - Threshold for determining if Target Faces match faces in a frame. Lower is stricter. [LB: use amount/match all, MW: value]',
    
    'StrengthState':            False,
    'StrengthMode':             0, 
    'StrengthModes':            ['Strength'],  
    'StrengthAmount':           [100],
    'StrengthMin':              0,
    'StrengthMax':              500,
    'StrengthInc':              25,                                                 
    'StrengthUnit':             '%', 
    'StrengthIcon':             './rope/media/strength.png',
    'StrengthMessage':          'STRENGTH - Strength of the Swapper model. This performs additional iterations per 100% (100%=1, 200%=2, ... [MW: amount]',     

    'OrientationState':         False,
    'OrientationMode':          0, 
    'OrientationModes':         ['Orient'],  
    'OrientationAmount':        [0],
    'OrientationMin':           0,
    'OrientationMax':           270,
    'OrientationInc':           90,                                                 
    'OrientationUnit':          '%', 
    'OrientationIcon':          './rope/media/orient.png',
    'OrientationMessage':       'ORIENTATION - Rotate the face detector to better detect faces at different angles. [MW: angle]',                               
    
    "CLIPText":                 '',


    # 'ImgVid':                   'Video',
    }
    
PARAM_BUTTONS_CONSTANT = {   
    }
                
ACTIONS =   {
    'DockState':                False,
    'DockMode':                 0, 
    'DockModes':                [''],                         
    'DockIcon':                 './rope/media/dock.png',
    'DockMessage':              'UNDOCK WINDOW - Undocks the wimdow area. Cannot be re-docked.', 
    'DockButton':               [],
    'DockIconHolder':           [],

    'ImgDockState':                False,
    'ImgDockMode':                 0, 
    'ImgDockModes':                [''],                         
    'ImgDockIcon':                 './rope/media/dock.png',
    'ImgDockMessage':              'UNDOCK WINDOW - Undocks the wimdow area. Cannot be re-docked.', 
    'ImgDockButton':               [],
    'ImgDockIconHolder':           [],    
    
    'SaveImageState':                False,
    'SaveImageMode':                 0, 
    'SaveImageModes':                [''],                         
    'SaveImageIcon':                 './rope/media/save_disk.png',
    'SaveImageMessage':              'SAVE IMAGE - Save image to output folder', 
    'SaveImageButton':               [],
    'SaveImageIconHolder':           [],
    
    'PlayState':                False,
    'PlayMode':                 0, 
    'PlayModes':                [''],                         
    'PlayIcon':                 './rope/media/play.png',
    'PlayMessage':              'PLAY - Plays the video. Press again to stop playing', 
    'PlayButton':               [],
    'PlayIconHolder':           [],
    
    'RecordState':              False,
    'RecordMode':               0, 
    'RecordModes':              [''],                         
    'RecordIcon':               './rope/media/rec.png',
    'RecordMessage':            'RECORD - Arms the PLAY button for recording. Press RECORD, then PLAY to record. Press PLAY again to stop recording.', 
    'RecordButton':             [],
    'RecordIconHolder':         [],  

    'AddMarkerState':           False,
    'AddMarkerMode':            0, 
    'AddMarkerModes':           [''],                         
    'AddMarkerIcon':            './rope/media/add.png',
    'AddMarkerMessage':         'ADD MARKER - Attaaches a parameter marker to the current frame. Markers copy all parameter settings and apply them to all future frames, or until another marker is encountered.', 
    'AddMarkerButton':          [],
    'AddMarkerIconHolder':      [],  

    'RemoveMarkerState':        False,
    'RemoveMarkerMode':         0, 
    'RemoveMarkerModes':        [''],                         
    'RemoveMarkerIcon':         './rope/media/remove.png',
    'RemoveMarkerMessage':      'REMOVE MARKER - Removes the parameter marker from the current frame.', 
    'RemoveMarkerButton':       [],
    'RemoveMarkerIconHolder':   [],  

    'PrevMarkerState':          False,
    'PrevMarkerMode':           0, 
    'PrevMarkerModes':          [''],                         
    'PrevMarkerIcon':           './rope/media/prev.png',
    'PrevMarkerMessage':        'PREVIOUS MARKER - Move to the previous marker.', 
    'PrevMarkerButton':         [],
    'PrevMarkerIconHolder':     [],         

    'NextMarkerState':          False,
    'NextMarkerMode':           0, 
    'NextMarkerModes':          [''],                         
    'NextMarkerIcon':           './rope/media/next.png',
    'NextMarkerMessage':        'NEXT MARKER - Move to the next marker.', 
    'NextMarkerButton':         [],
    'NextMarkerIconHolder':     [],  

    'ToggleStopState':          False,
    'ToggleStopMode':           0, 
    'ToggleStopModes':          [''],                         
    'ToggleStopIcon':           './rope/media/STOP.png',
    'ToggleStopMessage':        'STOP MARKER - Sets a frame that will stop the video playing/recording.', 
    'ToggleStopButton':         [],
    'ToggleStopIconHolder':     [],                  
    

    'FindFacesState':           False,
    'FindFacesMode':            0, 
    'FindFacesModes':           ['Find'],                         
    'FindFacesIcon':            './rope/media/tarface.png',
    'FindFacesMessage':         'FIND FACES - Find all faces in the current frame.',     

    'ClearFacesState':          False,
    'ClearFacesMode':           0, 
    'ClearFacesModes':          ['Clear'],                         
    'ClearFacesIcon':           './rope/media/tarfacedel.png',
    'ClearFacesMessage':        'REMOVE FACES - Remove all currently found faces.',   

    'SwapFacesState':           False,
    'SwapFacesMode':            0, 
    'SwapFacesModes':           ['Swap'],                         
    'SwapFacesIcon':            './rope/media/swap.png',
    'SwapFacesMessage':         'SWAP - Swap assigned Source Faces and Target Faces', 
    'SwapFacesButton':          [],
    'SwapFacesIconHolder':      [],
    
 
    'LoadSFacesState':           False,
    'LoadSFacesMode':            0, 
    'LoadSFacesModes':           [''],                         
    'LoadSFacesIcon':            './rope/media/save.png',
    'LoadSFacesMessage':         'LOAD SOURCE FACES - Load Source Faces from Folder. Make sure the folder only contains <good> images.', 
    'LoadSFacesButton':          [],
    'LoadSFacesIconHolder':      [],

    'DelEmbedState':           False,
    'DelEmbedMode':            0, 
    'DelEmbedModes':           ['Del Emb'],                         
    'DelEmbedIcon':            './rope/media/delemb.png',
    'DelEmbedMessage':         'DELETE EMBEDDING - Delete the currently selected embedding', 
    'DelEmbedButton':          [],
    'DelEmbedIconHolder':      [],

    'LoadTVideosState':           False,
    'LoadTVideosMode':            0, 
    'LoadTVideosModes':           [''],                         
    'LoadTVideosIcon':            './rope/media/save.png',
    'LoadTVideosMessage':         'LOAD TARGET VIDEOS/IMAGES - Load targets from folder.', 
    'LoadTVideosButton':          [],
    'LoadTVideosIconHolder':      [],

    'ImgVidState':           False,
    'ImgVidMode':            0, 
    'ImgVidModes':           ['Videos', 'Images'],                         
    'ImgVidIcon':            './rope/media/imgvid.png',
    'ImgVidMessage':         'IMAGE/VIDEO - Toggle between Image and Video folder view.', 
    'ImgVidButton':          [],
    'ImgVidIconHolder':      [],    
    
    'StartRopeState':           False,
    'StartRopeMode':            0, 
    'StartRopeModes':           ['Start Rope'],                         
    'StartRopeIcon':            './rope/media/save.png',
    'StartRopeMessage':         'START ROPE - Loads all folders and initializes models', 
    'StartRopeButton':          [],
    'StartRopeIconHolder':      [],      
    
    'OutputFolderState':           False,
    'OutputFolderMode':            0, 
    'OutputFolderModes':           [''],                         
    'OutputFolderIcon':            './rope/media/save.png',
    'OutputFolderMessage':         'OUTPUT FOLDER - Select folder for Image and Video output.', 
    'OutputFolderButton':          [],
    'OutputFolderIconHolder':      [],  
    
    'ThreadsState':           False,
    'ThreadsMode':            0, 
    'ThreadsModes':           [''],                         
    'ThreadsIcon':            './rope/media/threads.png',
    'ThreadsMessage':         'THREADS - Set number of execution threads. Once PLAY is pressed, reducing the number of threads will not release memory.', 
    'ThreadsButton':          [],
    'ThreadsIconHolder':      [],  

    'VideoQualityState':           False,
    'VideoQualityMode':            0, 
    'VideoQualityModes':           [''],                         
    'VideoQualityIcon':            './rope/media/tarface.png',
    'VideoQualityMessage':         'VIDEO QUALITY - The encoding quality of the recorded video. 0 is best, 50 is wrost, 18 is mostly lossless. File size increases with a lower quality number.', 
    'VideoQualityButton':          [],
    'VideoQualityIconHolder':      [],  

    # 'State':           False,
    # 'Mode':            0, 
    # 'Modes':           ['Videos', 'Images'],                         
    # 'Icon':            './rope/media/imgvid.png',
    # 'Message':         'IMAGE/VIDEO - Toggle between Image and Video folder view.', 
    # 'Button':          [],
    # 'IconHolder':      [],      
    
    
     }   