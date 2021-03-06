{-# LANGUAGE TypeFamilies, GeneralizedNewtypeDeriving #-}

module ShouldCompile where

data family S a

newtype instance S Int = S Int
		       deriving Eq

data family S2 a b

newtype instance S2 Int b = S2 (IO b)
		          deriving Monad

