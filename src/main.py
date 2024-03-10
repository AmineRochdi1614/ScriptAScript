import sys

class Interpreter():
    def __init__(self):
        self.variables = {}

    def run(self, code):
        lines = code.split("\n")

        for line in lines:
            self.execute(line)

    def execute(self, line):
        parts = line.split()

        if not parts:
            return
        
        command = parts[0]

        if command == "print":
            self.handle_print(parts)

        if command == "input":
            self.handle_input(parts)

        if command == "let":
            self.handle_let(parts)

        if command == "help":
            print("print = prints text or variable value. input = input text or variable value. let = defines a variable.")

    def handle_print(self, parts):
        if len(parts) == 2:
            printed = parts[1]
            if printed in self.variables:
                print(self.variables[printed])
            else:
                print(printed)
        else:
            print("Invalid print statement.")

    def handle_input(self, parts):
        if len(parts) == 2:
            inputed = parts[1]
            if inputed in self.variables:
                input(self.variables[inputed])
            else:
                input(inputed)
        else:
            input("Invalid input statement.")

    def handle_let(self, parts):
        if len(parts) == 4:
            var_name = parts[1]
            var_operator = parts[2]
            var_value = parts[3]
            if var_value.isdigit():
                var_value = int(var_value)
                if var_operator == '=':
                    self.variables[var_name] = var_value
                elif var_operator == '+':
                    self.variables[var_name] += var_value
                elif var_operator == '-':
                    self.variables[var_name] -= var_value
                else:
                    print("Invalid operator.")
            else:
                if var_operator == '=':
                    self.variables[var_name] = var_value
                else:
                    print("Illegal operator")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            content = file.read()
            inter = Interpreter()

            inter.run(content)
    else:
        code = """
let x = 10
print x
"""
        inter = Interpreter()
        inter.run(code)
