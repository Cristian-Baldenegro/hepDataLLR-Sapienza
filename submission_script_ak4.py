from hepdata_lib import Submission
submission = Submission()
submission.read_abstract("example_inputs/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/SMP-22-007/")
submission.add_record_id(1234567, "inspire")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:AB.CDEFG")

from hepdata_lib import RootFileReader
reader = RootFileReader("lundDataAK4_hepData.root")
lundPlaneAK4 = reader.read_hist_2d("lundplaneUnfoldedAK4")

from hepdata_lib import Submission, Variable, Table

# Create variable objects
x = Variable("First Bin", is_independent=True, is_binned=True)
x.values = lundPlaneAK4["x_edges"]

y = Variable("Second Bin", is_independent=True, is_binned=True)
y.values = lundPlaneAK4["y_edges"]

rho = Variable("Average emission density", is_independent=False, is_binned=False)
rho.values = lundPlaneAK4["z"]

table = Table("Average primary Lund plane density for AK4 jets")
for var in [x,y,rho]:
	table.add_variable(var)
table.keywords["observables"] = ["rho(kT, DeltaR)"]
table.keywords["reactions"] = ["P P --> JETS"]
table.keywords["center-of-mass energy"] = ["13 TeV"]
submission.add_table(table)


#covariance matrix, statistical uncertainties

readerAK4StatUncertainties = RootFileReader("totCov_unfolded_hepData_ak4.root")
covarianceMatrixStatsAK4 = readerAK4StatUncertainties.read_hist_2d("covarianceMatrixStats_histogram")

# Create variable objects
xCovStatsAK4 = Variable("First bin", is_independent=True, is_binned=True)
xCovStatsAK4.values = covarianceMatrixStatsAK4["x_edges"]

yCovStatsAK4 = Variable("Second bin", is_independent=True, is_binned=True)
yCovStatsAK4.values = covarianceMatrixStatsAK4["y_edges"]

covMatrixStatsValue = Variable("covariance matrix entry", is_independent=False, is_binned=False)
covMatrixStatsValue.values = covarianceMatrixStatsAK4["z"]

tableCovMatrixStatsAK4 = Table("Covariance matrix of stat. uncertainties AK4 jets")
for var in [xCovStatsAK4,yCovStatsAK4, covMatrixStatsValue]:
        tableCovMatrixStatsAK4.add_variable(var)

submission.add_table(tableCovMatrixStatsAK4)


#covariance matrix, response statistical uncertainties

readerAK4ResponseStatUncertainties = RootFileReader("totCov_unfolded_hepData_responseStats_ak4.root")
covarianceMatrixResponseStatsAK4 = readerAK4ResponseStatUncertainties.read_hist_2d("covarianceMatrixResponseStats_histogram")

# Create variable objects
xCovResponseStatsAK4 = Variable("First bin", is_independent=True, is_binned=True)
xCovResponseStatsAK4.values = covarianceMatrixResponseStatsAK4["x_edges"]

yCovResponseStatsAK4 = Variable("Second bin", is_independent=True, is_binned=True)
yCovResponseStatsAK4.values = covarianceMatrixResponseStatsAK4["y_edges"]

covMatrixResponseStatsValue = Variable("covariance matrix entry", is_independent=False, is_binned=False)
covMatrixResponseStatsValue.values = covarianceMatrixResponseStatsAK4["z"]

tableCovMatrixResponseStatsAK4 = Table("Covariance matrix of response matrix stat. unc. for AK4 jets")
for var in [xCovResponseStatsAK4,yCovResponseStatsAK4, covMatrixResponseStatsValue]:
        tableCovMatrixResponseStatsAK4.add_variable(var)

submission.add_table(tableCovMatrixResponseStatsAK4)

#total covariance matrix, it's the sum of all covariance matrices

readerAK4totalCov = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4totalCov = readerAK4totalCov.read_hist_2d("covarianceMatrix_histogram")

