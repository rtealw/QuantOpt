import quantum_query_optimizer as qqo
# For development testing
#import sys
#sys.path.append('quantum_query_optimizer')
#import __init__ as qqo

# Example 1
D = ['00', '01', '10', '11']
E = ['0', '1', '1', '1']
qqo.runSDP(D=D, E=E)

# Example 2
solutions = qqo.runSDPForN(getD=qqo.getDAll, getE=qqo.getERandom, n_end=2, n_start=2)

## Additional Example: Generate Figures
#all_solutions = qqo.runSDPForN(getD=qqo.getDAll, getE=qqo.getEOR, n_end=5, n_start=1)
#qqo.visualizeRuntime(all_solutions, title="Runtime of OR by Input Size for All Inputs", filename="figures/or_all_runtime.eps")
#qqo.visualizeComplexity(all_solutions, title="Complexity of OR by Input Size for All Inputs", filename="figures/or_all_complexity.eps")
#
#worst_solutions = qqo.runSDPForN(getD=qqo.getDWorstOR, getE=qqo.getEOR, n_end=14, n_start=1)
#qqo.visualizeRuntime(worst_solutions, title="Runtime of OR by Input Size for Worse Inputs", filename="figures/or_worst_runtime.eps")
#qqo.visualizeComplexity(worst_solutions, title="Complexity of OR by Input Size for Worse Inputs", filename="figures/or_worst_complexity.eps")

# For development testing
## Additional Example: Paper Figures
#all_solutions = qqo.runSDPForN(getD=qqo.getDAll, getE=qqo.getEOR, n_end=6, n_start=1)
#worst_solutions = qqo.runSDPForN(getD=qqo.getDWorstOR, getE=qqo.getEOR, n_end=6, n_start=1)
#qqo.visualizeComplexityOR(all_solutions, title="Complexity of OR by Input Size", filename='figures/or_complexity.eps')
#qqo.visualizeRuntimeOR(all_solutions, worst_solutions, title="Runtime of OR by Input Size", filename='figures/or_runtime.eps')
