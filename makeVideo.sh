#!/bin/bash

ls -tr > arquivos.txt
mencoder mf://@arquivos.txt -mf w=400:h=200:fps=1:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o output.avi