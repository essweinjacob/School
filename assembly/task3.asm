BEGIN: NOOP
READ X
LOAD X
ADD W
BRZERO PRINT
PUSH
LOAD X
STACKW 0
LOAD A
ADD W
STORE A
LOAD X
BRPOS DOUBLEPOS
BRNEG DOUBLENEG
BR END

DOUBLEPOS: NOOP
SUB T
BRZPOS SUM
LOAD Y
MULT X
STORE Y
BR BEGIN

DOUBLENEG: NOOP
ADD T
BRZNEG SUM
LOAD Y
MULT X
STORE Y
BR BEGIN

SUM: NOOP
LOAD Y
ADD X
STORE Y
BR BEGIN

PRINT: NOOP
LOAD A
BRZERO END
STACKR 0
STORE X
WRITE X
POP
LOAD A
SUB W
STORE A
BR PRINT

END: NOOP
WRITE Y
STOP

W 1
A 0
X 0
Y 0
T 10
