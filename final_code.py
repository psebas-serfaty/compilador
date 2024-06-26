from intermedio_code import generate_intermediate_code

def generate_final_code(optimized_code, result):
    # Esta función genera el código final a partir del código intermedio optimizado y el resultado final.
    final_code = []
    final_code.extend(optimized_code)  # Añade el código intermedio optimizado al código final.
    final_code.append(f"print({result})")  # Añade una instrucción para imprimir el resultado final.
    return final_code

def generate_printear_code(ast):
    # Esta función genera el código para la instrucción PRINTEAR.
    if ast.type == 'PRINTEAR':
        expr_code, result = generate_intermediate_code(ast.children[0])  # Genera el código intermedio para la expresión PRINTEAR.
        return expr_code + [f"print({result})"]  # Devuelve el código intermedio seguido de la instrucción para imprimir el resultado.

def generate_final_code_with_printear(optimized_code, ast):
    # Esta función genera el código final que incluye la instrucción PRINTEAR si está presente.
    final_code = []
    for line in optimized_code:
        final_code.append(line)  # Añade cada línea del código intermedio optimizado al código final.
    
    printear_code = generate_printear_code(ast)  # Genera el código PRINTEAR si existe.
    if printear_code:
        final_code.extend(printear_code)  # Añade el código PRINTEAR al código final.
    
    return final_code  # Devuelve el código final completo.