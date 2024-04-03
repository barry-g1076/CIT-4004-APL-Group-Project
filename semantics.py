# import parser_1 as parser
# from shortsourcecode import data as shortdata
# import ply.lex as lex

# Symobol Table
from typing import Union
from SymbolTable import symbol_table, add_to_symbol_table, check_symbol_table

# Scope Stack
# scope_stack = []


# def enter_scope():
#     scope_stack.append({})


# def exit_scope():
#     scope_stack.pop()


# Symbol Table


def semantic_analyzer(ast):
    # enter_scope()
    # for x in ast:
    #     if (
    #         x[0] == "declaration"
    #         or x[0] == "assignment"
    #         or x[0] == "abstract_function_declaration"
    #     ):
    #         handle_in_scope(x)
    #     else:
    #         handle_out_of_scope(x)
    for x in ast:
        if x[0] == "declaration":
            print("*" * 30)
            print(symbol_table)
            # print(scope_stack)
            print("*" * 30)
            handle_declaration(x)
        elif x[0] == "assignment":
            print("*" * 30)
            print(symbol_table)
            # print(scope_stack)
            print("*" * 30)
            handle_assignment(x)
        elif x[0] == "abstract_function_declaration":
            print("*" * 30)
            print(symbol_table)
            # print(scope_stack)
            print("*" * 30)
            handle_abstract_function_declaration(x)
        elif x[0] == "print_statement":
            print("*" * 30)
            print(symbol_table)
            # print(scope_stack)
            print("*" * 30)
            handle_print_statement(x)
        elif x[0] == "attempt_findout_block":
            print("*" * 30)
            print(symbol_table)
            # print(scope_stack)
            print("*" * 30)
            handle_attempt_findout_block(x)
        elif x[0] == "abstract_call":
            print("*" * 30)
            print(symbol_table)
            # print(scope_stack)
            print("*" * 30)
            handle_abstract_call(x)
        elif x[0] == "conditionals":
            print("*" * 30)
            print(symbol_table)
            # print(scope_stack)
            print("*" * 30)
            handle_conditionals(x)
        elif x[0] == "argument_declaration":
            print(x[2])
    # exit_scope()


# def handle_in_scope(node):
#     # current_scope = scope_stack[-1]
#     if node[0] == "declaration":
#         handle_declaration(node, current_scope)
#     elif node[0] == "assignment":
#         handle_assignment(node, current_scope)
#     elif node[0] == "abstract_function_declaration":
#         handle_abstract_function_declaration(node, current_scope)


# def handle_out_of_scope(node):
#     current_scope = scope_stack[-1]
#     if node[0] == "print_statement":
#         handle_print_statement(node, current_scope)
#     elif node[0] == "attempt_findout_block":
#         handle_attempt_findout_block(node, current_scope)
#     elif node[0] == "abstract_call":
#         handle_abstract_call(node, current_scope)
#     elif node[0] == "conditionals":
#         handle_conditionals(node, current_scope)


# Type checking
def type_checking(var_type, value):
    if var_type == "int":
        if not isinstance(value, int):
            print(f"Expected an integer, got type '{type(value).__name__}'")
            # raise ValueError(f"Expected an integer, got '{type(value).__name__}'")
            return False
        else:
            return True
    elif var_type == "float":
        if not isinstance(value, float):
            print(f"Expected a float, got '{type(value).__name__}'")
            # raise ValueError(f"Expected a float, got '{type(value).__name__}'")
            return False
        else:
            return True
    elif var_type == "bool":
        if not isinstance(value, bool):
            print(f"Expected a boolean, got '{type(value).__name__}'")
            # raise ValueError(f"Expected a boolean, got '{type(value).__name__}'")
            return False
        else:
            return True
    elif var_type == "string":
        if not isinstance(value, str):
            print(f"Expected a string, got '{type(value).__name__}'")
            # raise ValueError(f"Expected a string, got '{type(value).__name__}'")
            return False
        else:
            return True
    else:
        print(f"Unknown type '{var_type}'")
        # raise ValueError(f"Unknown type '{var_type}'")
        return False


def handle_expression(node):
    if isinstance(node, tuple):
        if node[0] == "add":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand + right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "sub":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand - right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "mul":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand * right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "div":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand / right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "power":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand**right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "not":
            # Check if the operand is a primitive type
            operand = handle_expression(node[1])
            if not isinstance(operand, bool):
                # print(f"Expected a boolean, got '{type(operand).__name__}'")
                raise ValueError(f"Expected a boolean, got '{type(operand).__name__}'")
            result = not operand
            print(operand, result)
            return result
        elif node[0] == "equivalent":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand == right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "greater_than":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand > right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "less_than":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand < right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "not_equal":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand != right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "less_than_or_equal":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand <= right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "greater_than_or_equal":
            left_operand = handle_expression(node[1])
            right_operand = handle_expression(node[2])
            result = left_operand >= right_operand
            print(left_operand, right_operand, result)
            return result
    else:
        # Check if the node is a string
        if isinstance(node, str):
            # Check is the node is a variable
            if node[0] == "_":
                # If the node is a variable, check if it is in the symbol table
                check = check_symbol_table(node)
                if not check:
                    print(f"Undeclared variable '{node}'")
                    raise ValueError(f"Undeclared variable '{node}'")
                var_type, value, is_locked, symbol_type = symbol_table[node]
                return value
        # print("before return", node)
        return node


