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

main()
