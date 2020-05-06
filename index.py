import argparse
import repositoriesdownload
import delay
import githubmetadata
import numberofextensionfile
import currentframeworkversion
import forksahead


def main(args):
    if args.download:
        repositoriesdownload.repositoriesdownload(args.framework, args.projects)
    if args.delay:
        delay.delay(args.framework, args.projects, args.githubtoken)
    if args.githubmetadata:
        githubmetadata.githubmetadata(args.framework, args.projects, args.githubtoken)
    if args.numberofextensionfile:
        numberofextensionfile.numberofextensionfile(args.framework, args.projects)
    if args.currentframeworkversion:
        currentframeworkversion.currentframeworkversion(args.framework, args.projects)
    if args.forksahead:
        forksahead.forksahead(args.framework, args.projects, args.githubtoken)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-framework", "-f", type=str, required=True, help="framework")
    parser.add_argument("-projects", "-p", type=str, required=True,
                        help="File's path that's contains the list of projects to analyze")
    parser.add_argument("-githubtoken", "-t", type=str, required=True, help="https://github.com/settings/tokens")
    parser.add_argument("-download", "-d", action="store_true", required=False,
                        help="Do you want to download the repositories?")
    parser.add_argument("-delay", "-e", action="store_true", required=False,
                        help="Do you want to computed the delay?")
    parser.add_argument("-githubmetadata", "-g", action="store_true", required=False,
                        help="Do you want to computed github metadata?")
    parser.add_argument("-numberofextensionfile", "-x", action="store_true", required=False,
                        help="Do you want to computed the number of files by extensions?")
    parser.add_argument("-currentframeworkversion", "-v", action="store_true", required=False,
                        help="Do you want to get the current version of framework?")
    parser.add_argument("-forksahead", "-k", action="store_true", required=False,
                        help="Do you want to get the number of forks and forks ahead?")
    args = parser.parse_args()

    main(args)
