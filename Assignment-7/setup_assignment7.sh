#!/bin/bash

echo "🔧 Setting up Python virtual environment for AIS Damage Classifier..."

# Step 1: Create virtual environment
python3 -m venv venv
echo "✅ Virtual environment 'venv' created."

# Step 2: Activate environment
source venv/bin/activate
echo "✅ Activated virtual environment."

# Step 3: Upgrade pip
pip install --upgrade pip

# Step 4: Install essential dependencies
echo "📦 Installing required Python packages..."
pip install numpy pandas matplotlib seaborn scikit-learn ipykernel notebook

# Step 5: Register kernel with Jupyter
python -m ipykernel install --user --name=venv --display-name "Python (Assignment7 Env)"
echo "✅ Jupyter kernel 'Python (Assignment7 Env)' registered."

echo "🎉 Setup Complete! Now open your Jupyter Notebook and select the 'Python (Assignment7 Env)' kernel."
