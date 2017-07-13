;+
; :Description:
;    Task to test task engine ENVIURI datatype
;    See qa_envitaskengine_datatype_enviuri.task for details
;       
; :Author:
;    SM, February, 2015 - Initial Draft
;-
pro qa_envitaskengine_datatype_enviuri, INPUT=input, $
                                   OUTPUT=output
                                   
  compile_opt idl2
    
  expectType = 7
  
  isType = Size(input,/TYPE)
  if (isType NE expectType) then begin
    Message, 'INPUT is not of expected type. IS: ' + $
      String(isType) + 'EXPECT: ' + String(expectType)
  endif

  if (~Isa(input, /SCALAR)) then begin
    Message, 'INPUT is not a scalar'
  endif
  
  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be'
  endif
  
  output = input

end
