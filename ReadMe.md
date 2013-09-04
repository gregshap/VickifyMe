# Convert VAN Changesets into Mediawiki

Parse commit comments into mediawiki with formatted links to PBIs, bug tickets, changeset diffs

## Installation

Install [python](http://python.org/) 2.7 and run:

```sh
    python VickifyMe.py AllTheChangesets.txt
```

Where "AllTheChangesets.txt" should contain a json collection of changeset data from TFS 2012.

## Pulling down the changeset data

Grab the json data by going to your TFS collection web portal, clicking 'SOURCE' and then "Find..." to get to the changeset picker.


Filter to the desired changesets, then use firebug, chrome tools, or your weapon of choice to grab the json response when you hit the find button.


Save the whole hunk of json into a text file next to the script, and when you run VickifyMe you'll get a new file with text ready to copy into MediaWiki.


## Notes

This is pretty dependent on having some standard conventions for writing commit notes, but that's a good idea anyway. 
It shouldn't be hard to edit for other checkin comment styles.

The current workflow to grab changeset data using devtools is a bit of pain. 
Some work to automate that process will make the tool much easier to adopt.
