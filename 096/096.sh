#!/bin/bash 

#https://github.com/Fantomas42/sudoku-solver
#http://www.commandlinefu.com/commands/view/3584/remove-color-codes-special-characters-with-sed

cat p096_sudoku.txt | sed ':a;N;$!ba;s/\n/ /g' | sed 's/Grid [0-9][0-9] /\n/g' | sed 's/ //g' > lineas.txt

suma=0
for l in $(cat lineas.txt); do 
    echo $l > /tmp/grid 
    solucion=$(sudoku_solver /tmp/grid | sed 's/ //g' | sed 's/|/\n/g' | head -1 | sed -r "s:\x1B\[[0-9;]*[mK]::g")
    suma=$((suma + solucion))
done
echo $suma
rm lineas.txt
