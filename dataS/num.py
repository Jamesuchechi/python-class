def main():
    values = []

    print("Enter numbers (type 'done' to finish):")
    print("Enter 'clear' to save and restart your program.")
    print("Enter 'exit' to exit the program.")

    while True:
        value = input("type 'clear' to restart your program and 'exit' to exit the program: ")
        if value.lower() == "exit":
            print("program terminated")
            break
        elif value.lower() == "clear":
            values.clear()
            print("program saved and restarted successfully")
            continue
        elif value.lower() == "done":
            for item in values:
                print(f'{item}\n')
        else:
            values.append(value)
            print(f"Added {value} to the list.")

if __name__ == "__main__":
    main()