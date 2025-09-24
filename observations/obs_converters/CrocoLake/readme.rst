CrocoLake 
=========

This observation converter reads data from the CrocoLake, which is a database of oceanographic
observations developed and maintained in the framework of the NSF-sponsored project
`CROCODILE <https://github.com/CROCODILE-CESM>`__ (CESM Regional Ocean and Carbon 
cOnfigurator with Data assimilation and Embedding).

More details about CrocoLake can be found at the Woods Hole Oceanographic Institution
Biogeochemical Ocean Observing and Modeling Lab (`boom-lab <https://github.com/boom-lab>`__): `crocolake-python <https://github.com/boom-lab/crocolake-python>`__.

Required Python packages
------------------------

- dask[dataframe]
- gsw
- numpy
- pandas

To install required packages (except for standard library modules):

.. code-block:: bash

   pip install dask[dataframe] gsw numpy pandas


Paths and examples
------------------

Two working examples showing how to select data from CrocoLake and store it in obs_seq.in format are provided. To use them, remember to replace 'crocolake_path' with your own path to CrocoLake.
