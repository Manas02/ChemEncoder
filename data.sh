#!/bin/bash

# Author : Manas Mahale <manas.mahale@bcp.edu.in>

# Copyright 2021 Manas Mahale
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software 
# is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR 
# THE USE OR OTHER DEALINGS IN THE SOFTWARE.

echo " ██████╗░██████╗░██╗░  ██╗░██████╗░  ██╗░    ██╗██╗░░██╗███████╗███╗░░██╗███████╗░██████╗░██████╗"
echo " ██╔══██╗██╔══██╗██║░  ██║██╔════╝░  ██║░    ██║██║░██╔╝██╔════╝████╗░██║██╔════╝██╔════╝██╔════╝"
echo " ██║░░██║██████╔╝██║░  ██║██║░░██╗░  ██║░    ██║█████═╝░█████╗░░██╔██╗██║█████╗░░╚█████╗░╚█████╗░"
echo " ██║░░██║██╔══██╗██║░  ██║██║░░╚██╗  ██║░    ██║██╔═██╗░██╔══╝░░██║╚████║██╔══╝░░░╚═══██╗░╚═══██╗"
echo " ██████╔╝██║░░██║╚██████╔╝╚██████╔╝  ███████╗██║██║░╚██╗███████╗██║░╚███║███████╗██████╔╝██████╔╝"
echo " ╚═════╝░╚═╝░░╚═╝░╚═════╝░░╚═════╝░  ╚══════╝╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░"
echo ""

echo "© 2021 Manas Mahale"
rm -rf Data
echo ""
echo "This File Creates Data folder and downloads the 3 classes for Drug-Likeness Anaysis"
echo ""
mkdir Data
echo "✅ Main Data Folder Created"
mkdir Data/raw
mkdir Data/interim
mkdir Data/processed
echo "✅ Data Sub Folders Created"
cd Data/raw
curl -o drug.csv https://zinc15.docking.org/substances/subsets/world.csv?count=all -s
echo "1️⃣ /3️⃣  Data for Drug Class Downloaded ✅"
curl -o drug_like.tsv https://www.bindingdb.org/bind/purchase_target_10000.tsv -s
echo "2️⃣ /3️⃣  Data for Drug-Like Class Downloaded ✅"
curl -o non_drug.csv https://zinc15.docking.org/substances/subsets/aggregators.csv?count=all -s
echo "3️⃣ /3️⃣  Data for Non-Drug Class Downloaded ✅"
cd ../..
echo "⚙️ Processing Data ✅"
echo "🧮 Summary Table"
python3 data_proc.py
echo "✅ DONE !! ✅"