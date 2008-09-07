import os
import re

# prepare version-/platform-specific ghci024.stdout
# - listen to ghci -package ghc, to figure out package ghc contents for :show packages
# - change flag defaults according to platform (unregistered -> -fno-asm-mangling)
# - prepare separate flag lists for 6.9 or earlier 
#   (please make sure to add your flags to the right section!)
#
def prepare024( opts ):
  h = os.popen('echo :q | '+config.compiler+' --interactive -package ghc ')
  packages = h.read()
  h.close()
  packagelist = []
  for l in packages.splitlines():
    if re.match('^Loading package',l): 
      packagelist += [re.sub(r'^Loading package (\S*) .*$',r'\1',l)]
  packagelist += ['rts']
  packagelist.sort()

  if config.unregisterised :
    mangling = 'no-'
  else:
    mangling = ''

  if version_lt(config.compiler_version, '6.9') :
    outtext = """\
-- ghci024.stdout is a generated file! please edit ghci024.py instead.
options currently set: none.
GHCi-specific dynamic flag settings:
  -fno-print-explicit-foralls
  -fprint-bind-result
  -fno-break-on-exception
  -fno-break-on-error
  -fno-print-evld-with-show
other dynamic, non-language, flag settings:
  -fno-warn-dodgy-imports
  -fwarn-duplicate-exports
  -fno-warn-hi-shadowing
  -fno-warn-implicit-prelude
  -fno-warn-incomplete-patterns
  -fno-warn-incomplete-record-updates
  -fwarn-missing-fields
  -fwarn-missing-methods
  -fno-warn-missing-signatures
  -fno-warn-name-shadowing
  -fwarn-overlapping-patterns
  -fno-warn-simple-patterns
  -fno-warn-type-defaults
  -fno-warn-monomorphism-restriction
  -fno-warn-unused-binds
  -fno-warn-unused-imports
  -fno-warn-unused-matches
  -fwarn-deprecations
  -fno-warn-orphans
  -fno-warn-tabs
  -fno-strictness
  -fno-full-laziness
  -fno-liberate-case
  -fno-spec-constr
  -fno-cse
  -fignore-interface-pragmas
  -fomit-interface-pragmas
  -fdo-lambda-eta-expansion
  -fno-ignore-asserts
  -fno-ignore-breakpoints
  -fno-do-eta-reduction
  -fno-case-merge
  -fno-unbox-strict-fields
  -fno-dicts-cheap
  -fno-excess-precision
  -f%(mangling)sasm-mangling
  -fno-force-recomp
  -fno-hpc-no-auto
  -fno-rewrite-rules
  -fprint-bind-contents
  -fno-vectorise
  -fno-regs-graph
  -fno-regs-iterative
  -fgen-manifest
  -fembed-manifest
  -fimplicit-import-qualified
active language flags:
  -XImplicitPrelude
  -XMonomorphismRestriction
  -XMonoPatBinds
-- :set -fglasgow-exts
active language flags:
  -XPatternGuards
  -XUnicodeSyntax
  -XMagicHash
  -XPolymorphicComponents
  -XExistentialQuantification
  -XKindSignatures
  -XPatternSignatures
  -XEmptyDataDecls
  -XParallelListComp
  -XForeignFunctionInterface
  -XUnliftedFFITypes
  -XLiberalTypeSynonyms
  -XRankNTypes
  -XTypeOperators
  -XRecursiveDo
  -XImplicitPrelude
  -XGADTs
  -XTypeFamilies
  -XMonomorphismRestriction
  -XMonoPatBinds
  -XRelaxedPolyRec
  -XImplicitParams
  -XScopedTypeVariables
  -XUnboxedTuples
  -XStandaloneDeriving
  -XDeriveDataTypeable
  -XTypeSynonymInstances
  -XFlexibleContexts
  -XFlexibleInstances
  -XConstrainedClassMethods
  -XMultiParamTypeClasses
  -XFunctionalDependencies
  -XGeneralizedNewtypeDeriving
active package flags: none
packages currently loaded:
  base
  rts
-- :set -package ghc
active package flags:
  -package ghc
packages currently loaded:
"""%{'mangling': mangling}

  else:
    outtext = """\
-- ghci024.stdout is a generated file! please edit ghci024.py instead.
options currently set: none.
GHCi-specific dynamic flag settings:
  -fno-print-explicit-foralls
  -fno-print-bind-result
  -fno-break-on-exception
  -fno-break-on-error
  -fno-print-evld-with-show
other dynamic, non-language, flag settings:
  -fwarn-dodgy-foreign-imports
  -fno-warn-dodgy-imports
  -fwarn-duplicate-exports
  -fno-warn-hi-shadowing
  -fno-warn-implicit-prelude
  -fno-warn-incomplete-patterns
  -fno-warn-incomplete-record-updates
  -fwarn-missing-fields
  -fwarn-missing-methods
  -fno-warn-missing-signatures
  -fno-warn-name-shadowing
  -fwarn-overlapping-patterns
  -fno-warn-simple-patterns
  -fno-warn-type-defaults
  -fno-warn-monomorphism-restriction
  -fno-warn-unused-binds
  -fno-warn-unused-imports
  -fno-warn-unused-matches
  -fwarn-warnings-deprecations
  -fwarn-deprecations
  -fwarn-deprecated-flags
  -fno-warn-orphans
  -fno-warn-tabs
  -fwarn-unrecognised-pragmas
  -fno-strictness
  -fno-static-argument-transformation
  -fno-full-laziness
  -fno-liberate-case
  -fno-spec-constr
  -fno-cse
  -fignore-interface-pragmas
  -fomit-interface-pragmas
  -fdo-lambda-eta-expansion
  -fno-ignore-asserts
  -fno-do-eta-reduction
  -fno-case-merge
  -fno-unbox-strict-fields
  -fmethod-sharing
  -fno-dicts-cheap
  -fno-excess-precision
  -f%(mangling)sasm-mangling
  -fno-force-recomp
  -fno-hpc-no-auto
  -fno-rewrite-rules
  -fprint-bind-contents
  -fno-run-cps
  -fno-convert-to-zipper-and-back
  -fno-vectorise
  -fno-regs-graph
  -fno-regs-iterative
  -fgen-manifest
  -fembed-manifest
  -fimplicit-import-qualified
active language flags:
  -XImplicitPrelude
  -XMonomorphismRestriction
  -XMonoPatBinds
-- :set -fglasgow-exts
active language flags:
  -XPostfixOperators
  -XPatternGuards
  -XUnicodeSyntax
  -XMagicHash
  -XPolymorphicComponents
  -XExistentialQuantification
  -XKindSignatures
  -XPatternSignatures
  -XEmptyDataDecls
  -XParallelListComp
  -XForeignFunctionInterface
  -XUnliftedFFITypes
  -XLiberalTypeSynonyms
  -XRankNTypes
  -XImpredicativeTypes
  -XTypeOperators
  -XRecursiveDo
  -XImplicitPrelude
  -XGADTs
  -XTypeFamilies
  -XMonomorphismRestriction
  -XMonoPatBinds
  -XRelaxedPolyRec
  -XImplicitParams
  -XScopedTypeVariables
  -XUnboxedTuples
  -XStandaloneDeriving
  -XDeriveDataTypeable
  -XTypeSynonymInstances
  -XFlexibleContexts
  -XFlexibleInstances
  -XConstrainedClassMethods
  -XMultiParamTypeClasses
  -XFunctionalDependencies
  -XGeneralizedNewtypeDeriving
active package flags: none
packages currently loaded:
  base
  ghc-prim
  integer
  rts
-- :set -package ghc
active package flags:
  -package ghc
packages currently loaded:
"""%{'mangling': mangling}

  outfile = open(in_testdir('ghci024.stdout'), 'w')
  outfile.write(outtext)
  for l in packagelist: outfile.write('  '+l+'\n')
  outfile.close()

  return;

