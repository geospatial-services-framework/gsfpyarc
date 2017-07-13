;+
; :Description:
;    Task to test ENVI task engine of ENVIRaster datatype
;    See qa_envitaskengine_datatype_enviraster.task for details
;       
; :Author:
;    MAJ, February, 2015 - Initial Draft
;-
pro qa_envitaskengine_datatype_enviraster, INPUT=input, $
                                           OUTPUT=output_uri
                                   
  compile_opt idl2
  
  expectType = 'ENVIRASTER'
  
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
  
  input.Export, output_uri, 'ENVI'

end
