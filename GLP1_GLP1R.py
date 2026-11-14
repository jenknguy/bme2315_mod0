
# Models GLP1 (natural hormone) and semaglutide (drug) both binding GLP1R
# Both compete for the same receptor spot, both turn the receptor on
# Plots how receptor activation changes as semaglutide increases,
# with GLP1 held at fasting or fed levels

import numpy as np                     # arrays, log-spaced concentrations
import matplotlib.pyplot as plt        # plotting


# ---------------------------------------------------------------
# Model function
# One ligand: fraction active = L / (Kd + L)
# Two ligands: divide each by its own Kd, add together, same formula
# More of either ligand -> more receptors on -> levels off at 1 (100%)
# ---------------------------------------------------------------
def Fact(G, S, Kd_G, Kd_S):
    """Fraction of GLP1R active with GLP1 (G) + semaglutide (S)"""
    occ = G / Kd_G + S / Kd_S          # combined binding strength of both ligands
    return occ / (1 + occ)             # fraction of receptors on, 0 to 1


# ---------------------------------------------------------------
# Parameters
# Kd = how tightly each ligand binds
# lower Kd = tighter binding
# GLP1 binds ~2x tighter than semaglutide
# GLP1 rises after eating; semaglutide stays ~1 nM on treatment
# ---------------------------------------------------------------
Kd_GLP1 = 0.17         # GLP1 binding constant [nM]
Kd_sema = 0.38         # semaglutide binding constant [nM]
GLP1_fast = 0.015      # GLP1 level when fasting [nM]
GLP1_fed = 0.040       # GLP1 level after a meal [nM]
sema_dose = 1.0        # typical semaglutide level on treatment [nM]


S = np.logspace(-4, 2, 500)     # semaglutide values to test: 0.0001-100 nM


# ---------------------------------------------------------------
# Plot
# Each curve: semaglutide varies, GLP1 stays fixed
# Low semaglutide -> curve sits at GLP1-only activation
# High semaglutide -> drug takes over, curves merge toward 1
# Dotted line = drug with no GLP1, for comparison
# ---------------------------------------------------------------
plt.figure()                                                   # new blank figure

plt.semilogx(S, Fact(GLP1_fast, S, Kd_GLP1, Kd_sema), lw=2,
             label=f"Fasting [GLP1] = {GLP1_fast} nM")         # activation with fasting GLP1

plt.semilogx(S, Fact(GLP1_fed, S, Kd_GLP1, Kd_sema), lw=2,
             label=f"Fed [GLP1] = {GLP1_fed} nM")              # activation with fed GLP1

plt.semilogx(S, Fact(0, S, Kd_GLP1, Kd_sema), lw=1, ls=":", c="k",
             label="Semaglutide alone")                        # activation with drug only

plt.axvline(sema_dose, ls="--", c="gray", lw=1)                 # marks typical drug level

plt.text(sema_dose * 1.15, 0.05, "~1 nM\n(therapeutic)",
         color="gray", fontsize=8)                             # label for that marker


# Axes, labels, save
plt.ylim(0, 1)                                                 # activation from 0 to 100%
plt.xlabel("[Semaglutide] (nM, log scale)")                    # x-axis: drug amount
plt.ylabel("Fraction GLP1R active (Fact)")                     # y-axis: receptors on
plt.title("GLP1 + semaglutide co-stimulation of GLP1R")        # plot title
plt.legend(loc="upper left", fontsize=8)                       # which curve is which
plt.tight_layout()                                             # keep labels from cutting off
plt.savefig("GLP1_GLP1R.png", dpi=200)                         # save plot as image


# ---------------------------------------------------------------
# Key numbers
# Activation with no drug vs. with 1 nM drug, fasting and fed
# Shows drug raises activation a lot and erases fasting/fed gap
# ---------------------------------------------------------------
for name, G in [("fasting", GLP1_fast), ("fed", GLP1_fed)]:
    print(f"{name}: no drug Fact = {Fact(G, 0, Kd_GLP1, Kd_sema):.3f}, "
          f"with 1 nM semaglutide Fact = {Fact(G, sema_dose, Kd_GLP1, Kd_sema):.3f}")


plt.show()                                                     # display the plot
