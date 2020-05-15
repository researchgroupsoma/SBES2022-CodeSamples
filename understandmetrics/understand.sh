#!/bin/bash
#process /home/facom/Documents/GIT/understand.txt

repositorios="repositories"
caminho_da_entrada="list-of-samples"

while read -r pasta || [[ -n "$pasta" ]] 
do 

	# echo $pasta
	
	var1=$(echo $pasta | awk -F "," '{print $1,$2}')
	set -- $var1

	caminhoDoProjeto=$1

	var1=$(echo $caminhoDoProjeto | awk -F "/" '{print $1,$2}')   
	set -- $var1

	nome_do_dono=$1
	nome_do_projeto=$2

	und create -db $nome_do_projeto.udb -languages java add $repositorios/$caminhoDoProjeto settings -metrics all settings -metricsOutputFile $nome_do_projeto.csv analyze metrics

done < entrada