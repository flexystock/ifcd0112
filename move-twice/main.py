def run(current_pos: int, dice: int) -> int:

    final_pos = current_pos + (dice * 2)
    return final_pos


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

