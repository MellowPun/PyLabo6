import DataToJSONFile
def main():
    delete_server()


def add_server():
    server_list = DataToJSONFile.load_from_JSON() 
    print(server_list)
    name_server = input("What is the name of the server: ")
    IP_address = input("What is the IP-address of the server (255.255.255.255): ")
    server_list.append(["Add Server",[name_server,IP_address]])
    DataToJSONFile.write_to_JSON(server_list)

def delete_server():
    server_list = DataToJSONFile.load_from_JSON()
    print(len(server_list))
    length_string = 0
    
    for i in range(len(server_list)):
        if server_list[i][0]== "Add Server":
            if len(server_list[i][1][0]) > length_string:
             length_string= len(server_list[i][1][0])

    for server in server_list:
        if server[0] == "Add Server":
            string_l = server[1][0]
            print("+-"+length_string*"-"+"-+-"+15*"-"+"-+")
            print(f"| {server[1][0]} |")

#        if server[0][0] == "Add Server":
 #             print("+"+len()*"-"+"+")
  #            print(f"| {} ", end ="")


if __name__=="__main__":
    main()
