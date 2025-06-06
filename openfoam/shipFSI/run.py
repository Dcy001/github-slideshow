#!/usr/bin/env python3
"""Run a basic ship FSI case using OpenFOAM."""
import os
import shutil
import subprocess
from pathlib import Path
import sys


def run(cmd):
    print("Running:", cmd)
    subprocess.check_call(cmd, shell=True)


def main():
    foam_tutorials = os.environ.get("FOAM_TUTORIALS")
    if not foam_tutorials:
        sys.exit("Please source OpenFOAM before running this script.")

    script_dir = Path(__file__).resolve().parent
    case_dir = script_dir / "shipFSICase"

    if case_dir.exists():
        shutil.rmtree(case_dir)
    shutil.copytree(Path(foam_tutorials) / "multiphase/interDyMFoam/ras/floatingObject", case_dir)

    dynamic_mesh_dict = case_dir / "constant/dynamicMeshDict"
    dynamic_mesh_dict.write_text(
        """dynamicFvMesh dynamicMotionSolverFvMesh;\n"
        "motionSolverLibs (\"libfvMotionSolvers.so\");\n\n"
        "solver sixDoFRigidBodyMotionSolver;\n\n"
        "sixDoFRigidBodyMotionCoeffs\n"
        "{\n"
        "    patches (hull);\n"
        "    centerOfMass (0 0 0);\n"
        "    rhoSolid 900;\n"
        "    rhoFluid 1000;\n"
        "    report on;\n"
        "}\n"
    )

    os.chdir(case_dir)
    run("blockMesh")
    run("setFields")
    run("interDyMFoam")


if __name__ == "__main__":
    main()
