import sys

# TTT  F Phe      TCT  S Ser      TAT  Y Tyr      TGT  C Cys
# TTC  F Phe      TCC  S Ser      TAC  Y Tyr      TGC  C Cys
# TTA  L Leu      TCA  S Ser      TAA  * Ter      TGA  * Ter
# TTG  L Leu i    TCG  S Ser      TAG  * Ter      TGG  W Trp
#
# CTT  L Leu      CCT  P Pro      CAT  H His      CGT  R Arg
# CTC  L Leu      CCC  P Pro      CAC  H His      CGC  R Arg
# CTA  L Leu      CCA  P Pro      CAA  Q Gln      CGA  R Arg
# CTG  L Leu i    CCG  P Pro      CAG  Q Gln      CGG  R Arg
#
# ATT  I Ile i    ACT  T Thr      AAT  N Asn      AGT  S Ser
# ATC  I Ile i    ACC  T Thr      AAC  N Asn      AGC  S Ser
# ATA  I Ile i    ACA  T Thr      AAA  K Lys      AGA  R Arg
# ATG  M Met i    ACG  T Thr      AAG  K Lys      AGG  R Arg
#
# GTT  V Val      GCT  A Ala      GAT  D Asp      GGT  G Gly
# GTC  V Val      GCC  A Ala      GAC  D Asp      GGC  G Gly
# GTA  V Val      GCA  A Ala      GAA  E Glu      GGA  G Gly
# GTG  V Val i    GCG  A Ala      GAG  E Glu      GGG  G Gly

prot2nt = {
    "F": "TT[TC]",
    "L": "(TT[AG]|CT[ACGT])",
    "I": "AT[ACT]",
    "M": "ATG",
    "V": "AT[ACG]",
    "S": "TC[ACGT]",
    "P": "CC[ACGT]",
    "T": "AC[ACGT]",
    "A": "GC[ACGT]",
    "Y": "TA[ACGT]",
    "*": "TA[AG]",
    "H": "CA[CT]",
    "Q": "CA[AG]",
    "N": "AA[CT]",
    "K": "AA[AG]",
    "D": "GA[CT]",
    "E": "GA[AG]",
    "C": "TG[CT]",
    "*": "TGA",
    "W": "TGG",
    "R": "CG[ACGT]",
    "S": "AG[CT]",
    "R": "AG[AG]",
    "G": "GG[ACGT]",
    ".": "...",
    "\n": "\n",
}

if len(sys.argv) < 2:
    print(f"Usage: biosearchx.py PROTEINSEARCHSEQUENCE")
    sys.exit(0)

for line in sys.argv[1]:
    if line[0] != ">":
        outline = ""
        for aa in line:
            outline += prot2nt[aa]
            sys.stdout.write(outline)
