{ pkgs, ... }:
rec {
  makeConfig = years: {
    packages.${pkgs.stdenv.hostPlatform.system} = builtins.mapAttrs (
      year: days:
      builtins.listToAttrs (
        pkgs.lib.imap1 (
          d: language:
          let
            day = builtins.toString d;
            paddedDay = if (builtins.stringLength day) <= 1 then "0" + day else day;
          in
          {
            name = "day${paddedDay}";
            value =
              let
                name = "${year}day${paddedDay}";
                lang = language {
                  inherit day name year;
                  source = ./${year}/day${paddedDay};
                };
              in
              pkgs.writeShellApplication {
                inherit name;
                runtimeInputs = [ getInput ] ++ lang.inputs;
                text = "getInput ${year} ${day} | ${lang.text}";
              };
          }
        ) days
      )
    ) years;
  };

  getInput = pkgs.writeShellApplication {
    name = "getInput";
    runtimeInputs = [ pkgs.curl ];
    text = builtins.readFile ./get-input.sh;
  };

  compiledLanguage =
    package:
    { name, source, ... }:
    let
      bin = "${name}Bin";
    in
    {
      inputs = [ (package { inherit bin source; }) ];
      text = bin;
    };

  languages = {
    apl =
      { source, ... }:
      {
        inputs = [ (pkgs.dyalog.override { acceptLicense = true; }) ];
        text = "dyalog -script ${source + ".apl"} 2> /dev/null";
      };
    bash =
      { source, ... }:
      {
        inputs = [ pkgs.bash ];
        text = "bash ${source + ".bash"}";
      };
    c = compiledLanguage ({ bin, source, ... }: pkgs.writeCBin bin (builtins.readFile (source + ".c")));
    dart =
      { source, ... }:
      {
        inputs = [ pkgs.dart ];
        text = "dart run ${source + ".dart"}";
      };
    elixir =
      { source, ... }:
      {
        inputs = [ pkgs.elixir ];
        text = "elixir ${source + ".exs"}";
      };
    fortran = compiledLanguage (
      { bin, source, ... }:
      pkgs.runCommandCC bin { nativeBuildInputs = [ pkgs.gfortran ]; } ''
        n="$out/bin/${bin}"
        mkdir -p $(dirname "$n")
        gfortran -fimplicit-none -fcheck=all -ffree-line-length-512 ${source + ".f90"} -o "$n"
      ''
    );
    go =
      { source, ... }:
      {
        inputs = [ pkgs.go ];
        text = "go run ${source + ".go"}";
      };
    haskell =
      { source, ... }:
      {
        inputs = [ pkgs.ghc ];
        text = "runghc ${source + ".hs"}";
      };
    idris =
      { source, ... }:
      {
        inputs = [ pkgs.idris2 ];
        text = "idris2 -x elba --source-dir / ${source + ".idr"}";
      };
    julia =
      { source, ... }:
      {
        inputs = [ pkgs.julia ];
        text = "julia ${source + ".jl"}";
      };
    kotlin =
      { source, ... }:
      {
        inputs = [ pkgs.kotlin ];
        text = "kotlinc -script ${source + ".kts"}";
      };
    lua =
      { source, ... }:
      {
        inputs = [ pkgs.lua ];
        text = "lua ${source + ".lua"}";
      };
    maxima =
      { source, ... }:
      {
        inputs = [ pkgs.maxima ];
        text = "maxima --very-quiet --init-mac=${source + ".mac"} --batch-string='main()$'";
      };
    nix =
      {
        day,
        source,
        year,
        ...
      }:
      {
        inputs = [ pkgs.nix ];
        text = "nix eval --show-trace --raw --file ${source + ".nix"} --apply \"f: f ''$(getInput ${year} ${day})''\"";
      };
    ocaml =
      { source, ... }:
      {
        inputs = [ pkgs.ocaml ];
        text = "ocaml ${source + ".ml"}";
      };
    prolog =
      { source, ... }:
      {
        inputs = [ pkgs.swi-prolog ];
        text = "swipl -g main ${source + ".pl"}";
      };
    python =
      { source, ... }:
      {
        inputs = [ pkgs.python3 ];
        text = "python3 ${source + ".py"}";
      };
    rust = compiledLanguage (
      { bin, source, ... }:
      pkgs.runCommandCC bin { nativeBuildInputs = [ pkgs.rustc ]; } ''
        n="$out/bin/${bin}"
        mkdir -p $(dirname "$n")
        rustc ${source + ".rs"} -o "$n"
      ''
    );
    scala =
      { source, ... }:
      {
        inputs = [ pkgs.scala-cli ];
        text = "scala-cli run ${source + ".scala"}";
      };
    typescript =
      { source, ... }:
      {
        inputs = [ pkgs.deno ];
        text = "deno run ${source + ".ts"}";
      };
    ucm =
      { source, ... }:
      {
        inputs = [ pkgs.unison-ucm ];
        text = "ucm run.file ${source + ".u"} main";
      };
    vala =
      { source, ... }:
      {
        inputs = [ pkgs.vala ];
        text = "vala ${source + ".vala"}";
      };
    wyvern =
      { source, ... }:
      {
        inputs = [ ];
        text = "";
      };
    xtend =
      { source, ... }:
      {
        inputs = [ ];
        text = "";
      };
    yorick =
      { source, ... }:
      {
        inputs = [ ];
        text = "";
      };
    zig =
      { source, ... }:
      {
        inputs = [ pkgs.zig ];
        text = "zig run ${source + ".zig"}";
      };
  };

  repeat = count: element: if count <= 0 then [ ] else [ element ] ++ (repeat (count - 1) element);
}
