animal = "Eagle"

match animal:
    case "Eagle" | "Parrot":
        print("Bird")
    case "Lion" | "Tiger":
        print("Mammal")
    case "Python" | "Crocodile":
        print("Reptile")
    case _:
        print("Unknown Class")