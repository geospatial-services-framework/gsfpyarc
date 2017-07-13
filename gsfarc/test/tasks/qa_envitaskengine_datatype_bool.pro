;+
; :Description:
;    Task to test IDL task engine of IDL Boolean datatype
;    See qa_envitaskengine_datatype_bool.task for details
;       
; :Author:
;    SM, March, 2015 - Initial Draft
;-
pro qa_envitaskengine_datatype_bool, INPUT=input, $
                                   OUTPUT=output
                                   
  compile_opt idl2
  
  if (~Isa(input, /BOOLEAN)) then begin
    Message, 'INPUT type is incorrect.'
  endif 
  
  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be'
  endif
  
  output = input

end
