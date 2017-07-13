;+
; :Description:
;    Task to test IDL task engine of IDL Byte datatype
;    See qa_idltaskengine_datatype_byte.task for details
;       
; :Author:
;    SM, February, 2015 - Initial Draft
;-
pro qa_idltaskengine_datatype_byte, INPUT=input, $
                                   OUTPUT=output
                                   
  compile_opt idl2
  
  expectType = 1
  
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
