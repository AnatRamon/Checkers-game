class Style(object):
    """"
    The Style object contains variety of styles to decorate the text in the terminal.
    Write the style before the text. At the end of the test write the end variable.
                    example:
    Style.Foreground.red, Style.Background.yellow, "This is a red text with yellow highlight", Style.end
    """

    end = "\033[0m"

    class Foreground(object):
        """
        The Foreground object contains variety of colours to colour the letters.
        """
        red = "\033[31m"
        blue = "\033[34m"
        dark_grey = "\033[90m"
        violet = "\033[35m"
        cyan = "\033[36m"

    class Background(object):
        """
        The Background object contains variety of colours to highlight the letters.
        """
        yellow = "\033[103m"
        light_grey = "\033[47m"


if __name__ == '__main__':
    print("This is a regular text.")
    print(Style.Background.light_grey + Style.Foreground.dark_grey + "This is a dark grey text "
                                                                     "with light grey highlight." + Style.end)
    print(Style.Foreground.red + "This is a red text." + Style.end)
    print(Style.Foreground.blue + "This is a blue text.")
    print("This is also blue, because you didn't end it." + Style.end)
    print(Style.Foreground.cyan + "On the other hand, I am a cyan text!" + Style.end)
    print(Style.Foreground.violet + "This is a violet text!!!" + Style.end)
    print(Style.Foreground.blue + Style.Background.yellow + "This is a blue text with yellow background" + Style.end)
