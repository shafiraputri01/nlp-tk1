#################################################################################
# GET EXPECTED OUTPUT LIST FROM FILE
#################################################################################

def get_expected_output_list(file):
    tokens_list = []

    output_file = open(file, "r", encoding="utf-8")
    lines = output_file.readlines()

    for line in lines:
        tokens = line.replace("\n", "").split("\t")
        tokens_list.append(tokens)

    return tokens_list


#################################################################################
# PROCESS REAL OUTPUT LIST FOR ACCURACY COMPUTATION
#################################################################################

def process_real_output_list(expected_output, real_output):
    expected_output_2 = expected_output.copy()
    real_output_2 = real_output.copy()
    real_output_result = []
    empty_str = ""

    while len(expected_output_2) != 0 and len(real_output_2) != 0:
        tmp = []

        exp_token_list = expected_output_2.pop()
        real_token_list = real_output_2.pop()

        tmp = real_token_list + tmp

        exp_token_join = empty_str.join(
            exp_token_list).replace(" ", "").replace("+", "")
        real_token_join = empty_str.join(
            real_token_list).replace(" ", "").replace("+", "")

        while exp_token_join != real_token_join:
            real_token_list = real_output_2.pop()
            real_token_join = empty_str.join(
                real_token_list).replace(" ", "").replace("+", "") + real_token_join
            tmp = real_token_list + tmp

        real_output_result.insert(0, tmp)

    return real_output_result


#################################################################################
# EXPORT A LIST TO A FILE
#################################################################################

def export_list_to_file(list, filename):
    outputfile = open(filename, "w", encoding="utf-8")

    for item in list:
        outputfile.write(str(item))     # write item in list
        outputfile.write("\n")          # write new line

    outputfile.close()