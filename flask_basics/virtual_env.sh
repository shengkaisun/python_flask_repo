# Create an env with a specific package included
conda create -n myenv numpy

# Create an env with a specific version of Python
conda create --name myenv python=3.8

# Specify a verison of a package
conda create -n myenv numpy=1.4

# List out all your envs
conda env list

# Create Flask environment
conda create -n myflaskenv flask

# Enter an env
conda activate myflaskenv

# Exit an env
conda deactivate