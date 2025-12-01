{
  description = "Advent of Code 2024 Solutions";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };

      getInput = pkgs.writeShellApplication {
        name = "getInput";
        runtimeInputs = [ pkgs.curl ];
        text = builtins.readFile ./get-input.sh;
      };
    in
    {
      packages.${system}."2024" = {
        day01 = pkgs.writeShellApplication {
          name = "day01";
          runtimeInputs = [
            getInput
            (pkgs.dyalog.override { acceptLicense = true; })
          ];
          text = "getInput 2024 1 | dyalog -script ${./2024/day01.apl} 2> /dev/null";
        };
        day02 = pkgs.writeShellApplication {
          name = "day02";
          runtimeInputs = [
            getInput
            pkgs.bash
          ];
          text = "getInput 2024 2 | bash ${./2024/day02.bash}";
        };
        day03 = pkgs.writeShellApplication {
          name = "day03";
          runtimeInputs = [
            getInput
            (pkgs.writeCBin "day03Bin" (builtins.readFile ./2024/day03.c))
          ];
          text = "getInput 2024 3 | day03Bin";
        };
        day04 = pkgs.writeShellApplication {
          name = "day04";
          runtimeInputs = [
            getInput
            pkgs.dart
          ];
          text = "getInput 2024 4 | dart run ${./2024/day04.dart}";
        };
        day05 = pkgs.writeShellApplication {
          name = "day05";
          runtimeInputs = [
            getInput
            pkgs.elixir
          ];
          text = "getInput 2024 5 | elixir ${./2024/day05.exs}";
        };
        day06 = pkgs.writeShellApplication {
          name = "day06";
          runtimeInputs = [
            (pkgs.runCommand "day06Bin"
              {
                nativeBuildInputs = [ pkgs.gfortran ];
              }
              ''
                n="$out/bin/day06Bin"
                mkdir -p $(dirname $n)
                gfortran -fimplicit-none -fcheck=all -ffree-line-length-512 ${./2024/day06.f90} -o "$n"
              ''
            )
            getInput
          ];
          text = "getInput 2024 6 | day06Bin";
        };
        day07 = pkgs.writeShellApplication {
          name = "day07";
          runtimeInputs = [
            getInput
            pkgs.go
          ];
          text = "getInput 2024 7 | go run ${./2024/day07.go}";
        };
        day08 = pkgs.writeShellApplication {
          name = "day08";
          runtimeInputs = [
            pkgs.ghc
            getInput
          ];
          text = "getInput 2024 8 | runghc ${./2024/day08.hs}";
        };
        day09 = pkgs.writeShellApplication {
          name = "day09";
          runtimeInputs = [
            pkgs.idris2
            getInput
          ];
          text = "getInput 2024 9 | idris2 -x elba --source-dir / ${./2024/day09.idr}";
        };
        day10 = pkgs.writeShellApplication {
          name = "day10";
          runtimeInputs = [
            pkgs.julia
            getInput
          ];
          text = "getInput 2024 10 | julia ${./2024/day10.jl}";
        };
        day11 = pkgs.writeShellApplication {
          name = "day11";
          runtimeInputs = [
            pkgs.kotlin
            getInput
          ];
          text = "getInput 2024 11 | kotlinc -script ${./2024/day11.kts}";
        };
        day12 = pkgs.writeShellApplication {
          name = "day12";
          runtimeInputs = [
            pkgs.lua
            getInput
          ];
          text = "getInput 2024 12 | lua ${./2024/day12.lua}";
        };
        day13 = pkgs.writeShellApplication {
          name = "day13";
          runtimeInputs = [
            pkgs.maxima
            getInput
          ];
          text = "getInput 2024 13 | maxima --very-quiet --init-mac=${./2024/day13.mac} --batch-string='main()$'";
        };
        day14 = pkgs.writeShellApplication {
          name = "day14";
          runtimeInputs = [ getInput ];
          text = "nix eval --show-trace --raw --file ${./2024/day14.nix} --apply \"f: f ''$(getInput 2024 14)''\"";
        };
        day15 = pkgs.writeShellApplication {
          name = "day15";
          runtimeInputs = [
            pkgs.ocaml
            getInput
          ];
          text = "getInput 2024 15 | ocaml ${./2024/day15.ml}";
        };
        day16 = pkgs.writeShellApplication {
          name = "day16";
          runtimeInputs = [
            pkgs.swi-prolog
            getInput
          ];
          text = "getInput 2024 16 | swipl -g main ${./2024/day16.pl}";
        };
        day17 = pkgs.writeShellApplication {
          name = "day17";
          runtimeInputs = [
            (pkgs.runCommandCC "day17Bin"
              {
                nativeBuildInputs = [ pkgs.rustc ];
              }
              ''
                n="$out/bin/day17Bin"
                mkdir -p $(dirname $n)
                rustc ${./2024/day17.rs} -o "$n"
              ''
            )
            getInput
          ];
          text = "getInput 2024 17 | day17Bin";
        };
        day18 = pkgs.writeShellApplication {
          name = "day18";
          runtimeInputs = [
            pkgs.scala-cli
            getInput
          ];
          text = ''
            getInput 2024 18 | scala-cli run ${./2024/day18.scala}
          '';
        };
        day19 = pkgs.writeShellApplication {
          name = "day19";
          runtimeInputs = [
            pkgs.deno
            getInput
          ];
          text = "getInput 2024 19 | deno run ${./2024/day19.ts}";
        };
        day20 = pkgs.writeShellApplication {
          name = "day20";
          runtimeInputs = [
            pkgs.unison-ucm
            getInput
          ];
          text = "getInput 2024 20 | ucm run.file ${./2024/day20.u} main";
        };
        day21 = pkgs.writeShellApplication {
          name = "day21";
          runtimeInputs = [
            pkgs.vala
            getInput
          ];
          text = "getInput 2024 21 | vala ${./2024/day21.vala}";
        };
        day22 = pkgs.writeShellApplication {
          name = "day22";
          runtimeInputs = [ getInput ];
          text = "";
        };
        day23 = pkgs.writeShellApplication {
          name = "day23";
          runtimeInputs = [ getInput ];
          text = "";
        };
        day24 = pkgs.writeShellApplication {
          name = "day24";
          runtimeInputs = [ getInput ];
          text = "";
        };
        day25 = pkgs.writeShellApplication {
          name = "day25";
          runtimeInputs = [
            pkgs.zig
            getInput
          ];
          text = "getInput 2024 25 | zig run ${./2024/day25.zig}";
        };
      };
    };
}
