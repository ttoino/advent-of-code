{
  description = "Advent of Code 2024 Solutions";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      pkgs = import nixpkgs {
        system = "x86_64-linux";
        config.allowUnfree = true;
      };

      lib = import ./lib.nix { inherit pkgs; };
    in
    with lib;
    makeConfig {
      "2025" =
        with languages;
        (repeat 9 rust)
        ++ [
          (minizinc rust)
          rust
          rust
        ];
      "2024" = with languages; [
        apl
        bash
        c
        dart
        elixir
        fortran
        go
        haskell
        idris
        julia
        kotlin
        lua
        maxima
        nix
        ocaml
        prolog
        rust
        scala
        typescript
        ucm
        vala
        wyvern
        xtend
        yorick
        zig
      ];
      "2023" = repeat 25 languages.python;
      "2022" = repeat 25 languages.python;
      "2021" = repeat 25 languages.python;
      "2018" = repeat 25 languages.python;
      "2017" = repeat 25 languages.python;
      "2016" = repeat 25 languages.python;
      "2015" = repeat 25 languages.python;
    };
}
