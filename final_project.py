f = open('file_name.txt')

def main():
    """
    transcibe() provides the original DNA-seq and transcribes RNA-seq
    """
    transcribe()

def transcribe():
    """
    next() scrips the first line description in a FASTA file
    """
    next(f)
    for line in f:
        print(line.strip("\n"))
        print(line.replace("T", "U"))
        print("---------------------------------")
    return f

if __name__ == "__main__":
    main()
