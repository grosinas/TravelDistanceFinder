# CyclingDistanceFinder
A simple tool to help me find which student accommodations are within cycling distance of my exchange univesrity. 
Takes url and output file name command line arguments, outputs the text from all div's with "address" class as a file. Requests destination address, transport mode and output file name as input. Outputs a file containing the destination address, transport mode and for each address found in the initial webpage - the distance in km and the time it takes to travel by chosen transport mode. 
## Usage
python3 ./src/app.py Website Name_of_output_file 

# dependencies
pip3 install bs4


When requested for a transport mode an example mode: find the list here visit https://giscience.github.io/openrouteservice/api-reference/endpoints/directions/extra-info/ 
