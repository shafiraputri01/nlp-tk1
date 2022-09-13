#!/bin/bash
# Author: Shafira Putri Novia Hartanti (shafira.putri91@ui.ac.id)

old_IFS=$IFS      # save the field separator           
IFS=$'\n'     # new field separator, the end of line

pushd ../in-tagger/aksara
source env/bin/activate
popd

pushd ../inputs
for FILE in input_*.txt ; do
		echo $LINE
		pushd ../in-tagger/aksara
		echo "python3 aksara.py -f \"../../inputs/$FILE\" --output \"../../outputs/output-aksara-$FILE.conllu\""
		python3 aksara.py -f "../../inputs/$FILE" --output "../../outputs/output-aksara-$FILE.conllu"
		popd
done
popd

pushd ../in-tagger/aksara
deactivate
popd
