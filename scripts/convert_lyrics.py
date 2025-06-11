import sys, os, re

old_filepath = sys.argv[1]
new_filepath = "../jp_lyrics/" + os.path.basename(old_filepath)

def main():
    with open(old_filepath, 'r') as f1, open(new_filepath, 'w') as f2:
        # start
        f2.write("---\n")
        f2.write("site: post\n")
    
        for line in f1:
            if line.startswith("title:"):
                add_title(f2, line)
            elif line.startswith("| Japanese"):
                continue
            elif line.startswith("|   "):
                f2.write(".  \n  \n")
            elif line.startswith("| "):
                add_lyrics(f2, line)

def add_title(f, line):
    title = re.search(r'"(.*?)"', line).group(1)
    f.write(f"title: {title}\n")
    f.write("---\n\n")

def add_lyrics(f, line):
    split = line.split("|")
    jp = split[1].strip()
    rm = split[2].strip()
    en = split[3].strip()
    f.write(jp+"  \n")
    f.write(rm.upper()+"  \n")
    f.write("**"+en+"**\n\n")

if __name__ == "__main__":
    main()
