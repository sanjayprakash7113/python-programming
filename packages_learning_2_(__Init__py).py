#A package = folder with Python files.
#But Python will treat a folder as a “package” ONLY if it contains __init__.py.


#To mark folder as a package
import mypkg.calc

#To control what gets imported
from .calc import add
from .utils import multiply

from mypkg import add, multiply
from mathpack import add, square

print(add(2,3))
print(square(5))
