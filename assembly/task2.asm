BEGIN: NOOP
READ X
LOAD X
ADD W
BRZERO END
LOAD X
BRZPOS DOUBLEPOS
BRZNEG DOUBLENEG
BR BEGIN

DOUBLEPOS: NOOP
SUB T
BRZPOS BEGIN
BR SUM

DOUBLENEG: NOOP
ADD T
BRZNEG BEGIN
BR SUM

SUM: NOOP
LOAD Y
ADD X
STORE Y
BR BEGIN

END: NOOP
WRITE Y
STOP

W 1
X 0
Y 0
T 10