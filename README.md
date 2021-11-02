# Bioinformatics

This is a repository of all the algorithms covered in the **Bioinformatics Course** part of the **Cambridge Computer Science Tripos**

# Algorithms Implemented:

**Alignment Problems:**
- [x] [Needleman-Wunsch](algorithms/needleman_wunsch.py)
  - [ ] Calculate LCS and Edit Distance using this approach
- [x] [Waterman-Smith](algorithms/waterman_smith.py)
- [ ] Nussinov RNA Folding
- [x] [Method of Four Russians for LCS](algorithms/four_russians_binary_encoding.py)
  - [ ] Extend to Edit Distance and Alignment


# Additional Files Explained:
- [Demos](demos.py) - **A list of functions that can be used to demo the algorithms**
- [Scoring Matrix](algorithms/scoring_matrices.py) - Stores different scoring matrices to use in alignment problems
- [Alignment-Graph](algorithms/alignment_graph.py)- A class for representing alignment/edit graphs
- [Rosalind](algorithms/rosalind.py) - Helper functions and playground for solving **[Rosalind](http://rosalind.info/problems/list-view/?location=bioinformatics-textbook-track) Questions**