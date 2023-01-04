import sys

# All the command line arguments passed to the script
CMD_ARGUMENT = { "other" : [] } 

def parse_cli_arguments():
    parser_state = 0 
    prev_arg = "" 
    arg_type = "" 
    
    # Iterate over all command line arguments
    for arg in sys.argv[1:]: 
        if arg.startswith( "--" ):
            arg = arg[2:]
            arg_type = "option"
        elif arg.startswith( "-" ): 
            arg = arg[1:] 
            arg_type = "option" 
        else: 
            arg_type = "value" 
        
        if parser_state == 0: 
            if arg_type == "option": 
                if ( arg not in CMD_ARGUMENT ) == True: 
                    CMD_ARGUMENT[ arg ]=[] 
                parser_state = 1 
            else: 
                CMD_ARGUMENT[ "other" ].append( arg ) 
        elif parser_state == 1: 
            if ( arg_type == "option" and (arg not in CMD_ARGUMENT) ) == True: 
                CMD_ARGUMENT[ arg ]=[] 
            else: 
                CMD_ARGUMENT[ prev_arg ].append( arg ) 
                parser_state = 0 
        prev_arg = arg

if __name__ == "__main__":
    
    # Parse the command line arguments 
    parse_cli_arguments()

    print( CMD_ARGUMENT )
