import argparse
import numpy as np
from moleculekit.molecule import Molecule

def build_BB(cg_file, ref_file):
    '''Build backbone representation form CA representation using all-atom template, which helps to reate cartoon represenation of protein in VMD and pymol.
    cg_file: CA representation of protein
    ref_file: all-atom template of protein
    
    Example:
    python build_backbone.py -cg_file 1AK4_CA.pdb -ref_file 1AK4.pdb
    '''

    # load files
    mol_ref = Molecule(ref_file)
    mol_ref.filter('name C CA N O and protein')
    mol = Molecule(cg_file)

    mol.align('name CA', refmol = mol_ref, refsel = 'name CA')

    resid_ref = np.array(list(set(mol_ref.resid)))
    resid_mol = mol.resid

    # extract coords. CA coords preserved, the rest coppied from ref file
    # alignment every 3 residues
    coords = []
    atom_ref = 0
    atom_mol = 0
    for n in range(len(resid_mol)-2):
        if n == 0:
            # initial alignment
            mol_ref.align(f'resid {resid_ref[n]} {resid_ref[n+1]} {resid_ref[n+2]} and name CA', refmol=mol, refsel= f'resid {resid_mol[n]} {resid_mol[n+1]} {resid_mol[n+2]}')
            for x in range(4):
                if mol_ref.name[atom_ref] == 'CA':
                    coords.append(mol.coords[atom_mol])
                    atom_mol += 1
                else:
                    coords.append(mol_ref.coords[atom_ref])
                atom_ref+=1

        for x in range(4):
            if mol_ref.name[atom_ref] == 'N':
                coords.append(mol_ref.coords[atom_ref])
            elif mol_ref.name[atom_ref] == 'CA':
                # new alignment:
                mol_ref.align(f'resid {resid_ref[n]} {resid_ref[n+1]} {resid_ref[n+2]} and name CA', refmol=mol, refsel= f'resid {resid_mol[n]} {resid_mol[n+1]} {resid_mol[n+2]}')
                coords.append(mol.coords[atom_mol])
                atom_mol += 1
            else:
                coords.append(mol_ref.coords[atom_ref])
            atom_ref+=1

        if n == len(resid_mol)-3:
            for x in range(4):
                if mol_ref.name[atom_ref] == 'CA':
                    coords.append(mol.coords[atom_mol])
                    atom_mol += 1
                else:
                    coords.append(mol_ref.coords[atom_ref])
                atom_ref+=1

    cord = np.stack(coords)

    # save
    mol_ref.coords = cord
    mol_ref.write(cg_file.replace('.pdb', '_BB.pdb'))

if __name__ == '__main__':

    '''
    Build backbone representation form CA representation using all-atom template, which helps to reate cartoon represenation of protein in VMD and pymol.
    Coordinates of CA atoms are unchanged the rest are build by aligning the reference based on 3 closest CA and copying the coordinates of N, C and O atoms form the backbone.
    This method will only work reasonably if the structure and the tempate are similar to each other. 
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-cg', '--cgmol', help='CA representation extracted from CG simulations', required=True)
    parser.add_argument('-r', '--refmol', help='reference all atom structure used as a template', required=True)

    args = parser.parse_args()

    build_BB(args.cgmol, args.refmol)
                                       