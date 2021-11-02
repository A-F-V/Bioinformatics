# Bioinformatics

This is a repository of all the algorithms covered in the **Bioinformatics Course** part of the **Cambridge Computer Science Tripos**

# Algorithms Implemented:
- [x] Needleman-Wunsch
  - [ ] Calculate LCS and Edit Distance using this approach
- [x] Waterman-Smith
- [ ] Nussinov RNA Folding
- [x] Method of Four Russians for LCS
  - [ ] Extend to Edit Distance and Alignment


# Files Explained:
- [Demos](demos.py) - **A list of functions that can be used to demo the algorithms**
- [Scoring_Matrix](algorithms/scoring_matrices.py) - Stores different scoring matrices to use in alignment problems
- [Alignment-Graph](algorithms/alignment_graph.py)- A class for representing alignment/edit graphs
- [Waterman-Smith](algorithms/waterman-smith.py) - Implementation for Waterman-Smith alignment
- [Needleman-Wunsch](algorithms/needleman_wunsch.py) - Implementation for Needleman-Wunsch
- [Four Russians Binary Encoding](algorithms/four_russians_binary_encoding.py) - A four russians sped up LCS (#todo edit distance and alignment)