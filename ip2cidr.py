from sys import stdin, stdout

def main():
    for line in stdin:
        stdout.write(str((lambda ip : ip+"\n" if "/" in ip else ip+"/32\n" if "." in ip else ip+"/128\n" if ":" in ip else ip+"\n") (line.strip("\n"))))
    
if __name__ == '__main__':
    main()