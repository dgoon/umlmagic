"""
Plantuml IPython magic extensions

Magic methods:
    %%uml
    @startuml
      blah blah ...
    @enduml

Usage:
    %load_ext umlmagic

Install:
    %install_ext https://raw.github.com/dgoon/umlmagic/master/umlmagic.py

Copied from gvmagic.py(https://github.com/cjdrake/ipython-magic/blob/master/gvmagic.py).
Thanks for good reference ;-)
"""

import os, shlex, urllib2
from subprocess import Popen, PIPE

from IPython.core.display import display_svg
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.utils.warn import info, error

def curpath():
    return os.path.split(os.path.realpath(__file__))[0]

def ensure_plantuml_jar():
    target_path = '%s/plantuml.jar' % (curpath())
    if not os.path.isfile(target_path):
        f = urllib2.urlopen("http://sourceforge.net/projects/plantuml/files/plantuml.jar/download")
        with open(target_path, 'wb') as fout:
            fout.write(f.read())

def runplantuml(s):
    """Execute plantuml and return a raw SVG image, or None."""
    cmd = 'java -jar %s/plantuml.jar -Tsvg -p' % curpath()
    plantuml = Popen(shlex.split(cmd), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdoutdata, stderrdata = plantuml.communicate(s.encode('utf-8'))

    status = plantuml.wait()
    if status == 0:
        return stdoutdata
    else:
        fstr = "plantuml returned {}\n[==== stderr ====]\n{}"
        error(fstr.format(status, stderrdata.decode('utf-8')))
        return None

@magics_class
class UMLMagics(Magics):
    @cell_magic
    def uml(self, line, cell):
        """plantuml cell magic
        Ignores arguments. """

        data = runplantuml(cell)
        if data:
            display_svg(data, raw=True)

def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    ensure_plantuml_jar()
    ipython.register_magics(UMLMagics)

def unload_ipython_extension(ipython):
    """Unload the extension in IPython."""
