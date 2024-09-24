def validateLicensePlate(value):
    match len(value):
        case 6 | 7:
            for i in range(len(value)):
                if (i <= 2 and value[i].isupper()) or (i > 2 and value[i].isdigit()):
                    continue
                else:
                    print("License plate is not valid")
                    exit()
            print("License plate is valid")
            exit()
        case _:
            print("License plate is not valid")
            exit()

license_plate = input("Input license plate number: ")
validateLicensePlate(license_plate)
