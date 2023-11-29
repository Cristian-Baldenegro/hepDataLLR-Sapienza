from hepdata_lib import Submission
submission = Submission()
submission.read_abstract("example_inputs/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/SMP-22-007/")
submission.add_record_id(1234567, "inspire")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:AB.CDEFG")

from hepdata_lib import RootFileReader
reader = RootFileReader("lundDataAK8_hepData.root")
lundPlaneAK8 = reader.read_hist_2d("lundplaneUnfoldedAK8")

from hepdata_lib import Submission, Variable, Table

# Create variable objects
x = Variable("ln(R/DeltaR)", is_independent=True, is_binned=True)
x.values = lundPlaneAK8["x_edges"]

y = Variable("ln(kT/GeV)", is_independent=True, is_binned=True)
y.values = lundPlaneAK8["y_edges"]

rho = Variable("Average Lund plane density", is_independent=False, is_binned=False)
rho.values = lundPlaneAK8["z"]

table = Table("Average primary Lund plane density for AK8 jets")
for var in [x,y,rho]:
	table.add_variable(var)
table.keywords["observables"] = ["rho(kT, DeltaR)"]
table.keywords["reactions"] = ["P P --> JETS"]
table.keywords["cmenergies"] = ["13000"]
submission.add_table(table)

#lundPlaneAK8_1D = reader.read_hist_1d("recoall1D")


#x1D = Variable("Bin index", is_independent=True, is_binned=False)
#x1D.values = lundPlaneAK8_1D["x"]
##rho1D = Variable("Average density for AK8 jets in 1D", is_independent=True, is_binned=False)
#rho1D.values = lundPlaneAK8_1D["y"]

#table1D = Table("Average primary Lund plane density for AK8 jets for 1D")
#for var in [x1D,rho1D]:
#        table.add_variable(var)
#table1D.keywords["observables"] = ["rho(kT, DeltaR)"]
#table1D.keywords["reactions"] = ["P P --> JETS"]
#table1D.keywords["cmenergies"] = ["13000"]
#submission.add_table(table1D)

from hepdata_lib import Uncertainty


submission.create_files('./outputSMP22007/')