# Create variable objects
xCovAK4totalCov = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4totalCov.values = covarianceAK4totalCov["x_edges"]

yCovAK4totalCov = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4totalCov.values = covarianceAK4totalCov["y_edges"]


covarianceAK4totalCovValue = Variable("Total covariance matrix for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4totalCovValue.values = covarianceAK4totalCov["z"]

tableCovMatrixAK4totalCov = Table("Total covariance matrix for AK4 jets")
for var in [xCovAK4totalCov,yCovAK4totalCov, covarianceAK4totalCovValue]:
        tableCovMatrixAK4totalCov.add_variable(var)

submission.add_table(tableCovMatrixAK4totalCov)

#covariance matrix, prior bias variation with response matrix fixed 

readerAK4Prior = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4Prior = readerAK4Prior.read_hist_2d("covarianceMatrixPrior_histogram")

# Create variable objects
xCovAK4Prior = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4Prior.values = covarianceAK4Prior["x_edges"]

yCovAK4Prior = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4Prior.values = covarianceAK4Prior["y_edges"]


covarianceAK4PriorValue = Variable("Covariance matrix for prior bias variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4PriorValue.values = covarianceAK4Prior["z"]

tableCovMatrixAK4Prior = Table("Covariance matrix for prior bias variation for AK4 jets")
for var in [xCovAK4Prior,yCovAK4Prior, covarianceAK4PriorValue]:
        tableCovMatrixAK4Prior.add_variable(var)

submission.add_table(tableCovMatrixAK4Prior)

#covariance matrix, response matrix variation

readerAK4Response = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4Response = readerAK4Response.read_hist_2d("covarianceMatrixResponse_histogram")

# Create variable objects
xCovAK4Response = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4Response.values = covarianceAK4Response["x_edges"]

yCovAK4Response = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4Response.values = covarianceAK4Response["y_edges"]


covarianceAK4ResponseValue = Variable("Covariance matrix for response matrix variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4ResponseValue.values = covarianceAK4Response["z"]

tableCovMatrixAK4Response = Table("Covariance matrix for response matrix variation for AK4 jets")
for var in [xCovAK4Response,yCovAK4Response, covarianceAK4ResponseValue]:
        tableCovMatrixAK4Response.add_variable(var)

submission.add_table(tableCovMatrixAK4Response)

#covariance matrix, JEC up

readerAK4JECup = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4JECup = readerAK4JECup.read_hist_2d("covarianceMatrixJECup_histogram")

# Create variable objects
xCovAK4JECup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4JECup.values = covarianceAK4JECup["x_edges"]

yCovAK4JECup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4JECup.values = covarianceAK4JECup["y_edges"]


covarianceAK4JECupValue = Variable("Covariance matrix for JEC up variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4JECupValue.values = covarianceAK4JECup["z"]

tableCovMatrixAK4JECup = Table("Covariance matrix for JEC up variation for AK4 jets")
for var in [xCovAK4JECup,yCovAK4JECup, covarianceAK4JECupValue]:
        tableCovMatrixAK4JECup.add_variable(var)

submission.add_table(tableCovMatrixAK4JECup)

#covariance matrix, JEC down

readerAK4JECdown = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4JECdown = readerAK4JECdown.read_hist_2d("covarianceMatrixJECdown_histogram")

# Create variable objects
xCovAK4JECdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4JECdown.values = covarianceAK4JECdown["x_edges"]

yCovAK4JECdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4JECdown.values = covarianceAK4JECdown["y_edges"]


covarianceAK4JECdownValue = Variable("Covariance matrix for JEC down variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4JECdownValue.values = covarianceAK4JECdown["z"]

tableCovMatrixAK4JECdown = Table("Covariance matrix for JEC down variation for AK4 jets")
for var in [xCovAK4JECdown,yCovAK4JECdown, covarianceAK4JECdownValue]:
        tableCovMatrixAK4JECdown.add_variable(var)

submission.add_table(tableCovMatrixAK4JECdown)


#covariance matrix, JER down

readerAK4JERdown = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4JERdown = readerAK4JERdown.read_hist_2d("covarianceMatrixJERdown_histogram")

# Create variable objects
xCovAK4JERdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4JERdown.values = covarianceAK4JERdown["x_edges"]

yCovAK4JERdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4JERdown.values = covarianceAK4JERdown["y_edges"]

covarianceAK4JERdownValue = Variable("Covariance matrix for JER down variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4JERdownValue.values = covarianceAK4JERdown["z"]

tableCovMatrixAK4JERdown = Table("Covariance matrix for JER down variation for AK4 jets")
for var in [xCovAK4JERdown,yCovAK4JERdown, covarianceAK4JERdownValue]:
        tableCovMatrixAK4JERdown.add_variable(var)

submission.add_table(tableCovMatrixAK4JERdown)


#covariance matrix, JER up 

readerAK4JERup = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4JERup = readerAK4JERup.read_hist_2d("covarianceMatrixJERup_histogram")

# Create variable objects
xCovAK4JERup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4JERup.values = covarianceAK4JERup["x_edges"]

yCovAK4JERup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4JERup.values = covarianceAK4JERup["y_edges"]

covarianceAK4JERupValue = Variable("Covariance matrix for JER down variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4JERupValue.values = covarianceAK4JERup["z"]

tableCovMatrixAK4JERup = Table("Covariance matrix for JER down variation for AK4 jets")
for var in [xCovAK4JERup,yCovAK4JERup, covarianceAK4JERupValue]:
        tableCovMatrixAK4JERup.add_variable(var)

submission.add_table(tableCovMatrixAK4JERup)

#covariance matrix, PU down

readerAK4PUdown = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4PUdown = readerAK4PUdown.read_hist_2d("covarianceMatrixPUdown_histogram")

# Create variable objects
xCovAK4PUdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4PUdown.values = covarianceAK4PUdown["x_edges"]

yCovAK4PUdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4PUdown.values = covarianceAK4PUdown["y_edges"]

covarianceAK4PUdownValue = Variable("Covariance matrix for PU down variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4PUdownValue.values = covarianceAK4PUdown["z"]

tableCovMatrixAK4PUdown = Table("Covariance matrix for PU down variation for AK4 jets")
for var in [xCovAK4PUdown,yCovAK4PUdown, covarianceAK4PUdownValue]:
        tableCovMatrixAK4PUdown.add_variable(var)

submission.add_table(tableCovMatrixAK4PUdown)

#covariance matrix, PU up

readerAK4PUup = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4PUup = readerAK4PUup.read_hist_2d("covarianceMatrixPUup_histogram")

# Create variable objects
xCovAK4PUup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4PUup.values = covarianceAK4PUup["x_edges"]

yCovAK4PUup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4PUup.values = covarianceAK4PUup["y_edges"]

covarianceAK4PUupValue = Variable("Covariance matrix for PU up variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4PUupValue.values = covarianceAK4PUup["z"]

tableCovMatrixAK4PUup = Table("Covariance matrix for PU up variation for AK4 jets")
for var in [xCovAK4PUup,yCovAK4PUup, covarianceAK4PUupValue]:
        tableCovMatrixAK4PUup.add_variable(var)

submission.add_table(tableCovMatrixAK4PUup)


#covariance matrix, FSR down

readerAK4FSRdown = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4FSRdown = readerAK4FSRdown.read_hist_2d("covarianceMatrixFSRdown_histogram")

# Create variable objects
xCovAK4FSRdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4FSRdown.values = covarianceAK4FSRdown["x_edges"]

yCovAK4FSRdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4FSRdown.values = covarianceAK4FSRdown["y_edges"]

covarianceAK4FSRdownValue = Variable("Covariance matrix for FSR down variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4FSRdownValue.values = covarianceAK4FSRdown["z"]

tableCovMatrixAK4FSRdown = Table("Covariance matrix for FSR down variation for AK4 jets")
for var in [xCovAK4FSRdown,yCovAK4FSRdown, covarianceAK4FSRdownValue]:
        tableCovMatrixAK4FSRdown.add_variable(var)

submission.add_table(tableCovMatrixAK4FSRdown)


#covariance matrix, FSR up

readerAK4FSRup = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4FSRup = readerAK4FSRup.read_hist_2d("covarianceMatrixFSRup_histogram")

# Create variable objects
xCovAK4FSRup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4FSRup.values = covarianceAK4FSRup["x_edges"]

yCovAK4FSRup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4FSRup.values = covarianceAK4FSRup["y_edges"]

covarianceAK4FSRupValue = Variable("Covariance matrix for FSR down variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4FSRupValue.values = covarianceAK4FSRup["z"]

tableCovMatrixAK4FSRup = Table("Covariance matrix for FSR down variation for AK4 jets")
for var in [xCovAK4FSRup,yCovAK4FSRup, covarianceAK4FSRupValue]:
        tableCovMatrixAK4FSRup.add_variable(var)

submission.add_table(tableCovMatrixAK4FSRup)

#covariance matrix, ISR down

readerAK4ISRdown = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4ISRdown = readerAK4ISRdown.read_hist_2d("covarianceMatrixISRdown_histogram")

# Create variable objects
xCovAK4ISRdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4ISRdown.values = covarianceAK4ISRdown["x_edges"]

yCovAK4ISRdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4ISRdown.values = covarianceAK4ISRdown["y_edges"]

covarianceAK4ISRdownValue = Variable("Covariance matrix for ISR down variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4ISRdownValue.values = covarianceAK4ISRdown["z"]

tableCovMatrixAK4ISRdown = Table("Covariance matrix for ISR down variation for AK4 jets")
for var in [xCovAK4ISRdown,yCovAK4ISRdown, covarianceAK4ISRdownValue]:
        tableCovMatrixAK4ISRdown.add_variable(var)

submission.add_table(tableCovMatrixAK4ISRdown)


#covariance matrix, ISR up

readerAK4ISRup = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4ISRup = readerAK4ISRup.read_hist_2d("covarianceMatrixISRup_histogram")

# Create variable objects
xCovAK4ISRup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4ISRup.values = covarianceAK4ISRup["x_edges"]

yCovAK4ISRup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4ISRup.values = covarianceAK4ISRup["y_edges"]

covarianceAK4ISRupValue = Variable("Covariance matrix for ISR up variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4ISRupValue.values = covarianceAK4ISRup["z"]

tableCovMatrixAK4ISRup = Table("Covariance matrix for ISR up variation for AK4 jets")
for var in [xCovAK4ISRup,yCovAK4ISRup, covarianceAK4ISRupValue]:
        tableCovMatrixAK4ISRup.add_variable(var)

submission.add_table(tableCovMatrixAK4ISRup)


#covariance matrix, FSR down ISR down

readerAK4FSRdownISRdown = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4FSRdownISRdown = readerAK4FSRdownISRdown.read_hist_2d("covarianceMatrixFSRdownISRdown_histogram")

# Create variable objects
xCovAK4FSRdownISRdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4FSRdownISRdown.values = covarianceAK4FSRdownISRdown["x_edges"]

yCovAK4FSRdownISRdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4FSRdownISRdown.values = covarianceAK4FSRdownISRdown["y_edges"]

covarianceAK4FSRdownISRdownValue = Variable("Covariance matrix for FSR down ISR down variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4FSRdownISRdownValue.values = covarianceAK4FSRdownISRdown["z"]

tableCovMatrixAK4FSRdownISRdown = Table("Covariance matrix for FSR down ISR down variation for AK4 jets")
for var in [xCovAK4FSRdownISRdown,yCovAK4FSRdownISRdown, covarianceAK4FSRdownISRdownValue]:
        tableCovMatrixAK4FSRdownISRdown.add_variable(var)

submission.add_table(tableCovMatrixAK4FSRdownISRdown)


#covariance matrix, FSR up ISR up

readerAK4FSRupISRup = RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4FSRupISRup = readerAK4FSRupISRup.read_hist_2d("covarianceMatrixFSRupISRup_histogram")

# Create variable objects
xCovAK4FSRupISRup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4FSRupISRup.values = covarianceAK4FSRupISRup["x_edges"]

yCovAK4FSRupISRup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4FSRupISRup.values = covarianceAK4FSRupISRup["y_edges"]

covarianceAK4FSRupISRupValue = Variable("Covariance matrix for FSR up ISR up variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4FSRupISRupValue.values = covarianceAK4FSRupISRup["z"]

tableCovMatrixAK4FSRupISRup = Table("Covariance matrix for FSR up ISR up variation for AK4 jets")
for var in [xCovAK4FSRupISRup,yCovAK4FSRupISRup, covarianceAK4FSRupISRupValue]:
        tableCovMatrixAK4FSRupISRup.add_variable(var)

submission.add_table(tableCovMatrixAK4FSRupISRup)


#covariance matrix, track inefficiency (2016 decorrelated piece) 

readerAK4TrackIneff2016= RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4TrackIneff2016 = readerAK4TrackIneff2016.read_hist_2d("covarianceMatrixTrackIneff2016_histogram")

# Create variable objects
xCovAK4TrackIneff2016 = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4TrackIneff2016.values = covarianceAK4TrackIneff2016["x_edges"]

yCovAK4TrackIneff2016= Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4TrackIneff2016.values = covarianceAK4TrackIneff2016["y_edges"]

covarianceAK4TrackIneff2016Value = Variable("Cov. matrix for 2016 tracking eff. for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4TrackIneff2016Value.values = covarianceAK4TrackIneff2016["z"]

tableCovMatrixAK4TrackIneff2016 = Table("Cov. matrix for 2016 tracking eff. for AK4 jets")
for var in [xCovAK4TrackIneff2016,yCovAK4TrackIneff2016, covarianceAK4TrackIneff2016Value]:
        tableCovMatrixAK4TrackIneff2016.add_variable(var)

submission.add_table(tableCovMatrixAK4TrackIneff2016)

#covariance matrix, track inefficiency (20178 decorrelated piece) 

readerAK4TrackIneff20178= RootFileReader("covarianceMatrix_systematic_ak4.root")
covarianceAK4TrackIneff20178 = readerAK4TrackIneff20178.read_hist_2d("covarianceMatrixTrackIneff20178_histogram")

# Create variable objects
xCovAK4TrackIneff20178 = Variable("First bin", is_independent=True, is_binned=True)
xCovAK4TrackIneff20178.values = covarianceAK4TrackIneff20178["x_edges"]

yCovAK4TrackIneff20178= Variable("Second bin", is_independent=True, is_binned=True)
yCovAK4TrackIneff20178.values = covarianceAK4TrackIneff20178["y_edges"]

covarianceAK4TrackIneff20178Value = Variable("Cov. matrix for 2017-2018 tracking eff. for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4TrackIneff20178Value.values = covarianceAK4TrackIneff20178["z"]

tableCovMatrixAK4TrackIneff20178 = Table("Cov. matrix for 2017-2018 tracking eff. for AK4 jets")
for var in [xCovAK4TrackIneff20178,yCovAK4TrackIneff20178, covarianceAK4TrackIneff20178Value]:
        tableCovMatrixAK4TrackIneff20178.add_variable(var)

submission.add_table(tableCovMatrixAK4TrackIneff20178)

submission.create_files('./output_testie_ak4/')
