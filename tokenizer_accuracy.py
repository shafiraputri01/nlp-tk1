#################################################################################
#
# Code for check accuracy of tokenizer
#
#################################################################################


#################################################################################
# GET TOTAL CORRECT TOKEN
#################################################################################

def get_total_correct_token(real_token_list, expected_token_list):
    real_token = real_token_list.copy()
    expected_token = expected_token_list.copy()

    correct_token = []
    while len(expected_token) != 0:
        last_exp_token = expected_token.pop()
        last_real_token = real_token.pop()
        if (last_exp_token == last_real_token):
            correct_token.insert(0, last_real_token)
        else:
            last_exp_token = last_exp_token.replace(" ", "").replace("+", "")
            last_real_token = last_real_token.replace(" ", "").replace("+", "")
            while last_exp_token != last_real_token:
                if last_exp_token in last_real_token:
                    last_exp_token = expected_token.pop().replace(
                        " ", "").replace("+", "") + last_exp_token
                elif last_real_token in last_exp_token:
                    last_real_token = real_token.pop().replace(
                        " ", "").replace("+", "") + last_real_token

    return len(correct_token)


#################################################################################
# GET ACCURACY OF TOKENIZER
#################################################################################

def get_tokenizer_accuracy(total_correct_token, total_token):
    return total_correct_token / total_token
