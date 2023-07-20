"""
Does unit/integration testing for buffer of PyTimeloop.
"""

# Imports some convenience libraries for easier unittest management.
import unittest
import typing
from pathlib import Path

# Imports the items we're testing; Engine is used to generate Buffers.
from bindings.model import Engine, Topology, BufferLevel

# Imports the test utility functions.
from tests.util import run_evaluation


class StatsTest(unittest.TestCase):
    """
    Tests that we are able to access BufferLevel::Stats in Python.
    """

    def test_accession(self) -> None:
        """Tests we are able to access all instance variables of BufferLevel.Stats.

        All test results will be printed out or logged through unittest assert.
        Nothing is returned.

        @param self The testing environment.
        """
        # Directory and path of all the config files.
        config_dir: Path = Path("01-model-conv1d-2level")
        paths: list[str] = [
            "arch/*.yaml",
            "map/conv1d-2level-os.map.yaml",
            "prob/*.yaml",
        ]

        # Engine that is used to generate the BufferLevel.
        engine: Engine = run_evaluation(config_dir, paths)
        # Topology containing the BufferLevel generated by Engine.
        topology: Topology = engine.get_topology()
        # BufferLevels constructed by Topology.
        buffer_levels: list[BufferLevel] = topology.buffer_levels

        # Goes through all levels and checks printout is working
        level: BufferLevel
        for level in buffer_levels:
            print(level)
            print("Stats:")
            # Gets the stats of the level.
            stats: BufferLevel.Stats = level.stats
            # Collects all instance variable names of stats.
            var_names: list[str] = {
                var_name
                for var_name in dir(stats)
                if not callable(getattr(stats, var_name))
            } - {"__doc__", "__module__"}
            # Tests we're able to access everything in Stats
            key: str
            for key in var_names:
                # Pulls the attribute from stats.
                attr: typing.Any = getattr(stats, key)

                ## TODO:: Replace this at some point with a ground truth reference.
                print(f"{key}: {attr}")
            print("Specs:")
            # Gets the specs of the level.
            specs: BufferLevel.Specs = level.specs
            # Collects all instance variable names of specs.
            var_names: list[str] = {
                var_name
                for var_name in dir(specs)
                if not callable(getattr(specs, var_name))
            } - {"__doc__", "__module__"}
            # Tests we're able to access everything in Specs
            key: str
            for key in var_names:
                # Pulls the attribute from specs.
                attr: typing.Any = getattr(specs, key)

                ## TODO:: Replace this at some point with a ground truth reference.
                print(f"{key}: {attr}")


if __name__ == "__main__":
    unittest.main()
