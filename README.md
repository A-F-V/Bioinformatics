![](logos/logo.png)

[![CodeFactor](https://www.codefactor.io/repository/github/a-f-v/bioinformatics/badge)](https://www.codefactor.io/repository/github/a-f-v/bioinformatics)
[![Run Python Tests](https://github.com/A-F-V/Bioinformatics/actions/workflows/actions.yml/badge.svg)](https://github.com/A-F-V/Bioinformatics/actions/workflows/actions.yml)

---

This is a repository of all the algorithms covered in the **Bioinformatics Course** part of the **Cambridge Computer Science Tripos**

# Algorithms Implemented:

### **Alignment Problems:**
- [x] [Needleman-Wunsch](src/algorithms/needleman_wunsch.py)
  - [ ] Calculate LCS and Edit Distance using this approach
- [x] [Waterman-Smith](src/algorithms/waterman_smith.py)
- [ ] Nussinov RNA Folding
- [ ] Space Efficient Global Alignment (#todo cleanup)
- [x] [Method of Four Russians for LCS](src/algorithms/four_russians_binary_encoding.py)
  - [ ] Extend to Edit Distance, Block Alignment and Global Alignment (for very simple score matrices)

### **Phylogeny (Evolutionary Tree) Algorithms**:
- [x] [Limb Length](src/algorithms/limb_length.py) - O(n^2) and O(n) solutions
- [x] [Additive Phylogeny](src/algorithms/additive_phylogeny.py)
- [x] [UPGMA](src/algorithms/upgma.py) - O(N^2 log(n)) solution using priority queue
- [x] [Neighbour Joining](src/algorithms/neighbour_joining.py)

# Additional Files Explained:
- [Demos](src/demos.py) - **A list of functions that can be used to demo the algorithms**
- [Scoring Functions](src/algorithms/scoring_functions.py) - Stores different scoring matrices encapsulated into a function to use in alignment problems
- [Alignment-Graph](src/algorithms/alignment_graph.py)- A class for representing alignment/edit graphs
- [Rosalind](src/rosalind) - Answers to the **[Rosalind](http://rosalind.info/problems/list-view/?location=bioinformatics-textbook-track) Questions**
