with open("/home/ilya/.config/alacritty/colors.yml", "r") as f:
    lines = f.readlines()

with open("/home/ilya/.config/alacritty/colors.yml", "w") as f:
    i = 0
    while i < len(lines):
        if " normal:" in lines[i]:
            f.write("abob\n")
            i += 7
        else:
            f.write(lines[i])
            i += 1
