import sys

def main():
    if (sys.argv[1] != ""):
        filename = sys.argv[1];
        print "reading file: ",filename
        file_handle = open(filename,"r")
        contents = file_handle.read()
        print contents
        print contents.find("fox");

if __name__ == "__main__":
    main()

