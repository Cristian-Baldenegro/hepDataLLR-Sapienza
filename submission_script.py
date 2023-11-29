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
x = Variable("First Bin", is_independent=True, is_binned=True)
x.values = lundPlaneAK8["x_edges"]

y = Variable("Second Bin", is_independent=True, is_binned=True)
y.values = lundPlaneAK8["y_edges"]

rho = Variable("Average emission density", is_independent=False, is_binned=False)
rho.values = lundPlaneAK8["z"]

table = Table("Average primary Lund plane density for AK8 jets")
for var in [x,y,rho]:
	table.add_variable(var)
table.keywords["observables"] = ["rho(kT, DeltaR)"]
table.keywords["reactions"] = ["P P --> JETS"]
table.keywords["cmenergies"] = ["13000"]
submission.add_table(table)


#covariance matrix, statistical uncertainties

readerAK8StatUncertainties = RootFileReader("totCov_unfolded_hepData_ak8.root")
covarianceMatrixStatsAK8 = readerAK8StatUncertainties.read_hist_2d("covarianceMatrixStats_histogram")

# Create variable objects
xCovStatsAK8 = Variable("First bin", is_independent=True, is_binned=True)
xCovStatsAK8.values = covarianceMatrixStatsAK8["x_edges"]

yCovStatsAK8 = Variable("Second bin", is_independent=True, is_binned=True)
yCovStatsAK8.values = covarianceMatrixStatsAK8["y_edges"]

covMatrixStatsValue = Variable("covariance matrix entry", is_independent=False, is_binned=False)
covMatrixStatsValue.values = covarianceMatrixStatsAK8["z"]

tableCovMatrixStatsAK8 = Table("Covariance matrix of stat. uncertainties AK8 jets")
for var in [xCovStatsAK8,yCovStatsAK8, covMatrixStatsValue]:
        tableCovMatrixStatsAK8.add_variable(var)

submission.add_table(tableCovMatrixStatsAK8)


#covariance matrix, response statistical uncertainties

readerAK8ResponseStatUncertainties = RootFileReader("totCov_unfolded_hepData_response_ak8.root")
covarianceMatrixResponseStatsAK8 = readerAK8ResponseStatUncertainties.read_hist_2d("covarianceMatrixStats_histogram")

# Create variable objects
xCovResponseStatsAK8 = Variable("First bin", is_independent=True, is_binned=True)
xCovResponseStatsAK8.values = covarianceMatrixResponseStatsAK8["x_edges"]

yCovResponseStatsAK8 = Variable("Second bin", is_independent=True, is_binned=True)
yCovResponseStatsAK8.values = covarianceMatrixResponseStatsAK8["y_edges"]

covMatrixResponseStatsValue = Variable("covariance matrix entry", is_independent=False, is_binned=False)
covMatrixResponseStatsValue.values = covarianceMatrixResponseStatsAK8["z"]

tableCovMatrixResponseStatsAK8 = Table("Covariance matrix of response matrix stat. unc. for AK8 jets")
for var in [xCovResponseStatsAK8,yCovResponseStatsAK8, covMatrixResponseStatsValue]:
        tableCovMatrixResponseStatsAK8.add_variable(var)

submission.add_table(tableCovMatrixResponseStatsAK8)

#total covariance matrix, it's the sum of all covariance matrices

readerAK8totalCov = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8totalCov = readerAK8totalCov.read_hist_2d("covarianceMatrix_histogram")

# Create variable objects
xCovAK8totalCov = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8totalCov.values = covarianceAK8totalCov["x_edges"]

yCovAK8totalCov = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8totalCov.values = covarianceAK8totalCov["y_edges"]


