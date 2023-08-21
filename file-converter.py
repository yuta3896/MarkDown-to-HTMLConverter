import markdown,sys

def main():
    if sys.argv[1] == 'markdown': 
        if len(sys.argv) != 4:
            print("Argument is missing!")
            sys.exit()
        try:       
            with open(sys.argv[2], 'r') as input:
                contents = input.read()
        except FileNotFoundError:
            print("FileNotFound!")
            sys.exit()
        with open(sys.argv[3], 'w') as output:
            output.write(markdown.markdown(contents, extensions=['extra', 'toc', 'sane_lists']))
            print("Converted html!")
    else:
        print("illegal command!")
        sys.exit()

if __name__ == "__main__":
    main()

