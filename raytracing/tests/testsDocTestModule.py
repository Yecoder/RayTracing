import envtest
import doctest
import raytracing

## if a new python file is added to the module, please add it in a new line

doctest.testmod(m=raytracing.axicon,verbose=False)
doctest.testmod(m=raytracing.components,verbose=False)
doctest.testmod(m=raytracing.eo,verbose=False)
doctest.testmod(m=raytracing.figure,verbose=False)
doctest.testmod(m=raytracing.gaussianbeam,verbose=False)
doctest.testmod(m=raytracing.imagingpath,verbose=False)
doctest.testmod(m=raytracing.lasercavity,verbose=False)
doctest.testmod(m=raytracing.laserpath,verbose=False)
doctest.testmod(m=raytracing.materials,verbose=False)
doctest.testmod(m=raytracing.matrix,verbose=False)
doctest.testmod(m=raytracing.matrixgroup,verbose=False)
doctest.testmod(m=raytracing.ray,verbose=False)
doctest.testmod(m=raytracing.rays,verbose=False)
doctest.testmod(m=raytracing.specialtylenses,verbose=False)
doctest.testmod(m=raytracing.utils,verbose=False)



