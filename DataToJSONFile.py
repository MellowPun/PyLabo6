import json
def main():
    return 0

def write_to_JSON(choice_input):
    with open("input.json","w") as f:
        json.dump(choice_input,f)


def load_from_JSON():
    with open("input.json","r") as f:
        getallen = json.load(f)
    return getallen


if __name__ == "__main__":
    main()

