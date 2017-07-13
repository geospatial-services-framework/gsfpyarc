; $Id:
;+
; :Description: This is a test task to test ENVIVector datatypes with in
;               the IDL task engine. It will save out the first part of the
;               the first record in each input vector to a new shapefile.
;    
;
; :Examples:
;
; :Params:
;    N/A
;
; :Returns:
;
; :Keywords:
;
; :Author:
;    BJG, March 2016 - Initial Draft
;-
pro qa_envitaskengine_datatype_ENVIVector, INPUT=input, $
                                           OUTPUT_URI=output_URI
  compile_opt idl2

  expectType = 'ENVIVector'
  
  if (~Isa(input, expectType)) then begin
    Message, 'INPUT is not of expected type. IS: ' + $
             Typename(input) + 'EXPECT: ' + String(expectType)
  endif

  if (~Isa(input, /SCALAR)) then begin
    Message, 'INPUT is not a scalar'
  endif
  
  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be'
  endif

  files = [ input.URI, input.Auxiliary_URI ]

  outFolder = File_DirName(output_URI)
  outBasename = File_BaseName(output_URI, '.shp')

  foreach file, files do begin
    ext = file.Substring(file.LastIndexOf('.'))
    outFile = FilePath(outBasename + ext, Root=outFolder)
    File_Copy, file, outFile
  endforeach
end
