from convert_conllu import convert_conllu_file, export_expected_output_list, export_input_list

# Dataset list
files = ["id_csui-ud-test", "id_gsd-ud-test", "id_pud-ud-test"]

print("Datasets list")
print("-"*70)

for file in files:
    result = convert_conllu_file("dataset/" + file + ".conllu")

    print("Nama dataset: " + file)
    print("Total data: " + str(len(result[0])))
    print("-"*50)

    # Export input list to txt file
    export_input_list(
        result[0], "processed_file/input_" + file + ".txt")

    # Export expected output list to txt file
    export_expected_output_list(
        result[1], "processed_file/expected_output_" + file + ".txt")
