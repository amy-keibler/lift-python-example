# Lift Python Example

This repository provides examples of various tools run by Lift in order to facilitate manual testing.

## Examples

### Bandit Example

This demonstrates Bandit's ability to provide notes on both insecure code and use of disallowed functions/imports.

- `B402` - importing an FTP module instead of a secure data transfer option
- `B101` - using `assert`, which may produce unexpected behavior after compiled to bytecode

## Usage

If you have [`nix` installed](https://nixos.wiki/wiki/Nix_Installation_Guide) with flake support, you can have a devlopment shell with the proper tools installed by running `nix develop`. This shell also provides helpful wrappers in the form `<tool name>-check`, for you to run them with the same commandline arguments as Lift. If you have [`direnv`](https://direnv.net/) set up, there is an `.envrc` that automatically applies the development shell.
