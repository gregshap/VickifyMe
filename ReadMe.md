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
curl -u gregshap -i https://api.github.com/repos/gregshap/vickifyme/commits?author=gregshap > GregsCommits.txt
```

Save the whole hunk of json into a text file next to the script, and when you run VickifyMe you'll get a new file with text ready to copy into MediaWiki.


## Notes

This is pretty dependent on having some standard conventions for writing commit notes, but that's a good idea anyway. 
It shouldn't be hard to edit for other checkin comment styles.

The current workflow to grab changeset data using devtools is a bit of pain. 
Some work to automate that process will make the tool much easier to adopt.
