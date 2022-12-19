libraries/Cabal/Cabal-syntax_PACKAGE = Cabal-syntax
libraries/Cabal/Cabal-syntax_dist-install_GROUP = libraries
$(if $(filter Cabal/Cabal-syntax,$(PACKAGES_STAGE0)),$(eval $(call build-package,libraries/Cabal/Cabal-syntax,dist-boot,0)))
$(if $(filter Cabal/Cabal-syntax,$(PACKAGES_STAGE1)),$(eval $(call build-package,libraries/Cabal/Cabal-syntax,dist-install,1)))
$(if $(filter Cabal/Cabal-syntax,$(PACKAGES_STAGE2)),$(eval $(call build-package,libraries/Cabal/Cabal-syntax,dist-install,2)))
