{-# LANGUAGE DataKinds #-}
module DataKind3 where

-- Fails because of no -XPolyKinds
data kind Foo a = Bar
