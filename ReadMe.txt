<h1> Example </h1>

<pre>
    <code> python VickifyMe.py AllTheChangesets.txt </code>
</pre>

<p>
In the example above, "AllTheChangesets.txt" should contain a json collection of changeset data from TFS 2012.
</p>

<h2> To Get the JSON Data</h2>
<p>
Grab the json data by going to your TFS collection web portal, clicking 'SOURCE' and then "Find..." to get to the changeset picker.
</p>

<p>
Filter to the desired changesets, then use firebug, chrome tools, or your weapon of choice to grab the json response when you hit the find button.
</p>

<p>
Save the whole hunk of json into a text file next to the script, and when you run VickifyMe you'll get a new file with text ready to copy into MediaWiki.
</p>


<h1> Disclaimers </h1>
<p>
This is really meant to work with Team Olive's checkin comment styles, and custom MediaWiki templates that we've installed on the Vicki. Mileage may vary with your own changeset comments and wiki behavior.
</p>

<h1> What's Next </h1>
Copying data out of dev tools is a pain, so I plan to make this more seemless by hitting TFS's RESTful api directly from the script. Python's Request library, and various TFS Api wrappers look promising.