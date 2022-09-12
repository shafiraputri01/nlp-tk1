#################################################################################
#
# Code for convert the Conllu file
#
# Author: Shafira Putri Novia Hartanti (shafira.putri91@ui.ac.id)
#
#################################################################################


#################################################################################
# GET LIST OF INPUT AND EXPECTED OUTPUT TEXT
#################################################################################

def convert_conllu_file(file):
    """Get tuple of input text list and expected output list"""

    sentence_list = []

    token_list = []
    expected_token_list = []

    input_file = open(file, "r", encoding="utf-8")
    lines = input_file.readlines()

    for line in lines:
        if line.startswith("# sent_id") or line.startswith("# text_en"):
            continue
        elif line.startswith("# text "):         # get text line
            text = line.split("=")[1][1:-1]     # get text
            sentence_list.append(text)
        else:                                   # get token line
            tokens = line.split("\t")
            if len(tokens) == 10:
                # check multiword token line
                if "-" not in tokens[0]:  # ignore multiword tokens line
                    token_list.append(tokens[1])
            else:
                expected_token_list.append(token_list)
                # reset the token_list for the next sentence
                token_list = []

    return sentence_list, expected_token_list


#################################################################################
# EXPORT INPUT TEXT TO FILE
#################################################################################

def export_input_list(input_list, file_name):
    """Export input list to file"""

    outputfile = open(file_name, "w", encoding="utf-8")

    for input in input_list:
        outputfile.write(input)
        outputfile.write("\n")

    outputfile.close()


#################################################################################
# EXPORT EXPECTED OUTPUT TO FILE
#################################################################################

def export_expected_output_list(expected_output_list, file_name):
    """Export expected output list to file"""

    outputfile = open(file_name, "w", encoding="utf-8")

    for output in expected_output_list:
        for i in range(0, len(output)):
            if i != 0:
                outputfile.write("\t")      # write token separator

            outputfile.write(output[i])     # write token

        outputfile.write("\n")              # write new line

    outputfile.close()
