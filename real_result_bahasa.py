import copy

def get_bahasa_real_output(inputfile):
    kalimat = []
    gabungan_kalimat = []

    fileObj = open(inputfile, "r", encoding="utf-8")
    lines = fileObj.readlines()

    for line in lines:
        if line.startswith("\n"):
            continue
        elif line.startswith("#"):
            if len(kalimat) == 0:
                continue
            else:
                gabungan_kalimat.append(copy.deepcopy(kalimat))
                kalimat.clear()
        else:
            kalimat.append(line.split('\t')[0])

    return gabungan_kalimat