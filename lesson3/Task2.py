with open('alice_in_wonderland.txt', 'r') as file:
    my_file = file.read()
    f = my_file.replace("...", ".")
    print "Number of sentences in a file - ", len(f.split("."))