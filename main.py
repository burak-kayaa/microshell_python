import sys
import os

def is_builtin(command: str):
    return command in ["exit", "echo", "type"]

def ft_exit(lexer):
    if (len(lexer) == 2):
        sys.exit(int(lexer[1]))
    elif (len(lexer) == 1):
        sys.exit(0)
    else:
        print(f"exit: too many arguments")

def ft_echo(lexer):
    for i in range(1, len(lexer)):
        if (i == len(lexer) - 1):
            print(f"{lexer[i]}", end="")
        else:
            print(f"{lexer[i]}", end=" ")
    print('')

def ft_type(lexer):
    if (len(lexer) == 1):
        print(f"type: not enough arguments")
    else:
        for i in range(1, len(lexer)):
            if (is_builtin(lexer[i])):
                print(f"{lexer[i]} is a shell builtin")
            else:
                path = os.environ["PATH"].split(":")
                for j in path:
                    if (os.path.exists(f"{j}/{lexer[i]}")):
                        print(f"{lexer[i]} is {j}/{lexer[i]}")
                        break
                else:
                    print(f"{lexer[i]}: not found")

def lexer(input: str):
    return input.split()

def main():
    while (1):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        n = input()
        m = lexer(n)
        if (n != ""):
            if (is_builtin(m[0])):
                if (m[0] == "exit"):
                    ft_exit(m)
                elif (m[0] == "echo"):
                    ft_echo(m)
                elif (m[0] == "type"):
                    ft_type(m)
            else:
                nt = os.environ["PATH"].split(":")
                for i in nt:
                    if (os.path.exists(f"{i}/{m[0]}")):
                        os.system(n)
                        break
                else:
                    print(f"{n}: command not found")


if __name__ == "__main__":
    main()
