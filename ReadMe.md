# Format github changesets into Mediawiki markup

Parse commit comments into mediawiki with formatted links to JIRA items, bug tickets, changeset diffs

Mostly useful for NGPVAN/VAN commit message style and associated mediawiki templates

## Installation

Install [python](http://python.org/) 2.7 and run:

```sh
    python VickifyMe.py AllTheChangesets.txt
```

Where "AllTheChangesets.txt" contains the json part of the response from https://api.github.com/repos/:owner/:repo/commits/

## Pulling down the changeset data

Grab the changesets you want from the github API http://developer.github.com/v3/git/commits/

If you are looking at a private repo, you can do this with a curl request like:
```sh
curl -u gregshap https://api.github.com/repos/gregshap/vickifyme/commits?author=gregshap > GregsCommits.txt
```

Run VickifyMe in the directoy of the json file, and you'll get a new file with text ready to copy into MediaWiki.

