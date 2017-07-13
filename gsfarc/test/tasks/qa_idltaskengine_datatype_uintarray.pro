;+
; :Description:
;    Task to test IDL task engine of IDL UINTARRAY datatype
;    See qa_idltaskengine_datatype_uintarray.task for details
;       
; :Author:
;    GG, March, 2016 - Initial Draft
;-
pro qa_idltaskengine_datatype_uintarray, INPUT=input, $
                                        OUTPUT=output, $
                                        EXPECT_DIMENSIONS=expectDims
                                   
  compile_opt idl2
  
  expectType = 12
  
  isType = Size(input,/TYPE)
  if (isType NE expectType) then begin
    Message, 'INPUT is not of expected type. IS: ' + $
      String(isType) + ' EXPECT: ' + String(expectType)
  endif

  if (~Isa(input, /ARRAY)) then begin
    Message, 'INPUT is not an array.'
  endif
  
  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be.'
  endif
  
  isDimensions = Fix(Size(input,/DIMENSIONS), TYPE=expectType)
  if (~ARRAY_EQUAL(isDimensions,expectDims)) then begin
    Message, 'INPUT is not of expected dimensions. IS: ' + $
      (isDimensions.ToString()).Join(',') + ' EXPECT:' + $
      (expectDims.ToString()).Join(',')
  endif

  output = input
  
end
