def run(feeling: str) -> str:
    match feeling.title():
        case 'Happy':
            return "😀"
        case 'Sad':
            return "😔"
        case 'Angry':
            return "😡"
        case 'Pensive':
            return "🤔"
        case 'Surprised':
            return "😮"
        case _:
            return None


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import ifcd0112.facemoji.vendor as vendor

    vendor.launch(run)
