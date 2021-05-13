#!/usr/bin/env python3.8

import sys
import function
import os
import __init__

sys.stdout = open(os.devnull, 'w')  # Bloque tout les "print"
function.restore(False)

# --------------* Variables *-------------- #

option = 1
command = 2
argument = 3
have_argument = False

# --------------* Argv *-------------- #

# ---* Option *--- #
try:

    if str(sys.argv[1]) == "-v" or str(sys.argv[1]) == "--verbose":
        sys.stdout = sys.__stdout__
        verbose = True

    elif str(sys.argv[1]) != "-v" or str(sys.argv[1]) != "--verbose":
        option -= 1
        command -= 1
        argument -= 1
        verbose = False

except:
    import __init__  # Run daemon

# ---* Command *--- #
try:
    if str(sys.argv[command]) == "append":
        try:
            argv_service = sys.argv[command + 1]
            function.append(argv_service, verbose)
        except:
            print("commande usage: uacs append 'service_to_append'")

    elif str(sys.argv[command]) == "--help" or str(sys.argv[command]) == "-h":
        sys.stdout = sys.__stdout__
        docs = open("docs/help.txt", "r")
        print(docs.read())
        docs.close()

    elif str(sys.argv[command]) == "start":
        __init__.main()

    elif str(sys.argv[command]) == "send_mail":
        function.send_mail("test", verbose)

    elif str(sys.argv[command]) == "restore":
        function.restore(verbose)

    elif str(sys.argv[command]) == "restore_service":
        function.restore_service(verbose)

    elif str(sys.argv[command]) == "restore_email":
        function.restore_email(verbose)

    elif str(sys.argv[command]) == "init":
        function.init()

    elif str(sys.argv[command]) == "stop":
        __init__.running = False


except:
    print("Command invalid or invalid arguments")
