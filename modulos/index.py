import argparse
import repositoriesdownload


def main(args):
    repositoriesdownload.repositoriesdownload(args.framework, args.projects)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-framework", "-f", type=str, required=True, help="framework")
    parser.add_argument("-download", "-d", action="store_true", required=False,
                        help="Do you want to download the repositories?")
    parser.add_argument("-projects", "-p", type=str, required=True,
                        help="File's path that's contains the list of projects to analyze")

    args = parser.parse_args()

    main(args)
