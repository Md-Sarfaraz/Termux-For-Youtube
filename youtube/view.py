class style:
    # color-start
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[34m'
    green = '\033[92m'
    cyan = '\033[96m'
    bblack = '\033[40m'
    dcol = '\033[49;39m'
    # style-start
    b = '\033[1m'  # bold
    u = '\033[4m'  # underline
    rb = '\033[21m'  # remove bold
    ru = '\033[24m'  # remove underline
    reset = '\033[0m'  # remove all attribute


def user_view():
    # OUTPUT To END_USER Start
    header()
    option_body()


def header():
    print(style.reset, style.blue, style.b)
    print("      MODIFIED BY :")
    raj = '''    ____      _       _
    |  _ \    / \     | |
    | |_) |  / _ \ _  | |
    |  _ <  / ___ \ |_| |
    |_| \_\/_/   \_\___/
    '''
    print(style.green, raj)
    print(f"{style.dcol}{style.blue}    Contact Email :{style.b}{style.green}")
    print(f"  sarfarazraj217@gmail.com{style.reset} {style.yellow}")
    print("__________________________________\n")


def option_body():
    print(f"{style.cyan}   1) Audio only")
    print("   2) Best Quality")
    print("   3) 240p Video  press 3")
    print("   4) 360p Video  press 4")
    print("   5) 480p Video  press 5")
    print("   6) 720  Video  press 6")
    print("   7) 1080p Video press 7")
    print("   8) 2k Video    press 8")
    print("   9) 4k Video    press 9")
    #print(f"   0) More Option ({style.red} BETA {style.cyan})")
    print(f"{style.reset}{style.yellow}———————————————————————————————————")
    print(f"{style.reset}{style.red} Press between 1 to 9 or Enter")
    print(f"{style.reset}{style.yellow}———————————————————————————————————{style.reset}")


if __name__ == "__main__":
    user_view()
