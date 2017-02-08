# with EXPR as VAR

VAR = EXPR
VAR = VAR.__enter__()

try:
	BLOCK
finally:
	VAR.__exit__()