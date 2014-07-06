#!/bin/sh
ORI=`pwd`
PEN=$ORI
DATA=`date +%Y-%m-%d-%H.%M`
# Faz backup das bases de dados usando o mysqldump
cd backup_bd
rm -r * 
cd ..
mkdir $PEN'/backup_bd/'$DATA
cd $PEN'/backup_bd/'$DATA
printf "realizando backup tb_pb"
mysqldump -u root -pPASSWORD -x -e -B tb_pb | gzip > backup_tbpb-$DATA.sql.gz
echo " ok " 
printf "realizando backup pbbd"
mysqldump -u root -pPASSWORD -x -e -B pbbd | gzip > backup_pbbd-$DATA.sql.gz
echo " ok"
printf "realizando backup matrix"
mysqldump -u root -pPASSWORD -x -e -B matrix | gzip > backup_matrix-$DATA.sql.gz
echo " ok"
printf "realizando backup tbpb001"
mysqldump -u root -pPASSWORD -x -e -B tbpb001 | gzip > backup_tbpb001-$DATA.sql.gz
echo " ok"
printf "realizando backup dbfmy"
mysqldump -u root -pPASSWORD -x -e -B dbfmy | gzip > backup_dbfmy-$DATA.sql.gz
echo " ok"
cd $PEN'/backup_bd'
echo "compactando SQLs"
tar -cf $DATA.bd.tar $DATA
rm -r $DATA
echo "backup completo" 
cd ~
./msg2.py




