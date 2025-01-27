from htmd.ui import *
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def computeWeights(model):
    stateconcat = np.concatenate(model.data.St)

    try:
        _active_set = model.msm.count_model.state_symbols
    except:
        _active_set = model.msm.active_set
    
    micro_ofcluster = -np.ones(model.data.K, dtype=int)
    micro_ofcluster[_active_set] = np.arange(len(_active_set))
    
    eqdist_offrame = model.msm.stationary_distribution[micro_ofcluster[stateconcat]]
    statprob = 1 / model.data.N
    frameweights = eqdist_offrame * statprob[stateconcat]
    return frameweights

def sample_state(model, state, statetype, frames=50, init_frames=0.1):
    if statetype == "macro":
        mode = "weighted"
    else:
        mode = "random"

    molsampl = model.sampleStates(
        states=[state,], statetype=statetype, samplemode=mode, frames=frames
    )[1][0]

    if init_frames is not None:
        framediff = int(model.data.simlist[0].numframes[0] * init_frames)
        molsampl[:,1] += framediff

    mol = Molecule(model.data.simlist[0].molfile)
    trajlist = []
    for ref in molsampl:
        simid = model.data.simlist[ref[0]]
        trajlist.append(simid.trajectory[0])
    mol.read(trajlist, frames=molsampl[:, 1])
    return mol, molsampl


def build_backbone(cg_mol, ref_mol):
    # this will only work resonably for structures close to reference file

    # load files
    mol_ref = ref_mol.copy()
    mol_ref.filter("name C CA N O and protein")

    traj_coords = []
    for frame in range(cg_mol.numFrames):
        mol = cg_mol.copy()
        mol.dropFrames(keep=frame)
        
        mol.align("name CA", refmol=mol_ref, refsel="name CA")

        resid_ref = np.array(list(set(mol_ref.resid)))
        resid_mol = mol.resid

        # extract coords. CA coords preserved, the rest coppied from ref file
        # alignment every 3 residues
        coords = []
        atom_ref = 0
        atom_mol = 0
        for n in range(len(resid_mol) - 2):
            if n == 0:
                # initial alignment
                mol_ref.align(
                    f"resid {resid_ref[n]} {resid_ref[n+1]} {resid_ref[n+2]} and name CA",
                    refmol=mol,
                    refsel=f"resid {resid_mol[n]} {resid_mol[n+1]} {resid_mol[n+2]}",
                )
                for x in range(4):
                    if mol_ref.name[atom_ref] == "CA":
                        coords.append(mol.coords[atom_mol])
                        atom_mol += 1
                    else:
                        coords.append(mol_ref.coords[atom_ref])
                    atom_ref += 1

            for x in range(4):
                if mol_ref.name[atom_ref] == "N":
                    coords.append(mol_ref.coords[atom_ref])
                elif mol_ref.name[atom_ref] == "CA":
                    # new alignment:
                    mol_ref.align(
                        f"resid {resid_ref[n]} {resid_ref[n+1]} {resid_ref[n+2]} and name CA",
                        refmol=mol,
                        refsel=f"resid {resid_mol[n]} {resid_mol[n+1]} {resid_mol[n+2]}",
                    )
                    coords.append(mol.coords[atom_mol])
                    atom_mol += 1
                else:
                    coords.append(mol_ref.coords[atom_ref])
                atom_ref += 1

            if n == len(resid_mol) - 3:
                for x in range(4):
                    if mol_ref.name[atom_ref] == "CA":
                        coords.append(mol.coords[atom_mol])
                        atom_mol += 1
                    else:
                        coords.append(mol_ref.coords[atom_ref])
                    atom_ref += 1

        traj_coords.append(np.stack(coords))
        
    mol_ref.coords = np.concatenate(traj_coords, axis=2)
    return mol_ref

# Plot related functions
def plotstates(model, states=None, dimx=0, dimy=1, cmap='Set1', zorder=5):
    import matplotlib as mpl
    if not states:
        states = range(model.macronum)
    cmap = mpl.cm.get_cmap(cmap, model.macronum)
    for macro in states:
        macrocenters = model.data.Centers[np.where(model.macro_ofcluster == macro)[0], :]
        macro_pop = round(model.eqDistribution(plot=False)[macro]*100, 1)
        plt.scatter(macrocenters[:,dimx], macrocenters[:,dimy], c=[cmap(macro) for i in range(len(macrocenters[:,0]))], zorder=zorder, label='Macro {}-{}%'.format(macro, macro_pop))   

def plotContour(data, weights, levels, contour = True, fill = True, 
                dimx=0, dimy=1, bins = 80, pad=0.5, cmap='Greys', zorder=1, 
                colors = 'black', alpha = 1):
    from htmd.kinetics import Kinetics
    xmin, xmax = [np.min(data[:, dimx]), np.max(data[:, dimx])] 
    ymin, ymax = [np.min(data[:, dimy]), np.max(data[:, dimy])] 
    hist_range = np.array([[xmin-pad, xmax+pad], [ymin-pad, ymax+pad]])
    counts, xbins, ybins = np.histogram2d(data[:, dimx], data[:, dimy], bins = bins, range=hist_range, weights=weights)
    counts = counts.T
    energy = np.where(counts != 0, -Kinetics._kB*350*np.log(counts), counts)
    energy[energy == 0] = np.max(energy) + 10
    ecorr = np.min(energy[energy!=0])
    energy = np.where(energy != 0, energy-ecorr, energy) ## Setting the minimum as 0
    xcenters = (xbins[:-1] + xbins[1:]) / 2
    ycenters = (ybins[:-1] + ybins[1:]) / 2
    meshx, meshy = np.meshgrid(xcenters, ycenters)
    cmap, norm = getcmap(cmap, levels)
    if contour:
        plt.contour(meshx, meshy, energy, levels=levels, colors=colors, vmin=0, vmax=levels[-1], linewidths=2, alpha = alpha)
    if fill:
        plt.contourf(meshx, meshy, energy, levels=levels, cmap=cmap, vmin=0, vmax=levels[-1], norm=norm)

def getcmap(cmap, bounds):
    import matplotlib.colors as clr
    cmap = plt.get_cmap(cmap)
     # 'rainbow' 'PuOr_r' 'viridis' 'magma' 
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmap = clr.LinearSegmentedColormap.from_list('Custom cmap', cmaplist, cmap.N)
    norm = clr.BoundaryNorm(bounds, cmap.N)
    cmap.set_under(color='white')
    cmap.set_over(color='white')
    return cmap, norm