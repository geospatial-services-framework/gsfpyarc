;+
; :Description:
;    Task to test IDL task engine of IDL Long64 datatype
;    See qa_idltaskengine_datatype_long64.task for details
;       
; :Author:
;    SM, March, 2015 - Initial Draft
;-
pro qa_idltaskengine_datatype_long64, INPUT=input, $
                                   OUTPUT=output
                                   
  compile_opt idl2
  
  expectType = 14
  
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
