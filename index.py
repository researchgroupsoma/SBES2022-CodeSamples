import argparse
import repositoriesdownload
import delay
import githubmetadata

def main(args):
    if args.download:
        repositoriesdownload.repositoriesdownload(args.framework, args.projects)
    if args.delay:
        delay.delay(args.framework, args.projects)
    if args.githubmetadata:
        githubmetadata.githubmetadata(args.framework, args.projects)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-framework", "-f", type=str, required=True, help="framework")
    parser.add_argument("-download", "-d", action="store_true", required=False,
                        help="Do you want to download the repositories?")
    parser.add_argument("-projects", "-p", type=str, required=True,
                        help="File's path that's contains the list of projects to analyze")
    parser.add_argument("-delay", "-e", action="store_true", required=False,
                        help="Do you want to computed the delay?")
    parser.add_argument("-githubmetadata", "-g", action="store_true", required=False,
                        help="Do you want to computed github metadata?")
    args = parser.parse_args()

    main(args)
