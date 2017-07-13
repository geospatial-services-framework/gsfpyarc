;+
; :Description:
;    Task to test IDL task engine of IDL BOOLARRAY datatype
;    See qa_idltaskengine_datatype_boolarray.task for details
;       
; :Author:
;    SM, March, 2016 - Initial Draft
;-
pro qa_idltaskengine_datatype_booleanarray, INPUT=input, $
                                        OUTPUT=output, $
                                        EXPECT_DIMENSIONS=expectDims
                                   
  compile_opt idl2
  
  
  if (~Isa(input, /BOOLEAN, /ARRAY)) then begin
    Message, 'INPUT is not an array.'
  endif
  
  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be.'
  endif
  
  isDimensions = Size(input,/DIMENSIONS)
  if (~ARRAY_EQUAL(isDimensions,expectDims)) then begin
    print, isDimensions
    Message, 'INPUT is not of expected dimensions. IS: ' + $
      (isDimensions.ToString()).Join(',') + ' EXPECT:' + $
      (expectDims.ToString()).Join(',')
  endif

  output = input
  
end