covarianceAK8totalCovValue = Variable("Total covariance matrix for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8totalCovValue.values = covarianceAK8totalCov["z"]

tableCovMatrixAK8totalCov = Table("Total covariance matrix for AK8 jets")
for var in [xCovAK8totalCov,yCovAK8totalCov, covarianceAK8totalCovValue]:
        tableCovMatrixAK8totalCov.add_variable(var)

submission.add_table(tableCovMatrixAK8totalCov)

#covariance matrix, prior bias variation with response matrix fixed 

readerAK8Prior = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8Prior = readerAK8Prior.read_hist_2d("covarianceMatrixPrior_histogram")

# Create variable objects
xCovAK8Prior = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8Prior.values = covarianceAK8Prior["x_edges"]

yCovAK8Prior = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8Prior.values = covarianceAK8Prior["y_edges"]


covarianceAK8PriorValue = Variable("Covariance matrix for prior bias variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8PriorValue.values = covarianceAK8Prior["z"]

tableCovMatrixAK8Prior = Table("Covariance matrix for prior bias variation for AK8 jets")
for var in [xCovAK8Prior,yCovAK8Prior, covarianceAK8PriorValue]:
        tableCovMatrixAK8Prior.add_variable(var)

submission.add_table(tableCovMatrixAK8Prior)

#covariance matrix, response matrix variation

readerAK8Response = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8Response = readerAK8Response.read_hist_2d("covarianceMatrixResponse_histogram")

# Create variable objects
xCovAK8Response = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8Response.values = covarianceAK8Response["x_edges"]

yCovAK8Response = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8Response.values = covarianceAK8Response["y_edges"]


covarianceAK8ResponseValue = Variable("Covariance matrix for response matrix variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8ResponseValue.values = covarianceAK8Response["z"]

tableCovMatrixAK8Response = Table("Covariance matrix for response matrix variation for AK8 jets")
for var in [xCovAK8Response,yCovAK8Response, covarianceAK8ResponseValue]:
        tableCovMatrixAK8Response.add_variable(var)

submission.add_table(tableCovMatrixAK8Response)

#covariance matrix, JEC up

readerAK8JECup = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8JECup = readerAK8JECup.read_hist_2d("covarianceMatrixJECup_histogram")

# Create variable objects
xCovAK8JECup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8JECup.values = covarianceAK8JECup["x_edges"]

yCovAK8JECup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8JECup.values = covarianceAK8JECup["y_edges"]


covarianceAK8JECupValue = Variable("Covariance matrix for JEC up variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8JECupValue.values = covarianceAK8JECup["z"]

tableCovMatrixAK8JECup = Table("Covariance matrix for JEC up variation for AK8 jets")
for var in [xCovAK8JECup,yCovAK8JECup, covarianceAK8JECupValue]:
        tableCovMatrixAK8JECup.add_variable(var)

submission.add_table(tableCovMatrixAK8JECup)

#covariance matrix, JEC down

readerAK8JECdown = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8JECdown = readerAK8JECdown.read_hist_2d("covarianceMatrixJECdown_histogram")

# Create variable objects
xCovAK8JECdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8JECdown.values = covarianceAK8JECdown["x_edges"]

yCovAK8JECdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8JECdown.values = covarianceAK8JECdown["y_edges"]


covarianceAK8JECdownValue = Variable("Covariance matrix for JEC down variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8JECdownValue.values = covarianceAK8JECdown["z"]

tableCovMatrixAK8JECdown = Table("Covariance matrix for JEC down variation for AK8 jets")
for var in [xCovAK8JECdown,yCovAK8JECdown, covarianceAK8JECdownValue]:
        tableCovMatrixAK8JECdown.add_variable(var)

submission.add_table(tableCovMatrixAK8JECdown)


#covariance matrix, JER down

readerAK8JERdown = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8JERdown = readerAK8JERdown.read_hist_2d("covarianceMatrixJERdown_histogram")

# Create variable objects
xCovAK8JERdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8JERdown.values = covarianceAK8JERdown["x_edges"]

yCovAK8JERdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8JERdown.values = covarianceAK8JERdown["y_edges"]

covarianceAK8JERdownValue = Variable("Covariance matrix for JER down variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8JERdownValue.values = covarianceAK8JERdown["z"]

tableCovMatrixAK8JERdown = Table("Covariance matrix for JER down variation for AK8 jets")
for var in [xCovAK8JERdown,yCovAK8JERdown, covarianceAK8JERdownValue]:
        tableCovMatrixAK8JERdown.add_variable(var)

submission.add_table(tableCovMatrixAK8JERdown)


#covariance matrix, JER up 

readerAK8JERup = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8JERup = readerAK8JERup.read_hist_2d("covarianceMatrixJERup_histogram")

# Create variable objects
xCovAK8JERup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8JERup.values = covarianceAK8JERup["x_edges"]

yCovAK8JERup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8JERup.values = covarianceAK8JERup["y_edges"]

covarianceAK8JERupValue = Variable("Covariance matrix for JER up variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8JERupValue.values = covarianceAK8JERup["z"]

tableCovMatrixAK8JERup = Table("Covariance matrix for JER up variation for AK8 jets")
for var in [xCovAK8JERup,yCovAK8JERup, covarianceAK8JERupValue]:
        tableCovMatrixAK8JERup.add_variable(var)

submission.add_table(tableCovMatrixAK8JERup)

#covariance matrix, PU down

readerAK8PUdown = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8PUdown = readerAK8PUdown.read_hist_2d("covarianceMatrixPUdown_histogram")

# Create variable objects
xCovAK8PUdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8PUdown.values = covarianceAK8PUdown["x_edges"]

yCovAK8PUdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8PUdown.values = covarianceAK8PUdown["y_edges"]

covarianceAK8PUdownValue = Variable("Covariance matrix for PU down variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8PUdownValue.values = covarianceAK8PUdown["z"]

tableCovMatrixAK8PUdown = Table("Covariance matrix for PU down variation for AK8 jets")
for var in [xCovAK8PUdown,yCovAK8PUdown, covarianceAK8PUdownValue]:
        tableCovMatrixAK8PUdown.add_variable(var)

submission.add_table(tableCovMatrixAK8PUdown)

#covariance matrix, PU up

readerAK8PUup = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8PUup = readerAK8PUup.read_hist_2d("covarianceMatrixPUup_histogram")

# Create variable objects
xCovAK8PUup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8PUup.values = covarianceAK8PUup["x_edges"]

yCovAK8PUup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8PUup.values = covarianceAK8PUup["y_edges"]

covarianceAK8PUupValue = Variable("Covariance matrix for PU up variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8PUupValue.values = covarianceAK8PUup["z"]

tableCovMatrixAK8PUup = Table("Covariance matrix for PU up variation for AK8 jets")
for var in [xCovAK8PUup,yCovAK8PUup, covarianceAK8PUupValue]:
        tableCovMatrixAK8PUup.add_variable(var)

submission.add_table(tableCovMatrixAK8PUup)


#covariance matrix, FSR down

readerAK8FSRdown = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8FSRdown = readerAK8FSRdown.read_hist_2d("covarianceMatrixFSRdown_histogram")

# Create variable objects
xCovAK8FSRdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8FSRdown.values = covarianceAK8FSRdown["x_edges"]

yCovAK8FSRdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8FSRdown.values = covarianceAK8FSRdown["y_edges"]

covarianceAK8FSRdownValue = Variable("Covariance matrix for FSR down variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8FSRdownValue.values = covarianceAK8FSRdown["z"]

tableCovMatrixAK8FSRdown = Table("Covariance matrix for FSR down variation for AK8 jets")
for var in [xCovAK8FSRdown,yCovAK8FSRdown, covarianceAK8FSRdownValue]:
        tableCovMatrixAK8FSRdown.add_variable(var)

submission.add_table(tableCovMatrixAK8FSRdown)


#covariance matrix, FSR up

readerAK8FSRup = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8FSRup = readerAK8FSRup.read_hist_2d("covarianceMatrixFSRup_histogram")

# Create variable objects
xCovAK8FSRup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8FSRup.values = covarianceAK8FSRup["x_edges"]

yCovAK8FSRup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8FSRup.values = covarianceAK8FSRup["y_edges"]

covarianceAK8FSRupValue = Variable("Covariance matrix for FSR up variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8FSRupValue.values = covarianceAK8FSRup["z"]

tableCovMatrixAK8FSRup = Table("Covariance matrix for FSR up variation for AK8 jets")
for var in [xCovAK8FSRup,yCovAK8FSRup, covarianceAK8FSRupValue]:
        tableCovMatrixAK8FSRup.add_variable(var)

submission.add_table(tableCovMatrixAK8FSRup)

#covariance matrix, ISR down

readerAK8ISRdown = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8ISRdown = readerAK8ISRdown.read_hist_2d("covarianceMatrixISRdown_histogram")

# Create variable objects
xCovAK8ISRdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8ISRdown.values = covarianceAK8ISRdown["x_edges"]

yCovAK8ISRdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8ISRdown.values = covarianceAK8ISRdown["y_edges"]

covarianceAK8ISRdownValue = Variable("Covariance matrix for ISR down variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8ISRdownValue.values = covarianceAK8ISRdown["z"]

tableCovMatrixAK8ISRdown = Table("Covariance matrix for ISR down variation for AK8 jets")
for var in [xCovAK8ISRdown,yCovAK8ISRdown, covarianceAK8ISRdownValue]:
        tableCovMatrixAK8ISRdown.add_variable(var)

submission.add_table(tableCovMatrixAK8ISRdown)


#covariance matrix, ISR up

readerAK8ISRup = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8ISRup = readerAK8ISRup.read_hist_2d("covarianceMatrixISRup_histogram")

# Create variable objects
xCovAK8ISRup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8ISRup.values = covarianceAK8ISRup["x_edges"]

yCovAK8ISRup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8ISRup.values = covarianceAK8ISRup["y_edges"]

covarianceAK8ISRupValue = Variable("Covariance matrix for ISR up variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8ISRupValue.values = covarianceAK8ISRup["z"]

tableCovMatrixAK8ISRup = Table("Covariance matrix for ISR up variation for AK8 jets")
for var in [xCovAK8ISRup,yCovAK8ISRup, covarianceAK8ISRupValue]:
        tableCovMatrixAK8ISRup.add_variable(var)

submission.add_table(tableCovMatrixAK8ISRup)


#covariance matrix, FSR down ISR down

readerAK8FSRdownISRdown = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8FSRdownISRdown = readerAK8FSRdownISRdown.read_hist_2d("covarianceMatrixFSRdownISRdown_histogram")

# Create variable objects
xCovAK8FSRdownISRdown = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8FSRdownISRdown.values = covarianceAK8FSRdownISRdown["x_edges"]

yCovAK8FSRdownISRdown = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8FSRdownISRdown.values = covarianceAK8FSRdownISRdown["y_edges"]

covarianceAK8FSRdownISRdownValue = Variable("Covariance matrix for FSR down ISR down variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8FSRdownISRdownValue.values = covarianceAK8FSRdownISRdown["z"]

tableCovMatrixAK8FSRdownISRdown = Table("Covariance matrix for FSR down ISR down variation for AK8 jets")
for var in [xCovAK8FSRdownISRdown,yCovAK8FSRdownISRdown, covarianceAK8FSRdownISRdownValue]:
        tableCovMatrixAK8FSRdownISRdown.add_variable(var)

submission.add_table(tableCovMatrixAK8FSRdownISRdown)


#covariance matrix, FSR up ISR up

readerAK8FSRupISRup = RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8FSRupISRup = readerAK8FSRupISRup.read_hist_2d("covarianceMatrixFSRupISRup_histogram")

# Create variable objects
xCovAK8FSRupISRup = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8FSRupISRup.values = covarianceAK8FSRupISRup["x_edges"]

yCovAK8FSRupISRup = Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8FSRupISRup.values = covarianceAK8FSRupISRup["y_edges"]

covarianceAK8FSRupISRupValue = Variable("Covariance matrix for FSR up ISR up variation for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8FSRupISRupValue.values = covarianceAK8FSRupISRup["z"]

tableCovMatrixAK8FSRupISRup = Table("Covariance matrix for FSR up ISR up variation for AK8 jets")
for var in [xCovAK8FSRupISRup,yCovAK8FSRupISRup, covarianceAK8FSRupISRupValue]:
        tableCovMatrixAK8FSRupISRup.add_variable(var)

submission.add_table(tableCovMatrixAK8FSRupISRup)


#covariance matrix, track inefficiency (2016 decorrelated piece) 

readerAK8TrackIneff2016= RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8TrackIneff2016 = readerAK8TrackIneff2016.read_hist_2d("covarianceMatrixTrackIneff2016_histogram")

# Create variable objects
xCovAK8TrackIneff2016 = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8TrackIneff2016.values = covarianceAK8TrackIneff2016["x_edges"]

yCovAK8TrackIneff2016= Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8TrackIneff2016.values = covarianceAK8TrackIneff2016["y_edges"]

covarianceAK8TrackIneff2016Value = Variable("Cov. matrix for 2016 tracking eff. for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8TrackIneff2016Value.values = covarianceAK8TrackIneff2016["z"]

tableCovMatrixAK8TrackIneff2016 = Table("Cov. matrix for 2016 tracking eff. for AK8 jets")
for var in [xCovAK8TrackIneff2016,yCovAK8TrackIneff2016, covarianceAK8TrackIneff2016Value]:
        tableCovMatrixAK8TrackIneff2016.add_variable(var)

submission.add_table(tableCovMatrixAK8TrackIneff2016)

#covariance matrix, track inefficiency (20178 decorrelated piece) 

readerAK8TrackIneff20178= RootFileReader("covarianceMatrix_systematic_ak8.root")
covarianceAK8TrackIneff20178 = readerAK8TrackIneff20178.read_hist_2d("covarianceMatrixTrackIneff20178_histogram")

# Create variable objects
xCovAK8TrackIneff20178 = Variable("First bin", is_independent=True, is_binned=True)
xCovAK8TrackIneff20178.values = covarianceAK8TrackIneff20178["x_edges"]

yCovAK8TrackIneff20178= Variable("Second bin", is_independent=True, is_binned=True)
yCovAK8TrackIneff20178.values = covarianceAK8TrackIneff20178["y_edges"]

covarianceAK8TrackIneff20178Value = Variable("Cov. matrix for 2017-2018 tracking eff. for AK8 jets", is_independent=False, is_binned=False)
covarianceAK8TrackIneff20178Value.values = covarianceAK8TrackIneff20178["z"]

tableCovMatrixAK8TrackIneff20178 = Table("Cov. matrix for 2017-2018 tracking eff. for AK8 jets")
for var in [xCovAK8TrackIneff20178,yCovAK8TrackIneff20178, covarianceAK8TrackIneff20178Value]:
        tableCovMatrixAK8TrackIneff20178.add_variable(var)

submission.add_table(tableCovMatrixAK8TrackIneff20178)

readerAK4 = RootFileReader("lundDataAK4_hepData.root")
lundPlaneAK4 = readerAK4.read_hist_2d("lundplaneUnfoldedAK4")

# Create variable objects
xAK4 = Variable("First Bin", is_independent=True, is_binned=True)
xAK4.values = lundPlaneAK4["x_edges"]

yAK4 = Variable("Second Bin", is_independent=True, is_binned=True)
yAK4.values = lundPlaneAK4["y_edges"]

rhoAK4 = Variable("Average emission density", is_independent=False, is_binned=False)
rhoAK4.values = lundPlaneAK4["z"]

tableAK4 = Table("Average primary Lund plane density for AK4 jets")
for var in [xAK4,yAK4,rhoAK4]:
	tableAK4.add_variable(var)
tableAK4.keywords["observables"] = ["rho(kT, DeltaR)"]
tableAK4.keywords["reactions"] = ["P P --> JETS"]
tableAK4.keywords["cmenergies"] = ["13000"]
submission.add_table(tableAK4)

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

covarianceAK4JERupValue = Variable("Covariance matrix for JER up variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4JERupValue.values = covarianceAK4JERup["z"]

tableCovMatrixAK4JERup = Table("Covariance matrix for JER up variation for AK4 jets")
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

covarianceAK4FSRupValue = Variable("Covariance matrix for FSR up variation for AK4 jets", is_independent=False, is_binned=False)
covarianceAK4FSRupValue.values = covarianceAK4FSRup["z"]

tableCovMatrixAK4FSRup = Table("Covariance matrix for FSR up variation for AK4 jets")
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


submission.create_files('./outputSMP22007/')
