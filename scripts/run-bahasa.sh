#!/bin/bash
# Author: Shafira Putri Novia Hartanti (shafira.putri91@ui.ac.id)

old_IFS=$IFS      # save the field separator           
IFS=$'\n'     # new field separator, the end of line

pushd ../inputs
for FILE in input_*.txt ; do
	for LINE in $(cat $FILE); do
		pushd ../in-tagger/tagger
		echo "./tag.sh -raw $LINE >> ../../outputs/output-bahasa-$FILE"
		./tag.sh -raw $LINE >> ../../outputs/output-bahasa-$FILE
		
		echo "#" >> ../../outputs/output-bahasa-$FILE
		echo "" >> ../../outputs/output-bahasa-$FILE
		popd
	done
done
popd