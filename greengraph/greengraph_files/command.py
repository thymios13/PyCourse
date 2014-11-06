from argparse import ArgumentParser
from greengraph_main import myGreengraph

def process():
    parser = ArgumentParser(description = "Generate the Graphpath of green between 2 locations(cities)")

    parser.add_argument('location_1')
    parser.add_argument('location_2')

    arguments= parser.parse_args()

    myGreengraph(arguments.location_1, arguments.location_2)

    if __name__ == "__main__":
        process()
