def run(items: list[int]) -> list[int]:
    if not items:
        return []

    pos = len(items) // 2
    paso = items[pos]

    if paso == 0:
        return []

    return items[::paso][::-1]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)