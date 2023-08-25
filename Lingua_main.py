
def interpret(command):
    if command.startswith("ASK"):
        # Handle ASK command
        pass
    elif command.startswith("DEBUG"):
        # Handle DEBUG command
        pass
    # ... Handle other commands
    else:
        return "Unknown command"

if __name__ == "__main__":
    while True:
        cmd = input("Lingua> ")
        if cmd.lower() in ["exit", "quit"]:
            break
        print(interpret(cmd))
