{ pkgs, ... }:
rec {
  makeBin =
    {
      day,
      language,
      name,
      source,
      year,
      ...
    }:
    let
      lang = language {
        inherit
          day
          name
          source
          year
          ;
      };
    in
    pkgs.writeShellApplication {
      inherit name;
      runtimeInputs = [ getInput ] ++ lang.inputs;
      text = "get-input ${year} ${day} | ${lang.text}";
    };

  makeConfig = years: {
    packages.${pkgs.stdenv.hostPlatform.system} = builtins.mapAttrs (
      year: days:
      builtins.listToAttrs (
        pkgs.lib.imap1 (
          d: language:
          let
            day = builtins.toString d;
            paddedDay = padDay day;
          in
          {
            name = "day${paddedDay}";
            value =
              let
                name = "${year}day${paddedDay}";
                script = makeBin {
                  inherit
                    day
                    language
                    name
                    year
                    ;
                  source = ./${year}/day${paddedDay};
                };
              in
              script
              // {
                verify = pkgs.writeShellApplication {
                  name = "${name}-verify";
                  runtimeInputs = [
                    getOutput
                    script
                  ];
                  text = "diff <(get-output ${year} ${day}) <(${name} | rg --only-matching --pcre2 '(?<=Part \\d: |Solution: ).*')";
                };
              };
          }
        ) days
      )
    ) years;
  };

  aocRequest = pkgs.writeShellApplication {
    name = "aoc-request";
    runtimeInputs = [ pkgs.curl ];
    text = builtins.readFile ./scripts/aoc-request.sh;
  };

  getInput = pkgs.writeShellApplication {
    name = "get-input";
    runtimeInputs = [ aocRequest ];
    text = builtins.readFile ./scripts/get-input.sh;
  };

  getOutput = pkgs.writeShellApplication {
    name = "get-output";
    runtimeInputs = [
      aocRequest
      pkgs.ripgrep
    ];
    text = builtins.readFile ./scripts/get-output.sh;
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
    minizinc =
      language:
      {
        day,
        source,
        year,
        ...
      }:
      {
        inputs = [
          pkgs.minizinc
          (makeBin {
            inherit
              day
              language
              source
              year
              ;
            name = "input";
          })
        ];
        text = "input > /tmp/aoc${year}day${day}.dzn && minizinc --solver coin-bc ${source + ".mzn"} /tmp/aoc${year}day${day}.dzn";
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
        text = "nix eval --show-trace --raw --file ${source + ".nix"} --apply \"f: f ''$(get-input ${year} ${day})''\"";
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
        inputs = [
          (pkgs.python3.withPackages (pp: [
            pp.more-itertools
            pp.intervaltree
          ]))
        ];
        text = "python3 ${source + ".py"}";
      };
    rust = compiledLanguage (
      { bin, source, ... }:
      pkgs.runCommandCC bin { nativeBuildInputs = [ pkgs.rustc ]; } ''
        n="$out/bin/${bin}"
        mkdir -p $(dirname "$n")
        rustc --edition 2024 ${source + ".rs"} -o "$n"
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

  padDay = day: if (builtins.stringLength day) <= 1 then "0" + day else day;
}