# Handles declarations
def handle_declaration(node):
    if len(node) == 4:
        var_mut, var_type, var_name = node[1][1], node[2], node[3]
        is_locked = var_mut == "lock"
        # type_checking(var_type, None)
        check_symbol = add_to_symbol_table(var_name, var_type, None, is_locked)
        if check_symbol:
            print(f"Declared '{var_mut}' variable '{var_name}' of type '{var_type}'")
        else:
            print(f"Variable '{var_name}' is already declared")
            raise ValueError(f"Variable '{var_name}' is already declared")
    elif len(node) == 5:
        var_mut, var_type, var_name, value = node[1][1], node[2], node[3], node[4]
        is_locked = var_mut == "lock"
        # Checks if the type is correct
        value = handle_expression(value)
        type_check = type_checking(var_type, value)
        if not type_check:
            raise ValueError(f"Expected an {var_type}, got '{type(value).__name__}'")
            # raise ValueError(f"Cannot assign locked variable '{var_name}'")
        if not type_check:
            print(f"The variable '{var_name}' recived the wrong type")
            raise ValueError(f"Cannot assign locked variable '{var_name}'")
        # Adds to the symbol table or sends back false
        check_symbol = add_to_symbol_table(var_name, var_type, value, is_locked)
        if check_symbol:
            print(f"'{var_name}' added to symbol table")
            print(symbol_table)
        else:
            print(f"Variable '{var_name}' is already declared")
            raise ValueError(f"Variable '{var_name}' is already declared")
        print(
            f"Declared '{var_mut}' variable '{var_name}' of type '{var_type}' with value '{value}'"
        )
    else:
        raise ValueError("Invalid declaration")


# Handles assignments
def handle_assignment(node):
    if len(node) == 4:
        var_name, value = node[1], node[3]
        value = handle_expression(value)
        check_symbol = check_symbol_table(var_name)
        if not check_symbol:
            print(f"Undeclared variable '{var_name}'")
            raise ValueError(f"Undeclared variable '{var_name}'")
        else:
            var_type, old_value, is_locked, symbol_type = symbol_table[var_name]
            if is_locked and old_value is not None:
                print(f"Cannot reassign locked variable '{var_name}'")
                raise ValueError(f"Cannot reassign locked variable '{var_name}'")
            else:
                type_check = type_checking(var_type, value)
                if not type_check:
                    raise ValueError(
                        f"Expected an {var_type}, got '{type(value).__name__}'"
                    )
                    # raise ValueError(f"Cannot assign locked variable '{var_name}'")
                if type_check:
                    symbol_table[var_name] = (var_type, value, is_locked, symbol_type)
                    print(f"Assigned value '{value}' to variable '{var_name}'")
                else:
                    # TODO add type that was given
                    print(
                        f"Type mismatch for variable '{var_name}' expected '{var_type}'"
                    )
                    raise ValueError(
                        f"Type mismatch for variable '{var_name}' expected '{var_type}'"
                    )
    else:
        raise ValueError("Invalid assignment")


# Handles print statements
def handle_print_statement(node):
    if node[2] != "@":
        if check_symbol_table(node[2]):
            var_name = node[2]
            # TODO remove the print statement
            var_type, value, is_locked, symbol_type = symbol_table[var_name]
            print(f"{node[1]}, '{value}'")
        else:
            print(f"Undeclared variable '{node[2]}'")
            raise ValueError(f"Undeclared variable '{node[2]}'")
    else:
        print(f"{node[1]}")


# Handles attempt and findout blocks
def handle_attempt_findout_block(node):
    handle_attempt_block(node[1])
    handle_findout_block(node[2])
    # print(node)


# Handles attempt block
def handle_attempt_block(node):
    # print(node[1])
    semantic_analyzer(node[1])


# Handles findout block
def handle_findout_block(node):
    # print(node)
    semantic_analyzer(node[2])


# TODO: Implement parameter and argument declaration
# Handles abstract function declaration
def handle_abstract_function_declaration(node):
    check_table = check_symbol_table(node[1])
    if check_table:
        print(f"Function '{node[1]}' is already declared")
        raise ValueError(f"Function '{node[1]}' is already declared")
    else:
        # enter_scope()
        add_to_symbol_table(node[1], None, node[3], True, "function")
        print(f"Declared function '{node[1]}'")
        print(symbol_table)
        # exit_scope()
    # print(node)
    # semantic_analyzer(node[2])


# TODO: Implement parameter and argument declaration
# Handles abstract function call
def handle_abstract_call(node):
    check_table = check_symbol_table(node[1])
    if check_table:
        var_type, value, is_locked, symbol_type = symbol_table[node[1]]
        if symbol_type == "function":
            # enter_scope()
            semantic_analyzer(value)
            # exit_scope()
        else:
            print(f"'{node[1]}' is not a function")
            raise ValueError(f"'{node[1]}' is not a function")
    else:
        print(f"Function '{node[1]}' is not declared")
        raise ValueError(f"Function '{node[1]}' is not declared")


# Handles conditionals
def handle_conditionals(node):
    print(node)
    pass
    # print(node)
