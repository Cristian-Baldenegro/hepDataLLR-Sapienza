from hepdata_lib import Submission
submission = Submission()
submission.read_abstract("example_inputs/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/SMP-22-007/")
submission.add_record_id(1234567, "inspire")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:AB.CDEFG")
submission.add_additional_resource("XML file to map bin indices to physical binning for AK8 jets", "testUnfold5binning.xml", copy_file=True)

from hepdata_lib import RootFileReader
reader = RootFileReader("lundDataAK8_hepData.root")
lundPlaneAK8 = reader.read_hist_2d("lundplaneUnfoldedAK8")

from hepdata_lib import Submission, Variable, Table
from hepdata_lib import Uncertainty

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

lundPlaneAK8_1D = reader.read_hist_1d("recoall1D")


x1D = Variable("Bin index", is_independent=True, is_binned=False)
x1D.values = lundPlaneAK8_1D["x"]
rho1D = Variable("Average density for AK8 jets", is_independent=False, is_binned=False)
rho1D.values = lundPlaneAK8_1D["y"]
readerUncertaintiesAK8 = RootFileReader("1Duncertainties_ak8.root")
priorUncertaintyAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixPrior_histogram")
priorSymmetrizedUncertaintyAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixPriorSymmetrized_histogram")
priorAK8 = Uncertainty("priorBias", is_symmetric=False)
priorBiasSymmetrized = list(zip(priorUncertaintyAK8_1D["y"], priorSymmetrizedUncertaintyAK8_1D["y"]))
priorAK8.values = priorBiasSymmetrized#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(priorAK8)


responseUncertaintyAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixResponse_histogram")
responseSymmetrizedUncertaintyAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixResponseSymmetrized_histogram")
responseAK8 = Uncertainty("detectorResponse", is_symmetric=False)
responseBiasSymmetrized = list(zip(responseUncertaintyAK8_1D["y"], responseSymmetrizedUncertaintyAK8_1D["y"]))
responseAK8.values = responseBiasSymmetrized#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(responseAK8)

trackIneff2016UncertaintyAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixTrackIneff2016_histogram")
trackIneff2016SymmetrizedUncertaintyAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixTrackIneff2016Symmetrized_histogram")
trackIneff2016AK8 = Uncertainty("trackIneff2016", is_symmetric=False)
trackIneff2016Symmetrized = list(zip(trackIneff2016UncertaintyAK8_1D["y"], trackIneff2016SymmetrizedUncertaintyAK8_1D["y"]))
trackIneff2016AK8.values = trackIneff2016Symmetrized#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(trackIneff2016AK8)

trackIneff20178UncertaintyAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixTrackIneff20178_histogram")
trackIneff20178SymmetrizedUncertaintyAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixTrackIneff20178Symmetrized_histogram")
trackIneff20178AK8 = Uncertainty("trackIneff20178", is_symmetric=False)
trackIneff20178Symmetrized = list(zip(trackIneff20178UncertaintyAK8_1D["y"], trackIneff20178SymmetrizedUncertaintyAK8_1D["y"]))
trackIneff20178AK8.values = trackIneff20178Symmetrized#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(trackIneff20178AK8)

JERupAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixJERup_histogram")
JERdownAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixJERdown_histogram")
JER_AK8 = Uncertainty("JER", is_symmetric=False)
JERupAndDown = list(zip(JERupAK8_1D["y"], JERdownAK8_1D["y"]))
JER_AK8.values = JERupAndDown#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(JER_AK8)

JECupAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixJECup_histogram")
JECdownAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixJECdown_histogram")
JEC_AK8 = Uncertainty("JEC", is_symmetric=False)
JECupAndDown = list(zip(JECupAK8_1D["y"], JECdownAK8_1D["y"]))
JEC_AK8.values = JECupAndDown#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(JEC_AK8)

PUupAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixPUup_histogram")
PUdownAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixPUdown_histogram")
PU_AK8 = Uncertainty("pileup", is_symmetric=False)
PUupAndDown = list(zip(PUupAK8_1D["y"], PUdownAK8_1D["y"]))
PU_AK8.values = PUupAndDown#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(PU_AK8)



FSRupAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixFSRup_histogram")
FSRdownAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixFSRdown_histogram")
FSR_AK8 = Uncertainty("FSR", is_symmetric=False)
FSRupAndDown = list(zip(FSRupAK8_1D["y"], FSRdownAK8_1D["y"]))
FSR_AK8.values = FSRupAndDown#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(FSR_AK8)

ISRupAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixISRup_histogram")
ISRdownAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixISRdown_histogram")
ISR_AK8 = Uncertainty("ISR", is_symmetric=False)
ISRupAndDown = list(zip(ISRupAK8_1D["y"], ISRdownAK8_1D["y"]))
ISR_AK8.values = ISRupAndDown#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(ISR_AK8)


FSRupISRupAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixFSRupISRup_histogram")
FSRdownISRdownAK8_1D = readerUncertaintiesAK8.read_hist_1d("covarianceMatrixFSRdownISRdown_histogram")
FSRISR_AK8 = Uncertainty("FSRandISR", is_symmetric=False)
FSRISRupAndDown = list(zip(FSRupISRupAK8_1D["y"], FSRdownISRdownAK8_1D["y"]))
FSRISR_AK8.values = FSRISRupAndDown#priorUncertaintyAK8_1D["y"]
rho1D.add_uncertainty(FSRISR_AK8)

readerAK8StatUncertainties = RootFileReader("correlationMatrices_ak8.root")

StatsAK8_1D = readerAK8StatUncertainties.read_hist_1d("stats1D_histogram")
Stats_AK8 = Uncertainty("Stats", is_symmetric=True)
Stats_AK8.values = StatsAK8_1D["y"]
rho1D.add_uncertainty(Stats_AK8)

responseStatsAK8_1D = readerAK8StatUncertainties.read_hist_1d("responseStats1D_histogram")
responseStats_AK8 = Uncertainty("MCstats", is_symmetric=True)
responseStats_AK8.values = responseStatsAK8_1D["y"]
rho1D.add_uncertainty(responseStats_AK8)

table1D = Table("AK8 primary Lund plane density mapped to 1D")
for var in [x1D,rho1D]:
        table1D.add_variable(var)
table1D.description = "Primary Lund jet plane density for AK8 jets in a one-dimensional representation with bin indices for MC tuning purposes. The mapping between the bin indices and the physical binning can be imported from the XML file attached to this HepData record using the TUnfoldBinningXML class of ROOT (qualitatively, it corresponds to slicing the Lund plane horizontally from low kT to high kT). All systematic uncertainties are bin-to-bin fully correlated (allowing for sign-changes bin-to-bin), with the exception of the statistical uncertainties from data and MC, for which a separate correlation matrix is provided in this HepData record."
table1D.location = "Corresponds to Figure 8 (lower panel) and the Lund plane slices of Figures 10--16 in the paper."
table1D.keywords["observables"] = ["rho(kT, DeltaR)"]
table1D.keywords["reactions"] = ["P P --> JETS"]
table1D.keywords["cmenergies"] = ["13000"]


submission.add_table(table1D)


#covariance matrix, statistical uncertainties


covarianceMatrixStatsAK8 = readerAK8StatUncertainties.read_hist_2d("correlationMatrix_histogram")

# Create variable objects
xCovStatsAK8 = Variable("Bin index", is_independent=True, is_binned=True)
xCovStatsAK8.values = covarianceMatrixStatsAK8["x_edges"]

yCovStatsAK8 = Variable("Bin index", is_independent=True, is_binned=True)
yCovStatsAK8.values = covarianceMatrixStatsAK8["y_edges"]

covMatrixStatsValue = Variable("Correlation coefficient", is_independent=False, is_binned=False)
covMatrixStatsValue.values = covarianceMatrixStatsAK8["z"]

tableCovMatrixStatsAK8 = Table("Correlation matrix for data and MC stats for AK8 jets")
for var in [xCovStatsAK8,yCovStatsAK8, covMatrixStatsValue]:
        tableCovMatrixStatsAK8.add_variable(var)
#tableCovMatrixStatsAK8.location = "Associated to the"
table1D.description = "Primary Lund jet plane density for AK8 jets in a one-dimensional representation with bin indices. The mapping between the bin indices and the physical binning can be imported from the XML file attached to this HepData record using the TUnfoldBinningXML class of ROOT (qualitatively, it corresponds to slicing the Lund plane horizontally from low kT to high kT)."
submission.add_table(tableCovMatrixStatsAK8)

submission.create_files('./outputSMP22007/')
