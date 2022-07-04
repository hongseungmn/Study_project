# 문자열을 slice한 결과와 id() 및 is() 연산자 출력 결과를 말해보시오.


# [1] : 문자열
t = "korea"
'''b = t
print( 'b ---> ', b, id(b) )'''

# [2] : 슬라이스 및 id() 출력
print( t, id(t), ' - ', t[:1], id(t[:1]), ' - ', t[:2], id(t[:2]), ' - ', t[:3], id(t[:3]), ' - ', t[:4], id(t[:4]) )
print( t[:], id(t[:]) )


'''print( '-' * 140 )
t += "!"
print( 't ---> ', t, id(t) )  # korea!
a = t[:-1]  # korea
print( 'a ---> ', a, id(a) )'''


# [3] : is 연산자 결과
print( '-' * 140 )
print( 't is t[:] = ', t is t[:] )
print( 't is t[:1] = ', t is t[:1] )
print( 't[:1] is t[:2] = ', t[:1] is t[:2] )
print( 't[:] is t[:5] = ', t[:] is t[:5] )



