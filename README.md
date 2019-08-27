# BayesianModel
This Repository contains three files:

1- A code.py file :
Is written with a python wrapper of a C++ library called " Structural Modeling, Inference and Learning Engine(SMILE) it contains two classes.The fist one is "CreatingBN" for the creation of a Bayesian network that models the causal relationships between metacognitive skills and their influence on the level of self-regulation. The second class is "InferenceCalls" for the modification of the values of each evidence and the  beliefs update (Bayesian inference). It is necessary to import a "pysmile" package from the site https://www.bayesfusion.com/

2- A Network.xdsl file :
Is an xdsl (xml) format file that was built by the CreatingBN class. To view the network, u need just to download the application GeNIe Modeler,GUI for SMILE.

3- A Skills'scores.csv file contains the discretized composite scores for each skill.

