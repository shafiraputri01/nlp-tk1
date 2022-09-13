from process_output import get_expected_output_list
from real_result_bahasa import get_bahasa_real_output
from tokenizer_accuracy import get_total_correct_token, get_tokenizer_accuracy

# Dataset list
datasets = ["id_csui-ud-test", "id_gsd-ud-test", "id_pud-ud-test"]

print("Result of Bahasa Tokenizer")
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
    real_output_result = get_bahasa_real_output(
        "output_tokenizer/output-bahasa-input_" + datasets[i] + ".txt")

    # Get tokenizer accuracy
    total_token = 0
    total_correct_token = 0
    for i in range(len(exp_output_result)):
        total_token += len(exp_output_result[i])
        total_correct_token += get_total_correct_token(real_output_result[i], exp_output_result[i])

    # Print total token of expected output and total correct token of real output
    print("Total token: " + str(total_token))
    print("Total correct token: " + str(total_correct_token))

    # Get tokenizer accuracy
    accuracy = get_tokenizer_accuracy(total_correct_token, total_token)
    print("Tokenizer accuracy: " + str(accuracy))

    print("-"*70)