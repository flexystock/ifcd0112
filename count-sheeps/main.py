def run(num_sheeps: int) -> str:

    sheep = "Sheep..."
    sleep = sheep * num_sheeps
    return sleep


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
