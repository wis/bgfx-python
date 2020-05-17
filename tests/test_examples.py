from examples.cubes.cubes import Cubes
from examples.helloworld.helloworld import HelloWorld
from tests.osmesa_context import OSMesaContext


def test_helloworld_example():
    HelloWorld.__bases__ = (OSMesaContext,)
    test = HelloWorld(1280, 720, "Test")
    test.run()


def test_cubes_example():
    Cubes.__bases__ = (OSMesaContext,)
    test = Cubes(1280, 720, "Test")
    test.run()