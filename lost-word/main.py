def run(text: str, target_word: str, replace_word: str) -> str:

    pos = text.find(target_word)

    half1 = text[:pos]
    half2 = text[pos + len(target_word):]

    mtext = half1 + replace_word + half2
    return mtext


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
