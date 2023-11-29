from hepdata_lib import Submission
submission = Submission()
submission.read_abstract("example_inputs/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/SMP-22-007/")

from hepdata_lib import RootFileReader
reader = RootFileReader("lundDataAK8_hepData.root")
lundPlaneAK8 = reader.read_hist_2d("primaryLundPlaneDensityAK8")


from hepdata_lib import Submission, Variable, Table

# Create variable objects
x = Variable("First Bin", is_independent=True, is_binned=True)
x.values = lundPlaneAK8["x_edges"]

y = Variable("Second Bin", is_independent=True, is_binned=True)
y.values = lundPlaneAK8["y_edges"]

rho = Variable("Average emission density", is_independent=False, is_binned=False)
rho.values = lundPlaneAK8["z"]

table = Table("Emission density")
for var in [x,y,rho]:
	table.add_variable(var)

submission.add_table(table)
submission.create_files('./output_testie2/')
