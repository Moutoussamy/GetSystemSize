# GetSystemSize
 Get the system size for the running NAMD MD simulation
## Informations

This script allow to calculate the system size for the running NAMD Molecular Dynamics simulations.

## Usage

```
python get_system_size.py -i XXXX.pdb
```

## Example:
```
python get_system_size.py -i toy.pdb
```

output:
```
cellBasisVector1 93.998 0 0
cellBasisVector2 0 93.99 0
cellBasisVector3 0 0 93.989
cellOrigin 0.0194285622995 0.107997277712 46.8495300155
```

## Only water molecule:
It is convenient sometimes to calculate the box size only for the water molecule (e.g. protein/membrane system). If you want to do that you  have to add the "-w" option:

```
python get_system_size.py -i toy.pdb -w 
```
