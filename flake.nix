{
  description = "Examples of python tools run against different code";

  inputs = {
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages."${system}";
        python = pkgs.python39.withPackages (p: with p; [ bandit ]);
        banditCheck = pkgs.writeShellApplication {
          name = "bandit-check";
          runtimeInputs = [ python ];
          text = ''
            bandit \
              --recursive bandit_example/ \
              --format json \
              --severity-level low \
              --confidence-level medium
          '';
        };
      in
      rec {
        checks.bandit = pkgs.runCommand "bandit-check" { buildInputs = [ banditCheck ]; } ''
          cd ${./.}
          bandit-check
          touch $out
        '';

        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            python
            banditCheck

            # Nix tooling
            nixpkgs-fmt
          ];
        };
      });
}
