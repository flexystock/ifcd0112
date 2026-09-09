def run(intcolor: int) -> str:

    hexcolor = f'#{intcolor:06X}'
    
    return hexcolor


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
