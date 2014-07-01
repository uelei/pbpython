#!/bin/bash
cd dbf
for i in $(ls *.dbf ); do
    echo importando $i
    dbf2mysql -hlocalhost -ddbfmy -c -t${i/%".dbf"}  -Uroot -Puc3r2l $i
    echo ok ${i/%".dbf"} .
    rm $i
done
for i in $(ls *.DBF ); do
    echo importando $i
    dbf2mysql -hlocalhost -ddbfmy -c -t${i/%".DBF"} -Uroot -Puc3r2l $i
    echo ok ${i/%".DBF"} .
    rm $i
done

