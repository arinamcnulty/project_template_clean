# main.py

from app.io.input import get_input_text, read_file_builtin, read_file_pandas
from app.io.output import print_to_console, write_to_file

def main():
    text1 = get_input_text()
    text2 = read_file_builtin()
    text3 = read_file_pandas()

    print_to_console(text1)
    print_to_console(text2)
    print_to_console(str(text3))

    write_to_file(text1)
    write_to_file(text2)
    write_to_file(str(text3))

if __name__ == "__main__":
    main()
