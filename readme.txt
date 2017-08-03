https://senselab.med.yale.edu/modeldb/ShowModel.cshtml?model=231238

This is the readme for an updated version of the Brian model created by R. Brette, which is itself a recreation of a NEURON model from the paper:

Rothman JS, Manis PB (2003) The roles potassium currents play in
regulating the electrical activity of ventral cochlear nucleus
neurons. J Neurophysiol 89:3097-113

The model now uses Brian2, which is more efficient at handling large numbers of cells than its predecessor (Brian version 1). Up to 10,000 cells have been tested, and Brian2 begins to show increased efficiency over Brian1 when # cells > ~1,000.

To run the model, first ensure that Brian and Brian2 are installed:

>>> pip install —-user brian brian2

Then cd to the model directory and type:

$ python useBrian1.py && python useBrian2.py

This will run the model first using Brian1, and then using Brian2. It will print out some data and a runtime. To change the number of cells created, manually change the value of ncell in the python files.

Also provided with this model is a graph showing the performance of the two simulators using different numbers of cells: 1 up to 10,000 cells. Note that these times were generated on a 2017 MacBook, 1.2 GHz Intel Core m3 with 8GB ram. Similar times were received when running the model in macOS and Arch Linux.

Brian2 is python based and installation instructions can be found at:

http://brian2.readthedocs.io/en/stable/

This model was contributed by Thomas McCall
thomas.mccall at case dot edu
