# Ship FSI Example

This example demonstrates a simple setup for running a multiphysics simulation of a ship in OpenFOAM. The simulation couples the free-surface flow around a hull with the six degree of freedom (6DoF) rigid-body motion model. A small Python script is provided to automate case setup and execution.

## Usage

1. Ensure OpenFOAM is installed and sourced, e.g.:
   ```bash
   source /opt/openfoam9/etc/bashrc
   ```
2. Run the provided Python script to create and execute the case:
   ```bash
   ./run.py
   ```

The script copies the standard `floatingObject` tutorial from the OpenFOAM distribution and modifies it with a simplified `dynamicMeshDict` suitable for a ship hull.
