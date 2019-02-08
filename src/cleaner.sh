#!/bin/sh
#Répertoire courant
rm -rf __pycache__/
rm -rf .pytest_cache/
#Répertoire misc
cd misc
rm -rf __pycache__/
cd ..
#Répertoire analysis_types
cd analysis_types
rm -rf __pycache__/
cd ..
#Répertoire read
cd read
rm -rf __pycache__/
cd ..
#Répertoire write
cd write
rm -rf __pycache__/
cd ..
#Répertoire tests
cd tests
rm -rf __pycache__/
rm -rf .pytest_cache