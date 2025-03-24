import sys
import DataToJSONFile
import servers
choice_input = None
modi = None
def main():
    if len(sys.argv) >1:
        modi_choice(sys.argv[1])

    else:
        management_servers()
def management_servers():
    print("What do you want to do?:\n[1] Add Server\n[2] Delete Server\n[3] Show List Server\n [4] Check servers")
    choice_input = int(input("Type [1/2/3]: "))
    DataToJSONFile.writeToJSON(choice_input)
    match choice_input:
        case 1:
           add_server()
        case 2:
            delete_server()
        case 3:
            print("Case 3")
        case 4: 
            check_modus()
        case _:
            print("This isn't a valid choice")
            
def check_modus():

def modi_choice(modi):
    match modi:
        case "management":
            management_servers()
        case "check":
            print("Check modus")

if __name__=="__main__":
    main()

