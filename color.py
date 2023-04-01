
def main():
    active = input("active hex (2 hex decimals): ")
    inactive = input("inactive hex (2 hex decimals): ")
    red =     "#" +   active + inactive + inactive
    green =   "#" + inactive +   active + inactive
    blue =    "#" + inactive + inactive +   active
    yellow =  "#" +   active +   active + inactive
    magenta = "#" +   active + inactive +   active
    cyan =    "#" + inactive +   active +   active
    print("    red:     '" + red +     "'")
    print("    green:   '" + green +   "'")
    print("    blue:    '" + blue +    "'")
    print("    yellow:  '" + yellow +  "'")
    print("    magenta: '" + magenta + "'")
    print("    cyan:    '" + cyan +    "'")
    with open("/home/ilya/.config/alacritty/colors.yml", "r") as f:
        lines = f.readlines()

    with open("/home/ilya/.config/alacritty/colors.yml", "w") as f:
        i = 0
        while i < len(lines):
            if "  normal:" in lines[i]:
                f.write("  normal:\n")
                f.write("    red:     '" + red +     "'\n")
                f.write("    green:   '" + green +   "'\n")
                f.write("    blue:    '" + blue +    "'\n")
                f.write("    yellow:  '" + yellow +  "'\n")
                f.write("    magenta: '" + magenta + "'\n")
                f.write("    cyan:    '" + cyan +    "'\n")
                i += 7
            else:
                f.write(lines[i])
                i += 1
main()
