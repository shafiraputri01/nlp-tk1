from convert_conllu import convert_conllu_file
from process_output import export_list_to_file, get_expected_output_list, process_real_output_list
from tokenizer_accuracy import get_tokenizer_accuracy, get_total_correct_token


# Dataset list
datasets = ["id_csui-ud-test", "id_gsd-ud-test", "id_pud-ud-test"]

print("Result of Aksara Tokenizer")
print("-"*70)

for i in range(0, len(datasets)):
    # Print dataset name
    print("Dataset name: " + datasets[i])

    # Get expected tokenizer output from a dataset file
    exp_output_result = get_expected_output_list(
        "processed_file/expected_output_" + datasets[i] + ".txt")

    # Print total input of dataset
    print("Total input: " + str(len(exp_output_result)))

    # Get real tokenizer output from a dataset file
    real_output_result = convert_conllu_file(
        "output_tokenizer/output-aksara-input_" + datasets[i] + ".txt.conllu")

    # Process real tokenizer output
    real_output_result_processed = process_real_output_list(
        exp_output_result, real_output_result[1])

    total_token_list = len(exp_output_result)
    total_correct_token_list = 0
    total_token = 0
    total_correct_token = 0
    uncorrect_token_list = []

    for j in range(len(exp_output_result)):
        total_token_data = len(exp_output_result[j])
        total_token += total_token_data

        # Get total correct token of real ouput
        total_correct_token_data = get_total_correct_token(
            real_output_result_processed[j], exp_output_result[j])
        total_correct_token += total_correct_token_data

        # Check if output from tokenizer is correct
        if total_token_data == total_correct_token_data:
            total_correct_token_list += 1
        else:
            uncorrect_token_list.append(real_output_result_processed[j])

    # Print total token list of expected output and total correct token list of real output
    print("Total token list: " + str(total_token_list))
    print("Total correct token list: " + str(total_correct_token_list))

    # Print total token of expected output and total correct token of real output
    print("Total token: " + str(total_token))
    print("Total correct token: " + str(total_correct_token))

    # Get tokenizer accuracy
    accuracy = get_tokenizer_accuracy(total_correct_token, total_token)
    print("Tokenizer accuracy: " + str(accuracy))

    # Export luncorrect token list to a file
    export_list_to_file(
        uncorrect_token_list,
        "uncorrect_token/uncorrect-token-aksara-" + datasets[i] + ".txt")

    print("-"*70)
