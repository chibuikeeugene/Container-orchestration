# a basic note app
from pathlib import Path

def main():
    # create a data file
    data_file = Path('./data/notes.txt')
    # create its directory to exist
    data_file.parent.mkdir(exist_ok=True, parents=True)

    with data_file.open("a", encoding="utf-8") as file:
        file.write("container started\n")

    print("stored notes: ")
    print(data_file.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
