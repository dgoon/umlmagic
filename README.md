# umlmagic

IPython notebook magic to draw UML diagram.

![Sample](http://raw.github.com/dgoon/umlmagic/master/static/umlmagic.png "Sample")

### Requirement

This extension uses [plantuml](http://plantuml.sourceforge.net/).
Plantuml is written in java and depends on [graphviz](http://www.graphviz.org/).
You can install graphviz with this command in ubuntu/debian:

    $ [sudo] apt-get install graphviz

### Install

    %install_ext https://raw.github.com/dgoon/umlmagic/master/umlmagic.py

### Cell magic

Try this:

    %%uml

    @startuml
    Alice -> Bob: Authentication Request
    Bob --> Alice: Authentication Response
    Alice -> Bob: Another authentication Request
    Alice <-- Bob: another authentication Response
    @enduml
