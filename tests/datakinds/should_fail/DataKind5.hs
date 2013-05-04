{-# LANGUAGE DataKinds #-}

module DataKind5 where

-- Int is not promotable
data kind Foo = Bar Int
