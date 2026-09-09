def run(speed_km_h: float) -> float:

    speed_cm_s = (speed_km_h * 100000) / 3600
    return float(int(speed_cm_s))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
