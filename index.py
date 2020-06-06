import argparse
import repositoriesdownload
import delay
import githubmetadata
import numberofextensionfile
import currentframeworkversion
import forksahead
import importcount
import maintainers
import file_extension_changes
import understandmetrics
import file_extension_changes_forks
import metricsbycommits
import stackoverflow
import generalprojects


def main(args):
    if args.download or args.all:
        repositoriesdownload.repositoriesdownload(args.framework, args.projects)
    if args.delay or args.all:
        delay.delay(args.framework, args.projects, args.githubtoken)
    if args.githubmetadata or args.all:
        githubmetadata.githubmetadata(args.framework, args.projects, args.githubtoken)
    if args.numberofextensionfile or args.all:
        numberofextensionfile.numberofextensionfile(args.framework, args.projects)
    if args.currentframeworkversion or args.all:
        currentframeworkversion.currentframeworkversion(args.framework, args.projects)
    if args.forksahead or args.all:
        forksahead.forksahead(args.framework, args.projects, args.githubtoken)
    if args.importcount or args.all:
        importcount.importcount(args.framework, args.projects)
    if args.maintainers or args.all:
        maintainers.maintainers(args.framework, args.projects, args.githubtoken)
    if args.file_extension_changes or args.all:
        file_extension_changes.file_extension_changes(args.framework, args.projects)
    if args.file_extension_changes_forks or args.all:
        file_extension_changes_forks.file_extension_changes_forks(args.framework, args.projects, args.githubtoken)
    if args.understandmetrics or args.all:
        understandmetrics.understandmetrics(args.framework, args.projects)
    if args.metricsbycommit or args.all:
        metricsbycommits.metrics_by_commits(args.framework, args.projects)
    if args.stackoverflow:
        stackoverflow.stackoverflow(args.framework, args.projects)
    if args.generalprojects:
        generalprojects.generalprojects(args.projects)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-framework", "-f", type=str, required=True, help="framework")
    parser.add_argument("-projects", "-p", type=str, required=True, help="File's path that's contains the list of projects to analyze")
    parser.add_argument("-all", action="store_true", required=False, help="Do you want to get all?")
    parser.add_argument("-githubtoken", "-t", type=str, required=True, help="https://github.com/settings/tokens")
    parser.add_argument("-download", "-d", action="store_true", required=False, help="Do you want to download the repositories?")
    parser.add_argument("-delay", "-e", action="store_true", required=False, help="Do you want to computed the delay?")
    parser.add_argument("-githubmetadata", "-g", action="store_true", required=False, help="Do you want to computed github metadata?")
    parser.add_argument("-numberofextensionfile", "-x", action="store_true", required=False, help="Do you want to computed the number of files by extensions?")
    parser.add_argument("-currentframeworkversion", "-v", action="store_true", required=False, help="Do you want to get the current version of framework?")
    parser.add_argument("-forksahead", "-k", action="store_true", required=False, help="Do you want to get the number of forks and forks ahead?")
    parser.add_argument("-importcount", "-i", action="store_true", required=False, help="Do you want to get the number imports of the framework into sample?")
    parser.add_argument("-maintainers", "-m", action="store_true", required=False, help="Do you want to get maintainers stats?")
    parser.add_argument("-file_extension_changes", "-o", action="store_true", required=False, help="Do you want to get metrics over the time?")
    parser.add_argument("-file_extension_changes_forks", action="store_true", required=False, help="Do you want to get metrics of forks over the time?")
    parser.add_argument("-understandmetrics", "-u", action="store_true", required=False, help="Do you want to get metrics from Understand SciTool?")
    parser.add_argument("-metricsbycommit", action="store_true", required=False, help="Do you want to get metrics by commits?")
    parser.add_argument("-stackoverflow", action="store_true", required=False, help="Do you want to get metrics of stackoverflow?")
    parser.add_argument("-generalprojects", action="store_true", required=False, help="General Projects")
    args = parser.parse_args()

    main(args)
