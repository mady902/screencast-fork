#!/bin/bash

ls *.png > arquivos.txt
mencoder mf://@arquivos.txt -mf w=400:h=200:fps=2:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o output.avi -audiofile teste.wav
#mencoder output.avi -o output2.avi -ovc copy -oac mp3lame -audiofile teste.wav
