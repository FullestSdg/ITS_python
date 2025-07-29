from equazionigrado2nd import * 

'''
ax2_value = AX2("+", 2)
bx_value = BX("-", 20)
c_value = C("-", 6)

ax2_value2 = AX2("+", 7)
bx_value2 = BX("+", 21)
c_value2 = C("-", 3)

equation:SecondGradeEquation = SecondGradeEquation(ax2_value, bx_value, c_value)
equation2:SecondGradeEquation = SecondGradeEquation(ax2_value2, bx_value2, c_value2)

print(f"{equation}\n{equation2}")
print(f"Risultato prima equazione:\n{SecondGradeEquationSolver(equation)}\n\nRisultato seconda equazione:\n{SecondGradeEquationSolver(equation2)}") 
'''
'''
ax2_value = AX2("+", 1)
bx_value = BX("+", 3)
c_value = C("-", 10)

equation:SecondGradeEquation = SecondGradeEquation(ax2_value, bx_value, c_value)
print(equation)
print(SecondGradeEquationSolver(equation))

ax2_value2 = AX2("+", 1)
bx_value2 = BX("-", 5)
c_value = C("+", 10)

equation2:SecondGradeEquation = SecondGradeEquation(ax2_value2, bx_value2, c_value)
print(equation2)
print(SecondGradeEquationSolver(equation))
'''

ax3_value = AX2("-", 5)
bx3_value = BX("+", 3)
c3_value = C("+", 7)

equation3:SecondGradeEquation = SecondGradeEquation(ax3_value, bx3_value, c3_value)
print(equation3)
print(SecondGradeEquationSolver(equation3))