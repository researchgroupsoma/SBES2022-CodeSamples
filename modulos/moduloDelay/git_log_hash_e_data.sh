#!/bin/bash
diretorio_saida="/home/gabriel.menezes/Documentos/mestrado/pesquisa/delayCorona/logs"
repositorios="/home/gabriel.menezes/Documentos/mestrado/pesquisa/repositorios/"

while read -r linha || [[ -n "$linha" ]] 
	do
		echo $linha
		
		cd $repositorios/$linha

		git checkout master
		
		git log --pretty=format:"%H;%ai;%s" --reverse > $diretorio_saida/$linha.txt

	done < /home/gabriel.menezes/Documentos/mestrado/pesquisa/baixarRepositorios/springsamples.txt
