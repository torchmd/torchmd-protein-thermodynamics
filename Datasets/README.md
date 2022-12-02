# Datasets for Machine Learning Coarse-grained Potentials of Protein Thermodynamics

In these tables you'll be able to find all the data necessary to reproduce the results in the publication.

## Reference MD simulations

| Protein | Size | Trajectories |
| --------- | ------ | ------------ |
| Chignolin | 1,4 GB | [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/chignolin_trajectories.tar.gz) |
| Trp-cage | 2,3 GB | [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/trpcage_trajectories.tar.gz) |
| BBA | 7,2 GB | [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/bba_trajectories.tar.gz) |
| WW-Domain | 19GB + 12GB | [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/wwdomain_1_trajectories.tar.gz), [Part 2](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/wwdomain_2_trajectories.tar.gz) |
| Villin | 5,5 GB | [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/villin_trajectories.tar.gz) |
| NTL9 | 38 GB | [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/ntl9_trajectories.tar.gz) |
| BBL | 33 GB + 26 GB| [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/bbl_1_trajectories.tar.gz), [Part 2](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/wwdomain_2_trajectories.tar.gz) |
| Protein B | 25 GB | [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/proteinb_trajectories.tar.gz) |
| Homeodomain | 8,9 GB| [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/wwdomain_1_trajectories.tar.gz) |
| Protein G | 8,7 GB + 32 GB + 805 GB| [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/proteing_1_trajectories.tar.gz), [Part 2](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/proteing_2_trajectories.tar.gz), [Part 3](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/proteing_3_trajectories.tar.gz)  |
| a3D | 16 GB + 20 GB| [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/a3D_trajectories.tar.gz) |
| Lambda-repressor | 39 GB | [Part 1](pub.htmd.org/protein_thermodynamics_data/reference_trajectories/lambda_trajectories.tar.gz)  |

## Reference Markov state model simulation analysis

Here you'll find all the files regarding the Markov state model analysis of the reference MD simulations above, used as a reference for the evaluation of the coarse-grained potentials.

pub.htmd.org/protein_thermodynamics_data/reference_MSM_analysis.tar.gz

## Experimental structures

Here are all the native structures obtained experimentally that we used as reference in the publication

pub.htmd.org/protein_thermodynamics_data/experimental_structures.tar.gz

## Training data

Here you can find all the training data used for all protein systems, containing alpha-carbon coordinates, forces, deltaforces and embeddings. All arrays are stored in `.npy` arrays.

| Protein | Coordinates| Forces | Deltaforces | Embeddings |
| --------- | :----: | :----------: | :---------: | :------: |
| Chignolin | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/chignolin_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/chignolin_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/chignolin_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/chignolin_ca_embeddings.npy) |
| Trp-cage | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/trpcage_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/trpcage_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/trpcage_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/trpcage_ca_embeddings.npy) |
| BBA | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/bba_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/bba_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/bba_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/bba_ca_embeddings.npy) |
| WW-Domain| [Link](pub.htmd.org/protein_thermodynamics_data/training_data/wwdomain_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/wwdomain_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/wwdomain_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/wwdomain_ca_embeddings.npy) |
| Villin | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/villin_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/villin_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/villin_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/villin_ca_embeddings.npy) |
| NTL9 | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/ntl9_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/ntl9_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/ntl9_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/ntl9_ca_embeddings.npy) |
| BBL | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/bbl_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/bbl_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/bbl_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/bbl_ca_embeddings.npy) |
| Protein B | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/proteinb_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/proteinb_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/proteinb_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/proteinb_ca_embeddings.npy) |
| Homeodomain | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/homeodomain_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/homeodomain_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/homeodomain_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/homeodomain_ca_embeddings.npy) |
| Protein G | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/proteing_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/proteing_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/proteing_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/proteing_ca_embeddings.npy) |
| a3D | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/a3d_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/a3d_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/a3d_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/a3d_ca_embeddings.npy) |
| Lambda-repressor | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/lambda_ca_coords.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/lambda_ca_forces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/lambda_ca_deltaforces.npy) | [Link](pub.htmd.org/protein_thermodynamics_data/training_data/lambda_ca_embeddings.npy) |
