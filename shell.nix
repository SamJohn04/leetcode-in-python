let
    pkgs = import <nixpkgs> {};
in pkgs.mkShell {
    packages = with pkgs; [
      python312
      python312Packages.pytest
      python312Packages.setuptools
      nodePackages.pyright
    ];
}
