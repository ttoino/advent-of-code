{
  projectRootFile = "flake.nix";

  programs = {
    clang-format.enable = true;
    dart-format.enable = true;
    fprettify.enable = true;
    gofmt.enable = true;
    ktfmt.enable = true;
    mix-format.enable = true;
    nixfmt.enable = true;
    ocamlformat.enable = true;
    ormolu.enable = true;
    prettier = {
      enable = true;
      settings = {
        printWidth = 80;
        singleQuote = false;
        tabWidth = 4;
        trailingComma = "all";
        useTabs = false;
        overrides = [
          {
            files = [
              "*.yml"
              "*.yaml"
            ];
            options = {
              tabWidth = 2;
            };
          }
        ];
      };
    };
    ruff-check = {
      enable = true;
      extendSelect = [ "I" ];
    };
    ruff-format = {
      enable = true;
      lineLength = 79;
    };
    rustfmt.enable = true;
    scalafmt.enable = true;
    shfmt = {
      enable = true;
      indent_size = 4;
    };
    stylua.enable = true;
    zig.enable = true;
  };

  settings = {
    excludes = [
      "build"
      "target"

      "*.apl"
      "*.i"
      "*.idr"
      "*.jl"
      "*.lock"
      "*.mac"
      "*.pl"
      "*.u"
      "*.vala"
      "*.wyv"
      "*.xtend"
    ];

    formatter.shfmt.includes = [ "*.zsh" ];
    formatter.stylua.options = [
      "--syntax"
      "Lua52"
    ];
  };
}
