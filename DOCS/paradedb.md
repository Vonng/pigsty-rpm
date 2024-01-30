# ParadeDB


```bash

git clone --recursive git@github.com:paradedb/paradedb.git

git clone --recursive https://github.com/paradedb/paradedb.git

cd postgresml; git checkout v2.8.1; 
cd ~/postgresml/pgml-extension
HTTPS_PROXY=http://xxx cargo update
```


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup install 1.73.0

# We recommend setting the default version to 1.73.0 for consistency across your system
rustup default 1.73.0

# Note: Replace --pg16 with your version of Postgres, if different (i.e. --pg15, --pg14, etc.)
cargo install --locked cargo-pgrx --version 0.11.2
```



### Run With Optimized Build

First, switch to latest Rust Nightly (as of writing, 1.77) via:

```bsah
rustup update nightly
rustup override set nightly
```

Then, reinstall pgrx for the new version of Rust:

```bsah
cargo install --locked cargo-pgrx --version 0.11.2 --force
```

Finally, run to build in release mode with SIMD:

```bsah
cargo pgrx run --release
```

Note that this may take several minutes to execute.

To revert back to the stable version of Rust, run:

```bsah
rustup override unset
```

Run Benchmarks
To run benchmarks locally, enter the pg_analytics/ directory and run cargo clickbench. This runs a minified version of the ClickBench benchmark suite on pg_analytics.